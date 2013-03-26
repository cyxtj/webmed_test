#coding=utf8
from flask import Flask
import flask.ext.restless

app = Flask(__name__)

from models import *
manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

#preprocessor = {'GET_MANY':[drug.get_all]}

manager.create_api(drug, methods=['GET','POST','DELETE'])
manager.create_api(fixedrecipeItem, methods=['GET','POST','DELETE'])
manager.create_api(fixedrecipe, methods=['GET','POST','DELETE'])

