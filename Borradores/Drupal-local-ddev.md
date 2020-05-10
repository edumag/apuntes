# Desarrollo drupal con ddev

## Instalación de ddev


```bash
curl -L https://raw.githubusercontent.com/drud/ddev/master/scripts/install_ddev.sh | bash

cat /tmp/ddev_bash_completion.sh >> ~/.bashrc
```

## Iniciar proyecto drupal commerce

```bash
mkdir my-drupal8-commerce
cd my-drupal8-commerce
ddev config --project-type php
ddev start
ddev composer create drupalcommerce/project-base --stability dev --no-interaction
ddev config --project-type drupal8
ddev restart
drush sql-drop
drush cr
```

## Instalación desde el navegador

[`https://my-drupal8-commerce.ddev.site`](https://my-drupal8-commerce.ddev.site)

## Descargamos el tema base

```bash
mkdir web/themes/contrib
cd web/themes/contrib
git clone https://github.com/AcroMedia/orange_framework.git
```

## Creamos un subtema

```
mkdir web/themes/custom
cd web/themes/custom
git clone https://github.com/gxleano/commerce_2_demo_subtheme.git
```

A continuación necesitaremos instalar el tema base Orange Framework y el
Subtema Commerce 2 demo subtheme para poder configurar este último  como
predeterminado y listo. 

## Configuramos gulp para preprocessamiento de CSS/JS:

```
cd web/themes/custom/commerce_2_demo_subtheme
ddev ssh
cd web/themes/custom/commerce_2_demo_subtheme
npm install
node_modules/.bin/gulp
```

## MailHog

http://my-drupal8-commerce.ddev.site:8025

## PhpMyAdmin

http://my-drupal8-commerce.ddev.site:8036/

## Referencias

- https://www.solucionex.com/blog/como-instalar-drupal-commerce-con-subtema-custom

