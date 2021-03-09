from adfree.forms import QRCodeForm
from flask import Blueprint, render_template, send_file
from io import BytesIO
from qrcode import make as generateQRCode

bp = Blueprint('qrcodes', __name__, url_prefix='/qr-codes')


@bp.route("/", methods=['GET', 'POST'])
def index():
    form = QRCodeForm()

    if form.validate_on_submit():
        content = form.content.data

        # generate qr code
        img = generateQRCode(content)
        # save to image and serve as attachement
        img_io = BytesIO()
        img.save(img_io, 'png')
        img_io.seek(0)
        return send_file(img_io,
                         attachment_filename="qrcode.png",
                         as_attachment=True)

    return render_template('qr-codes/index.html', form=form)
