from flask import render_template

from .. import bp, page_needs


@bp.route("/login", methods=["GET"])
def login():
    return render_template(bp.tmpl("login.html"), **page_needs)
