# Odoo

## Acceder a la base de datos

Desde la url [tuDominio]/web/database/manager

Se pueden hacer backups y restaurar base de datos.

Con una base datos nueva el login lo puedes hacer con admin::admin

## Errores comunes

    psycopg2.errors.UndefinedColumn: column res_partner.aeat_simplified_invoice does not exist

Base de datos sin migraciones.

Ejecutar upgrade para corregir.

Desde el container se puede ejecutar:

odoo  --db_host DB_HOST --db_port 5432 --db_user USER --db_password PASSWORD -c /etc/odoo/odoo.conf -u all --stop-after-init

## KeyError: 'ir.http'

El problema ocurre cuando hay un error al establecer la conexión a la base de datos.

Si tiene muchas bases de datos en la administración de Postgresql, debe especificar a cuál desea conectarse.

en el archivo de configuración agregar

db_name = DB_NAME_THAT_YOU_WANT_TO_CONNECT

después de eso deberías ejecutar la base ./odoo-bin -i



