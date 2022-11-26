from flask import render_template

from mmforms import Form, InputGroup, Input

from .. import bp, page_needs


@bp.route("/login", methods=["GET"])
def login():
    login_form = Form("login").add_inputs(
        Input("username").t_text().class_("form-control"),
        Input("password").t_password().class_("form-control"),
    )

    return render_template(bp.tmpl("login.html"), **page_needs, login_form=login_form.markup())
