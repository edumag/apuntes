#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## @file import_prodcts.py
## @brief Importación de productos a prestashop.

__version__ = '0.1.0'
__author__ = u'edu@lesolivex.com'

# 0: MARCA
# 1: CODIGO
# 2: REFERENCIA
# 3: SKU
# 4: EAN
# 5: MODELO
# 6: CODIGO COLOR
# 7: COLOR
# 8: TALLA
# 9: TALLA EU
# 10: CATEGORIA
# 11: NOMBRE
# 12: DETALLES
# 13: MATERIAL
# 14: FIT
# 15: CUIDADOS
# 16: FABRICADO
# 17: DISEÑADO
# 18: COLECCIÓN
# 19: CONTENEDOR
# 20:  PVP
# 21: STOCK INICIAL

from glob import glob
import csv


id_inicial = 1
prefix_url_img = "https://www.thetimeofbocha.com/upload/"
lista_productos = []
lista_combinaciones = []

def write_csv(type):
    with open(type + '.csv', 'w', newline='', encoding='utf-8') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',
            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        if type == 'productos':
            for row in lista_productos:
                spamwriter.writerow(row)
        else:
            for row in lista_combinaciones:
                spamwriter.writerow(row)

with open('in.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')

    codigo = False

    head_products = ['Product ID',
        'Active (0/1)', 'Name *', 'Categories (x,y,z...)', 'Price tax excluded',
        'Reference #', 'Supplier reference #', 'Supplier', 'Manufacturer', 'EAN13',
        'Quantity', 'Summary', 'Description', 'Tags (x,y,z...)',
        'Image URLs (x,y,z...)', 'Feature(Name:Value:Position)',
        'Acessories  (x,y,z...)']

    lista_productos.append(head_products)

    head_combinaciones = [
        'Product ID*', 'Attribute (Name:Type:Position)*', 'Value (Value:Position)*',
        'EAN13', 'Quantity', 'Image URLs (x,y,z...)'
    ]

    lista_combinaciones.append(head_combinaciones)

    counter_rows = 0
    for row in spamreader:

        if counter_rows == 0:
            counter_rows = counter_rows +1
            continue

        product = []
        atributs = []
        # Es nuevo producto
        if codigo != row[1]:
            codigo = row[1]
            id_inicial = id_inicial + 1


            product.append(id_inicial)
            product.append('1')
            product.append(row[11])
            product.append(row[10])                   # Categorías.
            product.append(row[20].replace(' €',''))  # Precio.
            product.append(row[2])
            product.append(row[16])
            product.append(row[17])
            product.append(row[0])
            product.append(row[4])                    # EAN
            product.append(row[21])                   # Stock
            product.append(row[12] + ' ' + row[13])   # Summary.
            product.append(row[15])                   # Description.
            product.append('')                        # Tags

            # Imágenes en carpeta upload.
            # @todo Comprovar que existe y si es así añadimos url.

            # Posibles nombres de imágenes.
            # REFERENCIA-1.jpg
            images_str = ''
            for n in ['1','2','3','4','5','6','7','8','9']:
                img_url = row[2] + '-' + n + '.jpg'
                if glob('../upload/' + img_url):
                    images_str = images_str + prefix_url_img + img_url + ','
                img_url2 = row[2] + '-' + n + '.JPG'
                if glob('../upload/' + img_url2):
                    images_str = images_str + prefix_url_img + img_url2 + ','

            # @todo Si no obtenemos ninguna imagen, probar de encontrar una
            #       solo con la primera parte de la referencia.

            if images_str.endswith(','):
                images_str = images_str[:-1]
            product.append(images_str)         # Images.

            # Caracteristicas.
            # Feature(Name:Value:Position)
            #
            # 1	 Composition
            # 2	 Características
            # 3	 Consejos de lavado
            # 4	 color
            # 5	 Composición
            # 6  Instrucciones de lavado
            # 7	 FIt
            # 8	 Made in
            # 9	 Genero
            # 10 Medidas
            # 11 Detalles
            # 12 Diseñado
            # 13 Fabricado
            # 14 Ajustable
            # 15 ID
            # 16 Tipo

            F = 'FIt:' + row[14] + ':0'
            F = F + ',Consejos de lavado:' + row[15].replace(',',' ') + ':1'
            F = F + ',color:' + row[7].replace(',',' ') + ':2'
            F = F + ',Made in:' + row[16].replace(',',' ') + ':3'
            F = F + ',Detalles:' + row[12].replace(',',' ') + ':4'
            F = F + ',Diseñado:' + row[17].replace(',',' ') + ':5'
            F = F + ',Fabricado:' + row[16].replace(',',' ') + ':6'
            F = F + ',Composición:' + row[13].replace(',',' ') + ':7'

            product.append(F)                         # Features.

            product.append('')                        # Acessories.

            lista_productos.append(product)
            product = []

        # Combinación.

        # Atributos.
        # 1	Tamaño
        # 2 Color
        # 3	Dimension
        # 4	Paper Type
        # 5	Tallas

        atributs.append(id_inicial)

        # Atributes
        color_atribute = 'color:color:0'
        tallas_atribute = ', Tallas:radio:1'
        color_values = row[6] + ':0'
        tallas_values = ', ' + row[8] + ':1'

        atributs.append(color_atribute + tallas_atribute)         # Atributes.
        atributs.append(color_values + tallas_values)             # Atributes values.

        atributs.append(row[4])
        atributs.append(row[21])


        # Posibles nombres de imágenes.
        # REFERENCIA-1.jpg
        images_str = ''
        for n in ['1','2','3','4','5','6','7','8','9']:
            img_url = row[2] + '-' + n + '.jpg'
            if glob('../upload/' + img_url):
                images_str = images_str + prefix_url_img + img_url + ','
            img_url2 = row[2] + '-' + n + '.JPG'
            if glob('../upload/' + img_url2):
                images_str = images_str + prefix_url_img + img_url2 + ','
        if images_str.endswith(','):
            images_str = images_str[:-1]

        atributs.append(images_str)         # Images.

        lista_combinaciones.append(atributs)



    # for r in lista_productos:
    #     print(r)

    write_csv('productos')
    write_csv('combinaciones')



