from flask import (
    Blueprint, flash, render_template, request, send_file
)
from io import BytesIO
import qrcode
from adfree.forms import QRCodeForm

bp = Blueprint('qrcodes', __name__, url_prefix='/qr-codes')


@bp.route("/", methods=['GET', 'POST'])
def index():
    form = QRCodeForm()

    if form.validate_on_submit():
        content = form.content.data

        # generate qr code
        img = qrcode.make(content)
        # save to image and serve as attachement
        img_io = BytesIO()
        img.save(img_io, 'png')
        img_io.seek(0)
        return send_file(img_io,
                         attachment_filename="qrcode.png",
                         as_attachment=True)

    return render_template('qr-codes/index.html', form=form)
