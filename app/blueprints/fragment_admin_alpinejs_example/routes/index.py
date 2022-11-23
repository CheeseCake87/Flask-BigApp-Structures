from flask import render_template

from .. import bp, page_needs


@bp.route("/", methods=["GET"])
def index():
    return render_template(bp.tmpl("index.html"), **page_needs)
