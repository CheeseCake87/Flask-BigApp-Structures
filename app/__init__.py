from flask import Flask
from flask_bigapp import BigApp
from flask_sqlalchemy import SQLAlchemy

bigapp = BigApp()
db = SQLAlchemy()

listed_structures = [
    ("default_theme", "default_theme_example.index"),
    ("fragment_alpinejs", "fragment_alpinejs_example.index"),
    ("pika", "pika_example.index")
]


def create_app():
    main = Flask(__name__)
    bigapp.init_app(main)
    db.init_app(main)
    bigapp.import_structures("structures")
    bigapp.import_models(folder="models")
    bigapp.import_builtins("flask/routes")
    bigapp.import_builtins("flask/template_filters")
    bigapp.import_blueprints("root")
    bigapp.import_blueprints("blueprints")

    @main.before_request
    def before_request():
        pass

    @main.after_request
    def after_request(response):
        return response

    return main
