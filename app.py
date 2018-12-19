#-*- coding=utf8 -*-
'''
write by xii
'''
from flask import Flask
from flask_assets import Environment,Bundle
from config import Config

app = Flask(__name__,template_folder='./template')

app.config['SECRET_KEY'] = Config.SECRET_KEY


assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('css/base.scss','css/login.scss','css/index.scss',filters='pyscss',output='scss/all.css')
assets.register('scss_all',scss)


from event import socketio
from routes import main

app.register_blueprint(main)

socketio.init_app(app)


if __name__ == "__main__":
    app.debug=True
    socketio.run(app)
