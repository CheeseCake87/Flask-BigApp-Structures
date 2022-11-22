![](https://github.com/CheeseCake87/Flask-BigApp-Structures/blob/master/app/blueprints/www/static/Flask-BigApp-SVG.svg)  

# Flask-BigApp Structures (themes)
### This is a collection of structures for Flask-BigApp
It includes pre-setup configs and a server module that can handle docker-compose deployments.

Configuration files to check over:
```text
# This config file is standard config file.
/app/default.config.toml

# This config file is tagged to have the env variables injected.
/app/env.config.toml

NOTE: The env.config.toml need set like: 

bigapp.init_app(main, "env.config.toml") 

Env config may not work when using Flask run.
```

### Flask

#### Start Flask
```
flask run
```

# Contribute a structure
If you want to contribute to this project, please read the [CONTRIBUTING.md](CONTRIBUTING.md) file.