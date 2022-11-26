from flask import render_template

from mmforms.standard_elements import Form
from mmforms.bootstrap_elements import Input

from .. import bp, page_needs


@bp.route("/login", methods=["GET"])
def login():
    login_form = Form("login_form").add_inputs(
        Input("username").t_text(),
        Input("password").t_password()
    )

    return render_template(bp.tmpl("login.html"), **page_needs, login_form=login_form.compile())
