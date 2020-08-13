# Laravel many to many.

En este ejemplo vamos a relacionar productos con grupos (En mi caso llamados
rotlles), de esta manera un producto podrá ser utilizado en diferentes grupos.

Damos por hecho que los dos modelos tanto grupos como productos ya los tenemos
creados.

```bash
php artisan migrate:make create_product_rotlle
```

Tener en cuenta el orden alfabético al referir los modelos a utilizar.

Modificamos el fichero de la migración creada para añadir los indices de las
tablas relacionadas y sus claves foráneas.

```php
public function up()
{
    Schema::create('product_rotlle', function (Blueprint $table) {
        $table->id();

        $table->bigInteger('product_id')->unsigned();
        $table->bigInteger('rotlle_id')->unsigned();
        
        $table->foreign('product_id')->references('id')->on('products')
            ->onDelete('cascade')
            ->onUpdate('cascade');

        $table->foreign('rotlle_id')->references('id')->on('rotlles')
            ->onDelete('cascade')
            ->onUpdate('cascade');

        $table->timestamps();
    });
```


