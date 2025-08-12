# Post instalación en Raspberry Pi

## Automatizar montado de disco externo

### Idiomas

    sudo echo "es_ES.UTF-8 UTF-8" >> /etc/locale.gen
    sudo locale-gen

## Instalación de Nginx Proxy Manager

```
services:
  app:
    image: 'jc21/nginx-proxy-manager:latest'
    restart: unless-stopped
    ports:
      - '80:80'
      - '81:81'
      - '443:443'
    volumes:
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt
    networks:
      - npm

networks:
  npm:
    name: npm
    driver: bridge
```


El usuario y el password por defecto de npm es:

admin@example.com changeme


## Instalación de nextcloud

Instalamos docker y docker-compose

    sudo apt install docker docker-compose

Permisos para usuario

    sudo usermod -aG docker $USER

## Añadir disco externo

### /etc/fstab

    UUID=UUID-DEL-UN-UNICO-UNICO /mnt/data/ext4 default,noatime 0 0

Puedes utilizar el comando **blkid** para obtener el UUID.

Permisos:

    sudo chmod 770 /mnt/data/nextcloud/data
    sudo chown -R 1000:33 /mnt/data/nextcloud/data

El usuario 1000 en mi caso es edumag.
El usuario 33 es www-data.

## nextcloud/docker-compose.yml

```
version: '3'

services:

  db:
    image: mariadb
    container_name: nextcloud-mariadb
    volumes:
      - db:/var/lib/mysql
      - /etc/localtime:/etc/localtime:ro
    environment:
      - MYSQL_ROOT_PASSWORD=xxxxxxxxxxxxxx
      - MYSQL_PASSWORD=xxxxxxxxxxxxxx
      - MYSQL_DATABASE=nextcloud
      - MYSQL_USER=nextcloud
    restart: unless-stopped
    networks:
      - nextcloud

  app:
    image: nextcloud:latest
    container_name: nextcloud-app
    depends_on:
      - db
    volumes:
      - nextcloud:/var/www/html
      - ./app/custom_apps:/var/www/html/custom_apps
      - ./app/themes:/var/www/html/themes
      - ./app/config:/var/www/html/config
      - /mnt/data/nextcloud/data:/var/www/html/data
      - /etc/localtime:/etc/localtime:ro
    environment:
      - VIRTUAL_HOST=lesolivex.dynv6.net
      - LETSENCRYPT_HOST=lesolivex.dynv6.net
      - LETSENCRYPT_EMAIL=edu@lesolivex.com
    restart: unless-stopped
    networks:
      - npm
      - nextcloud

volumes:
  nextcloud:
  db:
networks:
  nextcloud:
    name: nextcloud
    driver: bridge
  npm:
    external: true
```

## Ejecutar comandos desde docker-compose

    docker exec -it --user www-data nextcloud-app bash

### Buscar ficheros no indexados

    docker exec -it --user www-data nextcloud-app  php occ files:scan --all

### Añadir dominio de confianza

    docker exec -it --user www-data nextcloud-app php occ config:system:set trusted_domains 2 --value=raspberrypi

## NoIP


