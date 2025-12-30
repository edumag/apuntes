# Preparar servidor VPS Debian 13

Post instalación de servidor linux debian 13, y configuración de seguridad.

```bash
$ fastfetch
        _,met$$$$$gg.          debian@vps-58a7ea55
     ,g$$$$$$$$$$$$$$$P.       -------------------
   ,g$$P""       """Y$$.".     OS: Debian GNU/Linux 13 (trixie) x86_64
  ,$$P'              `$$$.     Host: OpenStack Nova (19.3.2)
',$$P       ,ggs.     `$$b:    Kernel: Linux 6.12.57+deb13-cloud-amd64
`d$$'     ,$P"'   .    $$$     Uptime: 55 mins
 $$P      d$'     ,    $$P     Packages: 417 (dpkg)
 $$:      $$.   -    ,d$$'     Shell: bash 5.2.37
 $$;      Y$b._   _,d$P'       Terminal: /dev/pts/1
 Y$$.    `.`"Y$$$$P"'          CPU: 4 x Intel Core (Haswell, no TSX) (4) @ 2.39 GHz
 `$$b      "-.__               GPU: Cirrus Logic GD 5446
  `Y$$b                        Memory: 409.91 MiB / 7.58 GiB (5%)
   `Y$$.                       Swap: Disabled
     `$$b.                     Disk (/): 1.59 GiB / 73.62 GiB (2%) - ext4
       `Y$$b.                  Local IP (ens3): **.**.***.*/32
         `"Y$b._               Locale: es_ES.UTF-8
             `""""
```

## Actualizar

    sudo apt update && sudo apt upgrade

## Instalar locales

    sudo dpkg-reconfigure locales
    sudo apt-get install locales-all

## rsyslog

    sudo apt-get install --reinstall rsyslog

## ssh

### Cambio de puerto

    sudo vim /etc/ssh/sshd_config

    - # Port 22
    + Port 3333 # El que tu quieras en verdad.

Reiniciamos servicio:

    sudo systemctl restart sshd

Ahora para entrar de nuevo deberemos especificar el puerto.

    ssh -p port user@server

Incluso añadirlo en el ~/.ssh/config para no tener que especificarlo todo el
rato.

    Host server
        IdentityFile ~/.ssh/id_rsa
        User ubuntu
        Hostname server.com
        Port 1111

### Llave ssh

Copiar llave publica al servidor para poder entrar sin contraseña.

    ssh-copy-id -i ~/.ssh/LLAVE USUARIO@SERVIDOR

### sshd_config

Configuración más que recomendada:

Si activamos estas reglas tener en cuenta que tenéis que tener configurado
previamente la llave ssh en tu ordenador y añadida al servidor.

    PermitRootLogin no        # No se permite acceso a root desde ssh.
    AllowUsers USER1 USER2    # Lista de usuarios que si pueden entrar.
    PasswordAuthentication no # Solo permitimos entrar con clave ssh.

## Servidor de correo

    sudo apt install postfix

Seleccionamos "Internet site"

y ponemos el nombre del servidor smtp.

### Configuración de postfix

Configuramos servidor de correo para poder recibir correos de aviso.

### /etc/postfix/main.cf

Modificamos configuración para que no acepte correo del exterior.

    inet_interfaces = loopback-only

### /etc/aliases

    mailer-daemon: postmaster
    postmaster: root
    root: TU_EMAIL
    logcheck: root
    nobody: root
    hostmaster: root
    usenet: root
    news: root
    webmaster: root
    www: root
    ftp: root
    abuse: root
    noc: root
    security: root

Activamos los nuevos alias y reiniciamos servidor postfix.

```
sudo newaliases
sudo systemctl restart postfix
```

### Enviar correo.

    sudo apt-get install mpack
    echo "Test" > /tmp/test.txt
    mpack -s 'test' /tmp/test.txt tu@email.com

## logcheck

sudo apt install logcheck

### Configuración de logcheck

`sudo vim /etc/logcheck/logcheck.conf`

Modificamos:

```
SENDMAILTO="TU_EMAIL"
MAILASATTACH=1
```

Editamos el fichero /etc/logcheck/ignore.d.server/custom

Aunque se puede poner el nombre que se quiera.

```
.*.from\ 251.red-79-157-159.dynamicip.rima-tde.net*
.*Synchronized\ to\ time\ server*
.*.\[UFW\ BLOCK\]*
.*filtering\ via\ arp/ip/ip6tables\ is\ no\ longer\ available*
.*Initializing\ XFRM\ netlink\ socket*
.*Netfilter\ messages\ via\ NETLINK*
.*ctnetlink\ v0.93:\ registering\ with\ nfnetlink.*
.*systemd-udevd*
.*networkd-dispatcher*
.*systemd-networkd*
.*IPv6:*
.*Link\ UP*
.*entered\ promiscuous\ mode*
.*entered\ blocking\ state*
.*can\ be\ used\ to\ set\ a\ preferred\ IP\ address*
.*Network\ configuration\ changed*
.*docker0*
.*eth0*
.*snapd*
.*containerd*
.*ovpn-server.*peer\ info*
.*ovpn-server.*VERIFY\ OK*
.*ovpn-server.*Initial\ packet*
.*ovpn-server.*Connection\ Initiated*
.*ovpn-server.*Control\ Channel*
```


`.*.from\ 251.red-79-157-159.dynamicip.rima-tde.net*`

Evitamos que nos avise ya que se trata de nuestros clientes de nextcloud intentando conectar cuando esta el ordenador de casa apagado.

`.*.Synchronized\ to\ time\ server*.ntp.ubuntu.com*`

Servidor actualizando la hora del sistema.

`.*.\[UFW\ BLOCK\]*`

Ips bloqueadas, son demasiadas.


### Probamos la salida:

`sudo -u logcheck logcheck -o -t`

Referencias:

• http://somebooks.es/recibir-informes-sobre-sucesos-de-ubuntu-server-18-04-lts-con-logcheck/

## Actualizaciones de seguridad automáticas

`sudo dpkg-reconfigure --priority=low unattended-upgrades`

Referencias:

• https://help.ubuntu.com/community/AutomaticSecurityUpdates

## Cortafuegos

    sudo apt install ufw

    sudo ufw allow http
    sudo ufw allow https
    sudo ufw allow [SSH PORT]
    sudo ufw disable && sudo ufw enable

### Status

    sudo ufw status

```
Status: active

To                         Action      From
--                         ------      ----
80/tcp                     ALLOW       Anywhere
443                        ALLOW       Anywhere
22/tcp                     ALLOW       Anywhere
80/tcp (v6)                ALLOW       Anywhere (v6)
443 (v6)                   ALLOW       Anywhere (v6)
22/tcp (v6)                ALLOW       Anywhere (v6)
```

### Ver reglas del cortafuegos:

`sudo iptables -L -n --line-numbers`

### Ver IPs bloqueadas:

`sudo iptables -L -n --line-numbers | grep REJECT`

## fail2ban

Evitar accesos no autorizados al servidor.

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

Desde systemd:

    sudo systemctl status fail2ban

### Consultar logs de fail2ban

Número de veces que han sido bloqueada las IPs:

`zgrep -h "Ban " /var/log/fail2ban.log* | awk '{print $NF}' | sort | uniq -c`

### Referencias:

- https://raiolanetworks.es/blog/bloquear-ataques-dos-con-fail2ban-en-linux/
- https://geekland.eu/como-consultar-logs-de-fail2ban/

## Varios

### Lynis

Lynis nos genera un informe muy completo sobre el estado de nuestro servidor y
nos da sugerencias.

    sudo apt-get install lynis

    sodo lynis audit system

### chkrootkit

Permite localizar rootkits.

    sudo apt install chkrootkit

    sudo chkrootkit

### Clamav

    sudo apt install clamav clamav-daemon clamav-freshclam clamdscan

Actualizar base d datos de virus.

    sudo freshclam

Evitar que arranque al inicio.

    sudo systemctl disable clamav-freshclam.service

### Scripts

He realizado unos pequeños scripts para tener una visión del estado
del servidor de forma rápida.

#### Instalar

    git clone https://github.com/edumag/magscripts

Los scripts están separados por temas así que es fácil eliminar los que no te interesan o añadir otros.

Instalar dependencias:

    sudo apt-get install chkrootkit clamscan docker

#### Ejecutar

    cd magscripts/servidor
    sudo ./magReportServer

#### Envío del informe.

    sudo ./magReportServer > /tmp/report.txt && mpack -s repor /tmp/report.txt  TU_EMAIL

