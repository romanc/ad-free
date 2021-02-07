from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('qrcodes', __name__, url_prefix='/qr-codes')


@bp.route("/")
def index():
    return render_template('qr-codes/index.html')
