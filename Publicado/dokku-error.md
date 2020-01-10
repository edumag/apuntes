# Error en deploy con dokku

Me he encontrado con el siguiente error al hacer el último deploy del blog.

```bash
git push dokku master
Counting objects: 1192, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (1154/1154), done.
Writing objects:  24% (287/1192)   
Writing objects: 100% (1192/1192), 3.44 MiB | 443.00 KiB/s, done.
Total 1192 (delta 864), reused 12 (delta 0)
remote: Resolving deltas: 100% (864/864), completed with 801 local objects.
-----> Cleaning up...
-----> Building lesolivex from herokuish...
-----> Adding BUILD_ENV to build environment...
-----> PHP app detected
remote: -----> Bootstrapping...
remote: 
remote:  !     ERROR: Failed to download minimal PHP for bootstrapping!
remote:  !     
remote:  !     This is most likely a temporary internal error. If the problem
remote:  !     persists, make sure that you are not running a custom or forked
remote:  !     version of the Heroku PHP buildpack which may need updating.
```
## Solución

Entramos en servidor y actualizamos herokuish.

```bash
sudo docker pull gliderlabs/herokuish:latest
```

