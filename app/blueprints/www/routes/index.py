from flask import render_template

from .. import bp

structures = [("default_theme", "default_theme_example.index")]


@bp.route("/", methods=["GET"])
def index():
    render = bp.tmpl("index.html")
    return render_template(render, structures=structures)
