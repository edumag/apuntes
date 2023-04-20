## Servidor

### Instalar en servidor

`sudo apt-get install knockd`

### Configuración

#### /etc/default/knockd

```
# control if we start knockd at init or not   
# 1 = start                                   
# anything else = don't start                 
# PLEASE EDIT /etc/knockd.conf BEFORE ENABLING
START_KNOCKD=1                                
                                              
# command line options                        
KNOCKD_OPTS="-i ens3"
```

#### /etc/knockd.conf

Ejemplo que viene por defecto.

```
[options]
        UseSyslog

[openSSH]
        sequence    = 7000,8000,9000
        seq_timeout = 5
        command     = /sbin/iptables -A INPUT -s %IP% -p tcp --dport 5775 -j ACCEPT
        tcpflags    = syn

[closeSSH]
        sequence    = 9000,8000,7000
        seq_timeout = 5
        command     = /sbin/iptables -D INPUT -s %IP% -p tcp --dport 5775 -j ACCEPT
        tcpflags    = syn
```

## Cliente

`sudo apt-get install knockd`

### Abriendo puerto

`knock localhost 7000 8000 9000`

### Cerrando puerto

`knock localhost 9000 8000 7000`


