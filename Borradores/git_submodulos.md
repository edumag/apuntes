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

```
git submodules update
```

## 2. Añadimos desde cero.

Ejemplo:

```
git submodule add git@gitlab.com:edumag/lesolivex-wt.git wp-content/themes/lesolivex
```

