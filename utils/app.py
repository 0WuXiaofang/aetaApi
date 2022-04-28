from flask import Flask
def register_blueprint(app):
    from api.v1 import create_blueprint_aFang
    app.register_blueprint(create_blueprint_aFang(), url_prefix='/api/v1')


def create_app():
    app = Flask(__name__)
    # app.config.from_object('config.setting')
    register_blueprint(app)
    return app

