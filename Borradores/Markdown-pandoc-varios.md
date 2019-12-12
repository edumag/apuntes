# Trucos de pandoc para exportar markdown

## Espacios en blanco.

```
$~$
$~$
$~$
```

## No poner numero de pagina en el pdf.

Podemos añadir en la cabecera del documentos la siguiente instrucción.

```
\pagenumbering{gobble}
```

## Margenes de las paginas.

Añadir la opción al exportar, ejemplo:

```
pandoc  -V geometry:margin=1in -o Escriptori/ejemplo.pdf ejemplo.md
```
