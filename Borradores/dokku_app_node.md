# Dokku con node

## Configurar la app en puerto 5000.





 2001  dokku apps:create mementomori
 2002  dokku buildpacks:add mementomori https://github.com/heroku/heroku-buildpack-nodejs.git
 2003  dokku domains:add mementomori.lesolivex.com
 2004  dokku domains:add mementomori mementomori.lesolivex.com
 2005  dokku builder-dockerfile:report
 2006  dokku builder-dockerfile:report node-js-app
 2007  dokku mementomori builder-dockerfile:report
 2008  dokku help
 2009  dokku apps:report mementomori
 2010  dokku builder-dockerfile:report mementomori



 2012  dokku config:show mementomori
 2013  dokku buildpacks:clear mementomori
 2014  dokku buildpacks:set mementomori heroku/nodejs



 2016  dokku config:set --no-restart mementomori DOKKU_LETSENCRYPT_EMAIL=edu@lesolivex.com
 2017  dokku letsencrypt mementomori
 2018  dokku letsencrypt:auto-renew


