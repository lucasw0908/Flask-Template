import logging
from flask import Blueprint, render_template


log = logging.getLogger(__name__)
error_handler = Blueprint("error_handler", __name__)


@error_handler.app_errorhandler(404)
def error404(err):
    return render_template("error/404.html"), 404


@error_handler.app_errorhandler(500)
def error500(err):
    log.error(err)
    return render_template("error/500.html"), 500