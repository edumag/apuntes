En servidor

```bash
export DATABASE_IMAGE_VERSION="5.7.28"
dokku mysql:create $app-db
dokku apps:create $app
dokku mysql:link $app-db $app
dokku config:set --no-restart $app DOKKU_LETSENCRYPT_EMAIL=$email
dokku letsencrypt $app
## Necesario para conectar dockerfile con mysql.
dokku docker-options:add $app build '--build-arg DATABASE_URL=`dokku config:get $app DATABASE_URL`'
# ENlazar puertos.
dokku proxy:ports-set $app https:443:80
```

Forzamos instalación en dokku con version 5 de mysql:

```
Digest: sha256:5eb9da766abdd5e8cedbde9870acd4b54c1c7e63e72c99e338b009d06f808f04
Status: Downloaded newer image for dokku/wait:0.4.3
=====> MySQL container created: $app-db
=====> $app-db mysql service information
       Config dir:          /var/lib/dokku/services/mysql/$app-db/config
       Data dir:            /var/lib/dokku/services/mysql/$app-db/data
       Dsn:                 mysql://mysql:aaf38bcf30f9f7b4@dokku-mysql-$app-db:3306/$app_db
       Exposed ports:       -                        
       Id:                  57659c5f30ba8685f808cdda9f803d5047a0f653160f418da1190fa8cd682073
       Internal ip:         172.17.0.11              
       Links:               -                        
       Service root:        /var/lib/dokku/services/mysql/$app-db
       Status:              running                  
       Version:             mysql:5.5  
```

dokku config:show APP:

```
=====> APP env vars
DATABASE_URL:             mysql://mysql:aaf38bcf30f9f7b4@dokku-mysql-$app-db:3306/$app_db
DOKKU_APP_RESTORE:        1
DOKKU_APP_TYPE:           herokuish
DOKKU_LETSENCRYPT_EMAIL:  $email
DOKKU_PROXY_PORT:         80
DOKKU_PROXY_PORT_MAP:     http:80:5000 https:443:5000
DOKKU_PROXY_SSL_PORT:     443
GIT_REV:                  9d372d044671a592c85da947565f2213c411b884
```

## En local

Dockerfile

```
FROM php:5.6-apache

RUN a2enmod rewrite
RUN a2enmod ssl

RUN docker-php-ext-install mysql 
RUN docker-php-ext-enable mysql


COPY ./ /var/www/html/

EXPOSE 443
```

composer.json

```
{
  "require": {
    "php": "5.6"
  },
  "scripts": {
    "post-install-cmd": [
      "chmod -R 777 wp-content"
    ]
  }
}
```

