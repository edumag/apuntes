# Seguridad y configuración de servidor

En estos días extraños de confinamiento parece que se ha multiplicado los
ataques en internet, en mi caso consiguieron entrar en mi vps y dejarlo
completamente inútil.

Aquí quedan los pasos que he recopilado para mantener el servidor con un mínimo
de seguridad.



## ssh

### Cambio de puerto

`sudo vim /etc/ssh/sshd_config`

    - # Port 22
    + Port 3333 # El que tu quieras en verdad.

Reiniciamos servicio:

`sudo /etc/init.d/ssh restart`

Ahora para entrar de nuevo deberemos especificar el puerto.

`ssh -p port user@server`

Incluso añadirlo en el ~/.ssh/config para no tener que especificarlo todo el
rato.

    Host server
        IdentityFile ~/.ssh/id_rsa                                          
        User ubuntu                                                         
        Hostname server.com                                            
        Port 1111


### sshd_config

Configuración más que recomendada:

Si activamos estas reglas tener en cuenta que tenéis que tener configurado
previamente la llave ssh en tu ordenador y añadida al servidor.

    PermitRootLogin no        # No se permite acceso a root desde ssh.
    AllowUsers USER1 USER2    # Lista de usuarios que si pueden entrar.
    PasswordAuthentication no # Solo permitimos entrar con clave ssh.

## Cortafuegos

    sudo ufw allow http
    sudo ufw allow https
    sudo ufw allow [SSH PORT]
    sudo ufw disable && sudo ufw enable

## Swap

Tener swap es fundamental para evitar fallos por falta de memoria.

Con esta formula creamos un fichero que nos servirá como swap en caso de que
nuestro servidor no la tenga habilitada.

    fallocate -l 3G /swapfile
    chmod 600 /swapfile
    mkswap /swapfile
    swapon /swapfile


sudo vim /etc/fstab

    /swapfile swap swap defaults 0 0

## PostFix con SMTP.

Si teneis un servidor de correo contratado podeis configurar postfix para
que envie los correos desde él.

Si quereis utilizar un gmail tendreis que buscar como hacerlo.

Configuramos servidor de correo para poder recibir correos de aviso.

`sudo apt.get install postfix`

Seleccionamos "Internet site"

y ponemos el nombre del servidor smtp.

### Configuración

`sudo vim /etc/postfix/main.cf`

modificamos:

```
myhostname = example.com
relayhost = [mail.isp.example]:587
# enable SASL authentication
smtp_sasl_auth_enable = yes
# disallow methods that allow anonymous authentication.
smtp_sasl_security_options = noanonymous
# where to find sasl_passwd
smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
# Enable STARTTLS encryption
smtp_use_tls = yes
# where to find CA certificates
smtp_tls_CAfile = /etc/ssl/certs/ca-certificates.crt
```

Credenciales:

Añadimos nuestras credenciales de nuestro servidor smtp.

`sudo vim /etc/postfix/sasl_passwd`

	[mail.isp.example]:587 username:password

```
sudo postmap /etc/postfix/sasl_passwd
sudo chown root:root /etc/postfix/sasl_passwd /etc/postfix/sasl_passwd.db
sudo chmod 0600 /etc/postfix/sasl_passwd /etc/postfix/sasl_passwd.db
sudo rm /etc/postfix/sasl_passwd
```

Reiniciamos postfix:

`sudo service postfix restart`

### Enviar correo.

    sudo apt-get install mpack
    echo "Test" > /tmp/test.txt
    mpack -s 'test' /tmp/test.txt tu@email.com


### Referencias:

- https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postfix-on-ubuntu-18-04-es

## fail2ban

`sudo apt-get install fail2ban`

Copiamos configuración por defecto a fichero personalizado.

`sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local`

Editar configuración:

`sudo vim /etc/fail2ban/jail.local`

Podemos añadir una lista de IPs para que sean ignoradas:

	ignoreip = 127.0.0.1/8 ::1 

Añadimos reglas para los wordpress:

    [ssh]
    enabled  = true
    port     = ssh
    filter   = sshd
    logpath  = /var/log/auth.log
    maxretry = 3
    bantime  = 1h

    [wordpress]
    enabled  = true
    filter   = wordpress
    logpath  = /var/log/nginx/*.log
    port     = 80,443
    bantime  = 1h

Creamos fichero /etc/fail2ban/filter.d/wordpress.conf y añadimos:

    # Fail2Ban filter for WordPress
    [Definition]
    failregex =  - - \[(\d{2})/\w{3}/\d{4}:\1:\1:\1 -\d{4}\] "POST /wp-login.php HTTP/1.1" 200
    ignoreregex =

Reiniciamos:

`sudo systemctl restart fail2ban`

Ver estado:

```
$ sudo fail2ban-client status

Status
|- Number of jail:	3
`- Jail list:	ssh, sshd, wordpress

$ sudo fail2ban-client status ssh
Status for the jail: ssh
|- Filter
|  |- Currently failed:	3
|  |- Total failed:	11
|  `- File list:	/var/log/auth.log
`- Actions
   |- Currently banned:	5
   |- Total banned:	6
   `- Banned IP list:	104.248.176.46 106.12.125.140 163.172.166.223 37.187.181.182 51.68.89.100
```

### Consultar logs de fail2ban

Número de veces que han sido bloqueada las IPs:

`zgrep -h "Ban " /var/log/fail2ban.log* | awk '{print $NF}' | sort | uniq -c`

### Referencias:

- https://raiolanetworks.es/blog/bloquear-ataques-dos-con-fail2ban-en-linux/
- https://geekland.eu/como-consultar-logs-de-fail2ban/

## Logcheck

`sudo apt-get install logcheck`

### Configuración

`sudo vim /etc/logcheck/logcheck.conf`

Modificamos:

```
SENDMAILTO="edu@lesolivex.com"
MAILASATTACH=1
```

### Configurando las reglas

`sudo vim /etc/logcheck/ignore.d.server/edumag`

Utilizamos expresiones regulares para indicar las lineas que no queremos mostrar.

```
*.from\ 251.red-79-157-159.dynamicip.rima-tde.net*
```

Probamos la salida:

`sudo -u logcheck logcheck -o -t`

Referencias:

• http://somebooks.es/recibir-informes-sobre-sucesos-de-ubuntu-server-18-04-lts-con-logcheck/

## Actualizaciones de seguridad automáticas

`sudo dpkg-reconfigure --priority=low unattended-upgrades`

Referencias:

• https://help.ubuntu.com/community/AutomaticSecurityUpdates

## Varios

### Ver reglas del cortafuegos:

`sudo iptables -L -n --line-numbers`

### Ver IPs bloqueadas:

`sudo iptables -L -n --line-numbers | grep REJECT`

### Lynis

Lynis nos genera un informe muy completo sobre el estado de nuestro servidor y
nos da sugerencias.

`sudo apt-get install lynis`

`sodo lynis audit system`

### chkrootkit

Permite localizar rootkits.

`sudo apt-get install rootkits`

`sudo chkrootkit`

## Extras

### Scripts
He realizado unos pequeños scripts para tener una visión del estado
del servidor de forma rapida.

[https://github.com/edumag/magscripts/tree/master/servidor/ReportServer](https://github.com/edumag/magscripts/tree/master/servidor/ReportServer) https://github.com/edumag/magscripts/tree/master/servidor/ReportServer

Los scripts están separados por temas así que es facil eliminar los que no te interesan o añadir otros.

#### Envío del informe.

`sudo ./reportServer.sh > /tmp/report.txt && mpack -s repor /tmp/report.txt  edu@lesolivex.com`



