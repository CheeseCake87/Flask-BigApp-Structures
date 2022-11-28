from time import sleep

from flask import render_template

from .. import bp


@bp.route("/other", methods=["GET"])
def other():
    sleep(2)
    return render_template(bp.tmpl("other.html"))
