# Submodulos con git

Tenemos dos formas de añadir submodulos.

## 1. Clonando primero el subproyecto.

Ejemplo:

Nos situamos en el directorio donde queremos clonar el proyecto.

Clonamos:

```
git clone git@gitlab.com:edumag/lesolivex-wt.git lesolivex
```

Pedimos a git que inicialice los submodulos automáticamente.

```
git submodules init
```

Actualizamos submodulos.

Para actualizar un submodulo deberemos hacerlo desde su directorio con:

```
git fetch && git pull.
```

No confundirse con el comando:

```
git submodules update
```

En este caso estariamos forzando al submodulo a volver a la versión anterior
en la que lo instalamos.

## 2. Añadimos desde cero.

Ejemplo:

```
git submodule add git@gitlab.com:edumag/lesolivex-wt.git wp-content/themes/lesolivex
```

## Referencias

- https://www.git-scm.com/book/es/v2/Herramientas-de-Git-Subm%C3%B3dulos
