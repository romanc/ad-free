from flask import Blueprint, render_template

bp = Blueprint('pdfmerge', __name__, url_prefix='/pdf-merge')


@bp.route("/")
def index():
    return render_template('pdf-merge/index.html')
