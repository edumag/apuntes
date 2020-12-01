# Laravel (Varios)

## Migraciones.

    ddev exec php artisan migrate:reset --seed

## Añadir componentes a mano.

Si añadimos componentes a mano sin utilizar artisan es necesario ejecutar:

```
ddev composer dump-autoload
```

De esta manera será reconocido.

## Borrar cache.

```
php artisan optimize:clear
```
