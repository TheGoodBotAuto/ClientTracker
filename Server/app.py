from flask import Flask, jsonify
from flask_cors import CORS
import os
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()


def createApp():
  # instantiate the app
  app = Flask(__name__)
  app.config.from_object(os.environ['APP_SETTINGS'])
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  # enable CORS
  CORS(app, resources={r'/*': {'origins': '*'}})
  db.init_app(app)
  return app