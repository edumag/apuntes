Automatizar la publicación de los apuntes generados en markdown con github.

Se da por entendido que ya tienes mkdocs con tu documentos.

Para ver como hacerlo: https://www.mkdocs.org/

```
virtualenv autodocs
source autodocs/bin/activate
```

Generarar fichero requirements.txt

```
Babel==2.8.0
click==7.1.1
future==0.18.2
gitdb==4.0.4
GitPython==3.1.1
htmlmin==0.1.12
Jinja2==2.11.2
joblib==0.14.1
jsmin==2.2.2
livereload==2.6.1
lunr==0.5.6
Markdown==3.2.1
MarkupSafe==1.1.1
mkdocs==1.1
mkdocs-awesome-pages-plugin==2.2.1
mkdocs-git-revision-date-localized-plugin==0.5.0
mkdocs-material==5.1.1
mkdocs-material-extensions==1.0b1
mkdocs-minify-plugin==0.3.0
nltk==3.5
Pygments==2.6.1
pymdown-extensions==7.0
pytz==2019.3
PyYAML==5.3.1
regex==2020.4.4
six==1.14.0
smmap==3.0.2
tornado==6.0.4
tqdm==4.45.0
```

Fichero .gitignore

```
autodocs/
requirements.txt
site
```

```
git commit -am 'Init mkdocs with github'
```

```
mkdocs gh-deploy
```

Salida del comando:

```
INFO     -  Cleaning site directory
INFO     -  Building documentation to directory: /home/edumag/desarrollo/apuntes/site
INFO     -  Documentation built in 0.69 seconds
INFO     -  Copying '/home/edumag/desarrollo/apuntes/site' to 'gh-pages' branch and pushing to GitHub.
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 312 bytes | 312.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:edumag/apuntes.git
   e027fa4..484035f  gh-pages -> gh-pages
   INFO     -  Your documentation should shortly be available at: https://edumag.github.io/apuntes/
```
