from flask import Flask
from flask_bigapp import BigApp
from flask_sqlalchemy import SQLAlchemy

bigapp = BigApp()
db = SQLAlchemy()


def create_app():
    main = Flask(__name__)
    bigapp.init_app(main)
    db.init_app(main)
    bigapp.import_structures("structures")
    bigapp.import_models(folder="models")
    bigapp.import_builtins("flask/routes")
    bigapp.import_builtins("flask/template_filters")
    bigapp.import_blueprints("blueprints")
    print(main.config['APP_NAME'], ", <- this value was pulled from main.config['APP_NAME']")
    print("Which was set in the .env file. It was then tagged in the env.config.toml file.")
    print("Navigate to app/__init__.py file to find this print statement.")
    return main
