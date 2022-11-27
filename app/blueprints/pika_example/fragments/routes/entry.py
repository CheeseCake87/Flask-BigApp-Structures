from flask import render_template

from .. import bp


@bp.route("/entry", methods=["GET"])
def entry():
    print(bp.tmpl("entry.html"))
    return render_template(bp.tmpl("entry.html"))
