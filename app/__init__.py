import os
from flask import Flask

def create_app(tc=None):
    app = Flask(__name__, instance_relative_config=True)

    if tc is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(tc)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    @app.route('/')
    def app_route_temp():
        return 'Temporary route'

    return app
