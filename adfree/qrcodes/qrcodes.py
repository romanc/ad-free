from flask import (
    Blueprint, flash, render_template, request, send_file
)
from io import BytesIO
import qrcode

bp = Blueprint('qrcodes', __name__, url_prefix='/qr-codes')


@bp.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        error = 'Content is required.' if not content else None

        if error is None:
            # todo - generate qr code
            # print("qr code content: %s" % content)
            img = qrcode.make(content)
            img_io = BytesIO()
            img.save(img_io, 'png')
            img_io.seek(0)
            return send_file(img_io,
                             attachment_filename="qrcode.png",
                             as_attachment=True)

        # Flash error message
        flash(error)

    return render_template('qr-codes/index.html')
