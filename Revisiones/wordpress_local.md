# Wordpress en local con docker

Vamos a crear una instalación de cero de wordpress con docker.

Se crearán volúmenes tanto de la base de datos como de los ficheros
de wordpress, permitiendo su persistencia y mantener los cambios que
hagamos en el proyecto.

## Instalación de docker.

https://docs.docker.com/installation/

## Configuración.

Creamos fichero docker-compose.yml

```
version: '3.7'

services:
  mysql:
    image: mariadb:10
    network_mode: bridge
    container_name: mysql-gm
    volumes:
      - ./gm_db_data:/var/lib/mysql
    restart: on-failure
    environment:
      MYSQL_ROOT_PASSWORD: password # Password MYSQL Root
  adminer:
    image: adminer
    container_name: adminer-gm
    network_mode: bridge
    restart: always
    ports:
      - 8080:8080
    depends_on:
    - mysql
    links:
    - mysql
  web:
    image: wordpress
    network_mode: bridge
    container_name: wordpress-gm
    restart: on-failure
    volumes:
     - ./html:/var/www/html
    environment:
      WORDPRESS_DB_NAME: wordpress
    ports: 
    - 8002:80
    depends_on:
    - mysql
    links:
    - mysql
volumes:
  gm_db_data:
```

## Script run

```
#!/bin/bash

echo "Iniciamos docker"
sudo service docker start

echo "Levatamos contenedores docker desde docker-compose.yml"
docker-compose up
```

Permisos de ejecución:

    chmod +x run


Ejecutamos script run.

Vamos a http://localhost:8002 y configuramos wordpress.

En este caso nuestros los datos serían:

- Nombre de la base de datos: wordpress
- Host: mysql
- Usuario: root
- Password: password

Ahora tenemos:

- Wordpress en http://localhost:8002

- Adminer en http://localhost:8080

## Varios.

### Importar base de datos.

Una vez tengamos la base de datos del servidor en local tendremos que
transformar las urls, ejemplo https://DOMINIO.com por http://localhost:8001.

Del fichero local hacemos una copia para local:

```
sed -e 's/https:\/\/DOMINIO\.com/http:\/\/localhost:8001/g' DOMINIO-servidor.sql > DOMINIO-local.sql
```

Ejecutamos importación:

```
docker exec -i mysql-container mysql -uuser -ppassword name_db < DOMINIO-local.sql
```

Nota:
 En mi caso he tenido problemas con la codificación de caracteres y he tenido
 que hacerlo desde adminer.


#### Otros.

Borrar base de datos:
```
docker exec -i mysql-container mysql -uuser -ppassword name_db -e 'DROP DATABASE wordpress;'
```

Crear base de datos:

```
docker exec -i mysql-container mysql -uuser -ppassword -e 'CREATE DATABASE wordpress character set utf8;'
```



### Depurar.

### Mostrar mensajes de error.

Activamos registro de errores desde wp-config.php:

```
// Enable WP_DEBUG mode
define('WP_DEBUG', true);

// Enable Debug logging to the /wp-content/debug.log file
define('WP_DEBUG_LOG', true);

// Disable display of errors and warnings
define('WP_DEBUG_DISPLAY', true);

// Mostrar errores.
@ini_set('display_errors',1);

// Use dev versions of core JS and CSS files (only needed if you are modifying these core files)
define('SCRIPT_DEBUG', true);
```

Ejecutamos:

```
sudo docker exec -ti APPNAME bash
tail -f wp-content/debug.log
```


