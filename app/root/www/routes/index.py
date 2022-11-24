from flask import render_template

from app import listed_structures
from .. import bp


@bp.route("/", methods=["GET"])
def index():
    render = bp.tmpl("index.html")
    return render_template(render, structures=listed_structures)
