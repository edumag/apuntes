## Regenerar base de datos con las migraciones y los seeder

    artisan migrate:reset --seed

## Crear nuevo campo en una tabla

Las migraciones nos permite modificar o alterar la base de datos de forma
ordenada.

### Creamos una migración.

```
artisan make:migration insert_new_field_in_table --table=table_in_db
```

### Ejecutar la migración

```bash
ddev artisan migrate

Migrating: 2023_05_22_084649_insert_dv_rsl_in_form_campos_obligatorios
Migrated:  2023_05_22_084649_insert_dv_rsl_in_form_campos_obligatorios (7.54ms)
```

Si añadimos componentes a mano sin utilizar artisan es necesario ejecutar:

```
ddev composer dump-autoload
```

