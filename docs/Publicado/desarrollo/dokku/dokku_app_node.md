# Dokku con node

Configurar la app en puerto 5000.

## Creamos app.

```
dokku apps:create mementomori
dokku buildpacks:add mementomori https://github.com/heroku/heroku-buildpack-nodejs.git
dokku domains:add mementomori.lesolivex.com
dokku domains:add mementomori mementomori.lesolivex.com
dokku builder-dockerfile:report
dokku builder-dockerfile:report node-js-app
```

## Añadimos buildpack nodejs.

```
dokku config:show mementomori
dokku buildpacks:clear mementomori
dokku buildpacks:set mementomori heroku/nodejs
```

## letsencrypt

```
dokku config:set --no-restart mementomori DOKKU_LETSENCRYPT_EMAIL=edu@lesolivex.com
dokku letsencrypt mementomori
dokku letsencrypt:auto-renew
```

