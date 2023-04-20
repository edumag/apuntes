# Wordpress polylang extas

Polylang es un plugin de wordpress que nos permite tener más de un idioma en
nuestra página.

Es gratuito pero a la vez bastante limitado.

Con este truco vamos a poder copiar todo el contenido de nuestras entradas al
traducirlas haciéndonos un poco más comodo el trabajo.

Hará falta que añadáis el código en el fichero functions.php de vuestro tema.

```php
/**
 * Duplica contenido al traducir entrada.
 * Realizado por:
 * https://junaidbhura.com/make-polylang-wordpress-plugin-copy-the-content-from-the-original-post/
 */
function jb_editor_content( $content ) {
    // Polylang sets the 'from_post' parameter
    if ( isset( $_GET['from_post'] ) ) {
        $my_post = get_post( $_GET['from_post'] );
        if ( $my_post )
            return $my_post->post_content;
    }

    return $content;
}
add_filter( 'default_content', 'jb_editor_content' );

/**
 * Duplica título al traducir entrada.
 * Realizado por:
 * https://junaidbhura.com/make-polylang-wordpress-plugin-copy-the-content-from-the-original-post/
 */
function jb_editor_title( $title ) {
    // Polylang sets the 'from_post' parameter
    if ( isset( $_GET['from_post'] ) ) {
        $my_post = get_post( $_GET['from_post'] );
        if ( $my_post )
            return $my_post->post_title;
    }

    return $title;
}
add_filter( 'default_title', 'jb_editor_title' );
```