from flask import current_app
from flask import render_template

structure = current_app.config.get('DEFAULT_STRUCTURE', None)


@current_app.errorhandler(400)
def system_400(error):
    if structure:
        render = f"{structure}/errors/400.html"
        return render_template(render, error=error), 400
    return error, 400


@current_app.errorhandler(401)
def system_401(error):
    if structure:
        render = f"{structure}/errors/401.html"
        return render_template(render, error=error), 401
    return error, 401


@current_app.errorhandler(403)
def system_403(error):
    if structure:
        render = f"{structure}/errors/403.html"
        return render_template(render, error=error), 403
    return error, 403


@current_app.errorhandler(404)
def system_404(error):
    if structure:
        render = f"{structure}/errors/404.html"
        return render_template(render, error=error), 404
    return error, 404


@current_app.errorhandler(405)
def system_405(error):
    if structure:
        render = f"{structure}/errors/405.html"
        return render_template(render, error=error), 405
    return error, 405


@current_app.errorhandler(500)
def system_500(error):
    if structure:
        render = f"{structure}/errors/500.html"
        return render_template(render, error=error), 500
    return error, 500
