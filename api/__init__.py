# import os
#
# from flask import Flask
# from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# CORS(app)
#
# db_url = os.getenv('DB_URL')
# app.config["SQLALCHEMY_DATABASE_URI"] = db_url
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db = SQLAlchemy(app)

db = SQLAlchemy()
