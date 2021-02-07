from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('pdfmerge', __name__, url_prefix='/pdf-merge')


@bp.route("/")
def index():
    return render_template('pdf-merge/index.html')
