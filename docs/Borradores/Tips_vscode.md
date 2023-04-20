# Trucos para Visual Studio Code

## Atajos de teclado

Ctrl + u:               Convertir a Mayúsculas / Minúsculas.
Ctrl + k + c:           Comentar bloque.
Ctrl + k + u:           Descimentar. 
Alt + Arriba/Abajo:     Mover linea o bloque.
Ctrl + k + f:           Formatear bloque.
Shift + Alt + Flechas:  Cursor en bloque.
Ctrl + k + x:           Snipers.
Ctrl + Shift + v:       Pegado cíclico.
Ctrl + c:               Copia linea actual.
Ctrl + r + Ctrl + e:    Encapsula.
Ctrl + /                Comenta bloque.

## Extensión "Todo tree"

Nos permite mostrar un arbol con todos las etiquetas que le especifiquemos.

En mi caso me gusta utilizar @todo y @bug en el código.

Una vez instalada modifico la configuración para que recoja mis etiquetas y
modifico la expresión regular que permite encontrarlas.

::

    ((//|#|<!--|;|/\*^| \*)\s*($TAGS)|^\s*- \[ \])


