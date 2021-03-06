from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
import os
from adfree.forms import YTForm
from youtube_dl import YoutubeDL
from pathlib import Path

bp = Blueprint('youtubedl', __name__,
               url_prefix='/youtube-dl',
               static_folder="downloads")


@bp.route("/", methods=['GET', 'POST'])
def index():
    form = YTForm()
    file = None

    try:
        p = Path(bp.root_path) / "downloads"
        os.makedirs(p)
    except OSError:
        pass

    if form.validate_on_submit():
        options = {
            'format': 'best[ext=mp4]/best',
            'noplaylist': True,
            'outtmpl': str(p) + "/%(title)s-%(id)s.%(ext)s",
        }

        with YoutubeDL(options) as yt:
            try:
                meta = yt.extract_info(form.link.data, download=True)
                title = meta["title"].replace("/", "_")
                file = "%s-%s.%s" % (title, meta["id"], meta["ext"])
            except:
                flash("Something went wrong downloading the file.")

    return render_template('youtube-dl/index.html', form=form, file=file)
