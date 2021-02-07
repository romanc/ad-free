from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('youtubedl', __name__, url_prefix='/youtube-dl')


@bp.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        link = request.form['link']
        error = 'Link is required.' if not link else None

        if error is None:
            # todo - do something here
            print("Link: %s" % link)
        else:
            flash(error)

    return render_template('youtube-dl/index.html')
