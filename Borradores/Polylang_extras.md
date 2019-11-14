# Polylang Extras

## SQL que recoge todas las entradas que tienen definido un idioma pero no el otro.

```
SELECT  wp_posts.ID FROM wp_posts  LEFT JOIN wp_term_relationships ON (wp_posts.ID = wp_term_relationships.object_id) WHERE 1=1  AND (
    wp_term_relationships.term_taxonomy_id IN (2)
) AND wp_posts.post_type = 'post' AND ((wp_posts.post_status = 'publish')) AND wp_posts.ID NOT IN (
    SELECT   wp_posts.ID FROM wp_posts  LEFT JOIN wp_term_relationships ON (wp_posts.ID = wp_term_relationships.object_id) WHERE 1=1  AND ( 
        wp_term_relationships.term_taxonomy_id IN (5)
    ) AND wp_posts.post_type = 'post' AND ((wp_posts.post_status = 'publish')) GROUP BY wp_posts.ID
) GROUP BY wp_posts.ID
```

## Añadimos catellano a todas las entradas que no lo tengan asignado.

```
INSERT INTO `wp_term_relationships` (`object_id`, `term_taxonomy_id`, `term_order`)

SELECT   wp_posts.ID, '5', '0' FROM wp_posts  LEFT JOIN wp_term_relationships ON (wp_posts.ID = wp_term_relationships.object_id) WHERE 1=1  AND ( 
    wp_term_relationships.term_taxonomy_id IN (2)
) AND wp_posts.post_type = 'post' AND ((wp_posts.post_status = 'publish')) AND wp_posts.ID NOT IN (
    SELECT   wp_posts.ID FROM wp_posts  LEFT JOIN wp_term_relationships ON (wp_posts.ID = wp_term_relationships.object_id) WHERE 1=1  AND ( 
        wp_term_relationships.term_taxonomy_id IN (5)
    ) AND wp_posts.post_type = 'post' AND ((wp_posts.post_status = 'publish')) GROUP BY wp_posts.ID
) GROUP BY wp_posts.ID
;
```

Esta técnica no funciona ya que polylang se lia con los idiomas.

Miramos de copiar las entradas que tenemos como ca a es.


