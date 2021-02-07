from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('youtubedl', __name__, url_prefix='/youtube-dl')


@bp.route("/")
def index():
    return render_template('youtube-dl/index.html')
