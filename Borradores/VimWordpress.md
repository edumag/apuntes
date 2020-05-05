"=========== Meta ============
"StrID : 1267
"Title : Vim Wordpress MarkDown
"Slug  : vim-wordpress-markdown
"Cats  : MarkDown, Vim, Wordpress
"Tags  : 
"=============================
"EditType   : post
"EditFormat : HTML
"BlogAddr   : https://lesolivex.com
"========== Content ==========



## Instalar

[VimWordpress](https://github.com/MrPeterLee/VimWordpress)

En mi caso lo instalo con VundleVim desde .vimrc:

    " VimWordperss
    Plugin 'mrpeterlee/VimWordpress'


Algunos ejemplos:

- :BlogList - Lista las 30 entradas más recientes.
- :BlogList page - Lista las 30 páginas más recientes.
- :BlogList post 100 - Lista las 100 entradas más recientes.
- :BlogNew post - Nueva entrada. :BlogNew page - Nueva página.
- :BlogSave - Graba. Aunque la documentación dice que por defecto graba como publicado, en mi caso graba como borrador.
- :BlogSave draft - Graba como borrador.
- :BlogPreview local - Previa local de la entrada o página.
- :BlogPreview publish - como ‘
- :BlogSave publish’ con navegador abierto.

Distintas formas de abrir una entrada existente:

- :BlogOpen 679
- :BlogOpen http://your-first-blog.com/archives/679
- :BlogOpen http://your-second-blog.com/?p=679
- :BlogOpen http://your-third-blog.com/with-your-custom-permalink



## Referencias

- https://www.cyberhades.com/2012/05/11/vim-markdown-y-wordpress/



