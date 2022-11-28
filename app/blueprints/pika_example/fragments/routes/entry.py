from time import sleep
import os
from flask import render_template

from .. import bp


@bp.route("/entry", methods=["GET"])
def entry():
    sleep(2)
    os.getcwd()
    return render_template(bp.tmpl("entry.html"))
