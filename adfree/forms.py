from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired


class QRCodeForm(FlaskForm):
    content = TextAreaField(
        label="Contents *",
        validators=[DataRequired()],
        default="Enter QR code contents",
        render_kw={"rows": 1,
                   "style": "overflow: hidden; resize: none; height: 59px;"})
    recaptcha = RecaptchaField(label="Please confirm you are human *")
    submit = SubmitField(label="Generate QR Code",
                         render_kw={"class": "primary"})


class YTForm(FlaskForm):
    link = StringField(label="Link *",
                       validators=[DataRequired()],
                       default="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    recaptcha = RecaptchaField(label="Please confirm you are human *")
    submit = SubmitField(label="Fetch video",
                         render_kw={"class": "primary"})
