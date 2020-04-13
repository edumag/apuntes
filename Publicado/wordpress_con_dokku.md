# Wordpress con dokku

**Actualización**: abril del 2020


## VPS

Contratamos maquina virtual con OVH.

Al entrar nos muestra mensaje de error:

```
warning: setlocale: LC_ALL: cannot change locale (es_ES.UTF-8)
```

Entramos por ssh y configuramos locales.

```
sudo dpkg-reconfigure locales
```

Configuramos los DNS para que nuestro dominio apunte al servidor.

Tipo A, Host: @, TUIP, TTL: 900
Tipo A, Subdominios: *


## Instalación

Seguimos documentación de [dokku](http://dokku.viewdocs.io/dokku/) 

    wget https://raw.githubusercontent.com/dokku/dokku/v0.17.9/bootstrap.sh
    sudo DOKKU_TAG=v0.17.9 bash bootstrap.sh


http://IP_DE_LA_MAQUINA

Copiamos nuestra clave pública desde nuestro local en .ssh/id_rsa.pub en el formulario y guardamos.

Dokku instalado!!!!


## Instalación wordpress

### Desde maquina virtual


```
sudo dokku plugin:install https://github.com/dokku/dokku-mysql.git mysql
sudo dokku plugin:install https://github.com/dokku/dokku-letsencrypt.git

dokku apps:create TUDOMINIO
dokku domains:add TUDOMINIO TUDOMINIO.com
dokku domains:add TUDOMINIO www.TUDOMINIO.com
dokku mysql:create gmdb
```

Creamos volúmenes:

```
sudo mkdir -p /var/lib/dokku/data/storage/TUDOMINIO/uploads

sudo chmod -R 755 /var/lib/dokku/data/storage/

dokku storage:mount TUDOMINIO /var/lib/dokku/data/storage/TUDOMINIO/uploads/:/app/wp-content/uploads/
```

#### Conexión con base de datos en dokku

```
dokku mysql:link gmdb TUDOMINIO
```

Creado el enlace entre la aplicación y el servicio de la base de datos,
tendremos en el fichero /home/dokku/TUDOMINIO/ENV de la aplicación la información para conectar con
ella en forma de variable de entorno que aprovecharemos más adelante para
recoger y conectar con la base de datos.


### Desde local

Debemos tener una instancia de wordpress en local.

Para ello puedes ver el post [Wordpress en local don docker](http://lesolivex.com/wordpress-en-local-con-docker/)

Nos situamos en la carpeta donde tenemos nuestro wordpress local, en mi caso la
carpeta html  y creamos .gitignore con el siguiente contenido:

```
.heroku/
.profile.d/
.composer/
.builders_run
.release
*.log
*.swp
*.back
*.bak
*.sql
*.sql.gz
~*
.htaccess
.maintenance
wp-content/blogs.dir/
wp-content/upgrade/
wp-content/backup-db/
wp-content/cache/
wp-content/backups/
wp-content/uploads/
secret/
/vendor/
# En mi caso añado.
.magtrabajos
```

Nota

: En caso de tener problemas de permisos con la carpeta local de wordpress
podeis ejecutar el siguiente comando: sudo chown -R www-data:$USER html/
 

Creamos compser.json:

```
{
  "require": {
    "php": "~7",
    "ext-mbstring" : "*",
    "ext-gd": "*"
  },
  "scripts": {
    "post-install-cmd": [
      "chmod -R 777 wp-content"
    ]
  }
}
```

Creamos fichero nginx_app.conf:

```
# WordPress permalinks                                                          
location / {                                                                    
  index index.php index.html;                                                   
  try_files $uri $uri/ /index.php?$args;                                        
}  

# Add trailing slash to */wp-admin requests.                                    
rewrite /wp-admin$ $scheme://$host$uri/ permanent;                              
                                                                                
# Deny access to any files with a .php extension in the uploads directory       
# Works in sub-directory installs and also in multisite network                 
location ~* /(?:uploads|files)/.*.php$ {                                        
  deny all;                                                                     
}                                                                               
                                                                                
#upload                                                                         
client_max_body_size 100M;                                                      
                                                                                
#jetpack connection                                                             
fastcgi_buffers 8 32k;                                                          
fastcgi_buffer_size 64k;                                                        
proxy_buffer_size 128k;                                                         
proxy_buffers 4 256k;                                                           
proxy_busy_buffers_size 256k;                                                   
proxy_read_timeout 300;
                                                                                
# enable gzip compression                                                       
gzip on;                                                                        
# Minimum file size in bytes (really small files aren’t worth compressing)      
gzip_min_length 1000;                                                           
# Compression level, 1-9                                                        
gzip_comp_level 2;                                                              
gzip_buffers 4 32k;                                                             
gzip_types text/plain application/javascript text/xml text/css image/svg+xml;   
# Insert `Vary: Accept-Encoding` header, as specified in HTTP1.1 protocol       
gzip_vary on;                                                                   
# end gzip configuration                                                        
                                                                                
# Set time to expire for headers on assets                                      
location ~* .(js|css|png|jpg|jpeg|gif|ico|svg)$ {                               
  expires 1y;                                                                   
}                                                                               
                                                                                
# Sitemap url, for WordPress SEO plugin                                         
#rewrite ^/sitemap_index.xml$ /index.php?sitemap=1 last;                        
#rewrite ^/([^/]+?)-sitemap([0-9]+)?.xml$ /index.php?sitemap=$1&sitemap_n=$2 last;

# Global restrictions configuration file.
# Designed to be included in any server {} block.
location = /favicon.ico {
 log_not_found off;
 access_log off;
}

location = /robots.txt {
 allow all;
 log_not_found off;
 access_log off;
}

# Deny all attempts to access hidden files such as .htaccess, .htpasswd, .DS_Store (Mac).
# Keep logging the requests to parse later (or to pass to firewall utilities such as fail2ban)
location ~ /\. {
 deny all;
}

# Deny access to any files with a .php extension in the uploads directory
# Works in sub-directory installs and also in multisite network
# Keep logging the requests to parse later (or to pass to firewall utilities such as fail2ban)
location ~* /(?:uploads|files)/.*\.php$ {
 deny all;
}

# Add trailing slash to */wp-admin requests.
rewrite /wp-admin$ $scheme://$host$uri/ permanent;

# Directives to send expires headers and turn off 404 error logging.
location ~* ^.+\.(ogg|ogv|svg|svgz|eot|otf|woff|mp4|ttf|rss|atom|jpg|jpeg|gif|png|ico|zip|tgz|gz|rar|bz2|doc|xls|exe|ppt|tar|mid|midi|wav|bmp|rtf)$ {
 access_log off; log_not_found off; expires max;
}

```

Creamos fichero custom_php.ini

```
upload_max_filesize = 50M
post_max_size = 50M
```

Creamos fichero Procfile:

```
web: vendor/bin/heroku-php-nginx -C nginx_app.conf -i custom_php.ini --verbose
```

Lanzamos composer update para que nos genere el composer.lock.

```
composer update
```

Iniciamos git y añadimos repositorio de dokku y subimos proyecto.

```
git init
git remote add dokku dokku@TUDOMINIO.com:TUDOMINIO
git add .
git commit -am 'Init'
git push dokku master
```

En estos momentos tenemos la aplicación funcionando pero el fichero
wp.config.php de wordpress contiene la configuración local y nos da error de
conexión.

Vamos a modificar el fichero wp-config.php por el del proyecto dokku-wordpress
que nos permite coger la configuración de las variables de entorno y en local
cogerá las que tengamos en el fichero por defecto.

Contenido de wp-config.php:

```
<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

function fromenv($key, $default = null) {
  $value = getenv($key);
  if ($value === false) {
    $value = $default;
  }
  return $value;
}

$DSN = parse_url(fromenv('DATABASE_URL', 'mysql://username_here:password_here@localhost:3306/database_name_here'));

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', substr($DSN['path'], 1));

/** MySQL database username */
define('DB_USER', $DSN['user']);

/** MySQL database password */
define('DB_PASSWORD', $DSN['pass']);

/** MySQL hostname */
define('DB_HOST', $DSN['host']);

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         fromenv('AUTH_KEY', 'put your unique phrase here'));
define('SECURE_AUTH_KEY',  fromenv('SECURE_AUTH_KEY', 'put your unique phrase here'));
define('LOGGED_IN_KEY',    fromenv('LOGGED_IN_KEY', 'put your unique phrase here'));
define('NONCE_KEY',        fromenv('NONCE_KEY', 'put your unique phrase here'));
define('AUTH_SALT',        fromenv('AUTH_SALT', 'put your unique phrase here'));
define('SECURE_AUTH_SALT', fromenv('SECURE_AUTH_SALT', 'put your unique phrase here'));
define('LOGGED_IN_SALT',   fromenv('LOGGED_IN_SALT', 'put your unique phrase here'));
define('NONCE_SALT',       fromenv('NONCE_SALT', 'put your unique phrase here'));

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix  = fromenv('TABLE_PREFIX', 'wp_');

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the Codex.
 *
 * @link https://codex.wordpress.org/Debugging_in_WordPress
 */
define('WP_DEBUG', (bool)fromenv('WP_DEBUG', false));

// If we're behind a proxy server and using HTTPS, we need to alert Wordpress of that fact
// see also http://codex.wordpress.org/Administration_Over_SSL#Using_a_Reverse_Proxy
if ( isset($_SERVER['HTTP_X_FORWARDED_PROTO'] )
    && $_SERVER['HTTP_X_FORWARDED_PROTO'] === 'https' )
{
    $_SERVER['HTTPS'] = 'on';
}

/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
  define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');
```

### Desde la web

http://TUDOMINIO.com

Y ya podemos hacer la configuración desde el dominio.

Ahora nos faltará como gestionar los cambios que hagamos en local
sobre nuestro tema personalizado o nuestros plugins ya que la idea
es que wordpress se actualice por si solo desde el servidor.


## Configurar los keys y salts de seguridad

Vamos a https://api.wordpress.org/secret-key/1.1/salt/ para generar las claves.

Y las añadimos a la configuración del proyecto.

```
dokku config:set wp AUTH_KEY='...your key...'
dokku config:set wp SECURE_AUTH_KEY='...your key...'
dokku config:set wp LOGGED_IN_KEY='...your key...'
dokku config:set wp NONCE_KEY='...your key...'
dokku config:set wp AUTH_SALT='...your key...'
dokku config:set wp SECURE_AUTH_SALT='...your key...'
dokku config:set wp LOGGED_IN_SALT='...your key...'
dokku config:set wp NONCE_SALT='...your key...'
```

#### Letsencrypt.

```
dokku config:set --no-restart TUDOMINIO DOKKU_LETSENCRYPT_EMAIL=TUCORREO@TUCORREO.com
dokku letsencrypt TUDOMINIO
dokku letsencrypt:auto-renew
dokku letsencrypt:cron-job --add
```

### Varios

#### Importación de la base de datos.

En caso de querer importar nuestra base de datos local dokku.

Podemos crear nuestra copia de la base de datos desde adminer.

Subimos el fichero al servidor y ejecutamos:

```
cat wordpress.sql | ssh dokku@TUDOMINIO.com mysql:import gmdb < .
```

> **Nota:** Tener en cuenta que será necesario cambiar las urls del fichero
antes de importar. Ejemplo: localhost:8002 por TUDOMINIO


#### Entrar a una consola de un container:

```
dokku run APLICACION bash
```

#### Lanzar comandos de dokku desde local:

```
ssh dokku@TUDOMINIO.com help
```

#### Logs.

Errores desde dokku:

```
ssh dokku@lesolivex.com dokku logs:failed menjut
```

Logs de acceso:

```
ssh dokku@lesolivex.com dokku logs menjut -t
```

Errores en nginx:

```
ssh dokku@lesolivex.com nginx:error-logs menjut -t
```

Log de mysql:

```
ssh dokku@lesolivex.com mysql:logs menjutdb -t
```

### Referencias:

- [playcode, Worpress digitalocean dokku](https://playcode.org/setup-wordpress-blog-digitalocean-using-dokku/)

- [Comunidad dokku](https://github.com/dokku-community/dokku-wordpress)

- [Vídeo tutorías completo](https://www.youtube.com/watch?v=fAEO8nLHXP://www.youtube.com/watch?v=fAEO8nLHXPI)

- [sysrun, instalando wordpress sobre dokku](https://www.sysrun.io/2015/11/03/installing-wordpress-on-dokku/)

- [Letsencrypt con dokku](https://blog.enjambrelab.com.ar/https-en-dokku-con-lets-encrypt/)

