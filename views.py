#coding=utf8
import flask.ext.restless
from models import *

manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)


manager.create_api(drug, methods=['GET','POST','DELETE'], postprocessors=dict(GET_MANY= [drug.get_all]))
manager.create_api(fixedrecipeItem, methods=['GET','POST','DELETE'], postprocessors=dict(GET_MANY= [fixedrecipeItem.get_all]))
manager.create_api(fixedrecipe, methods=['GET','POST','DELETE'], postprocessors=dict(GET_MANY= [fixedrecipe.get_all]))

if __name__ == '__main__':
    app.run()
