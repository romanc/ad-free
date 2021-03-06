from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class QRCodeForm(FlaskForm):
    content = TextAreaField(validators=[DataRequired()],
                            label="Contents *",
                            default="Enter QR code contents",
                            render_kw={"rows": 1,
                                       "style": "overflow: hidden; resize: none; height: 59px;"})
    recaptcha = RecaptchaField(label="Please confirm you are human *")
    submit = SubmitField(label="Generate QR Code",
                         render_kw={"class": "primary"})
