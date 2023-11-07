Si necesitamos realizar un test con la misma base de datos que utilizamos en la app.

Comentar las lineas en en phpunit.xml

    <server name="DB_CONNECTION" value="test"/>
    <server name="DB_DATABASE" value="test"/>


Comentar las lineas en tests/TestCase.php

    use Illuminate\Foundation\Testing\DatabaseMigrations;
    use Illuminate\Support\Facades\Artisan;

Dentro de la clase TestCase

    use CreatesApplication, DatabaseMigrations;


    public function setUp(): void

    {
        parent::setUp();
        Artisan::call('db:seed --class=CreateContentTest');
    }

