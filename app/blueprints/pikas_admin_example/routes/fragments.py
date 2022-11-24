from flask import render_template

from .. import bp


@bp.route("/fragment/test", methods=["GET"])
def fragment_test():
    return render_template(bp.tmpl("fragments/test.html"))
