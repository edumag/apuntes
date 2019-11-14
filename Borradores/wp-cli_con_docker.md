# WP-CLI con Docker

Para poder tener wp-cli en local utilizaremos una imagen de wordpress
que lo contenga.

## Fichero docker-compose.yml:

```
version: '3.7'
 
services:
  mysql:
    image: mariadb:10
    network_mode: bridge
    container_name: mysql-lo
    volumes:
      - ./gm_db_data:/var/lib/mysql
    restart: on-failure
    environment:
      MYSQL_ROOT_PASSWORD: password # Password MYSQL Root
  adminer:
    image: adminer
    container_name: adminer-lo
    network_mode: bridge
    restart: always
    ports:
      - 8080:8080
    depends_on:
    - mysql
    links:
    - mysql
  web:
    image: conetix/wordpress-with-wp-cli
    network_mode: bridge
    container_name: wordpress-lo
    restart: on-failure
    volumes:
      - ./html:/var/www/html
    environment:
      WORDPRESS_DB_NAME: wordpress
    ports: 
      - 8001:80
    depends_on:
      - mysql
    links:
    - mysql
volumes:
  gm_db_data:
```

## Abrir una consola en wpcli

```
docker-compose exec web wp --info
```

## Comandos de ejemplo

### Actualizar todos los plugins

```
wp plugin update --all
```

### Actualizar wordpress y base de datos

```
wp core update
wp core update-db
```

### Volver a una versión concreta.

```
wp core update --version=3.1 --force

```

## Referencias:

- [neliosoftware.com](https://neliosoftware.com/es/blog/como-gestionar-wordpress-desde-la-linea-de-comandos-con-wp-cli/)
- [developer.wordpress.org](https://developer.wordpress.org/cli/commands/) 
