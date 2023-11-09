from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('mysql+pymysql://root:123456789@gbdb081123.cmdgrs377mj8.eu-west-2.rds.amazonaws.com:3306/movies'))
app.config['SECRET_KEY'] = str(os.getenv('SECRET_KEY'))

db = SQLAlchemy(app)

from application import routes
