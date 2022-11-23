from time import sleep

from flask import render_template

from .. import bp


@bp.route("/fragment/client_card", methods=["GET"])
def client_card():
    sleep(5)
    return render_template(bp.tmpl("fragments/client_card.html"))


@bp.route("/fragment/blogs", methods=["GET"])
def blogs():
    return render_template(bp.tmpl("fragments/blogs.html"))
