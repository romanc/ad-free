import os

from flask import Flask, render_template


def create_app(test_config=None):
    # create and configure qr-codes app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev',
                            RECAPTCHA_PARAMETERS={"hl": "en"})

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page to say hello :)
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/legal')
    def legal():
        return render_template('legal.html')

    from adfree.qrcodes import qrcodes
    app.register_blueprint(qrcodes.bp)
    app.add_url_rule("/qr-codes", endpoint="index")

    from adfree.pdfmerge import pdfmerge
    app.register_blueprint(pdfmerge.bp)
    app.add_url_rule("/pdf-merge", endpoint="index")

    from adfree.youtubedl import youtubedl
    app.register_blueprint(youtubedl.bp)
    app.add_url_rule("/youtube-dl", endpoint="index")

    return app
