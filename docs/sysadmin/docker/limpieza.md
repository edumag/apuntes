## Eliminar las imágenes, los contenedores, los volúmenes y las redes sin utilizar o pendientes

docker system prune -a

## Eliminar imágenes de Docker

### Listar iágenes

docker images -a

### Eliminar

docker rmi Image Image

### Eliminar todas las imágenes

docker rmi $(docker images -a -q)

## Eliminar contenedores

### Parar

docker stop $(docker ps -a -q)

### Eliminar

docker rm $(docker ps -a -q)


## Regerencias

- https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes-es#eliminar-una-o-mas-imagenes-especificas


