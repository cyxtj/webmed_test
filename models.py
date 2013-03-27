#coding=utf-8
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:levis822@localhost:3306/duobiao'
db = SQLAlchemy(app)


class drug(db.Model):
    DRUGid = db.Column(db.String(36), nullable=False, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    unit = db.Column(db.String(10), nullable=False)
    alias = db.Column(db.String(100), nullable=False, default=' ')
    py = db.Column(db.String(20), nullable=False, default=' ')
    wb = db.Column(db.String(20), nullable=False, default=' ')
    isClassical = db.Column(db.Boolean, nullable=False, default=1) #comment '1:是标准的;0:非标准的'
    SPETid = db.Column(db.String(36), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    state = db.Column(db.Boolean, nullable=False, default=0) #comment '0:正常;1:锁定'

    @classmethod
    def get_all(self, data):
        tempList = []
        for (i, temp) in enumerate(data['objects']):
            tempList.append({})
            tempList[i]['DRUGid'] = temp['DRUGid']
            tempList[i]['name'] = temp['name']
        data['objects'] = tempList
        return data

class fixedrecipe(db.Model):
    FREPid = db.Column(db.String(36), nullable=False, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    effect = db.Column(db.String(200), nullable=False, default=' ')
    py = db.Column(db.String(20), nullable=False, default=' ')
    wb = db.Column(db.String(20), nullable=False, default=' ')
    isClassical = db.Column(db.Boolean, nullable=False, default=1) #comment '1:是标准的;0:非标准的'
    SPETid = db.Column(db.String(36), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    state = db.Column(db.Boolean, nullable=False, default=0) #comment '0:正常;1:锁定'

    @classmethod
    def get_all(self, data):
        tempList = []
        for (i, temp) in enumerate(data['objects']):
            tempList.append({})
            tempList[i]["FREPid"] = temp['FREPid']
            tempList[i]["name"] = temp['name']
        data['object'] = tempList
        return data


class fixedrecipeItem(db.Model):
    FRITid = db.Column(db.String(36), nullable=False, primary_key=True)
    DRUGid = db.Column(db.String(36),db.ForeignKey('drug.DRUGid'))
    FREPid = db.Column(db.String(36),db.ForeignKey('fixedrecipe.FREPid'))
    quality = db.Column(db.DECIMAL(18,4), nullable=False, default=0)
    sequence = db.Column(db.INTEGER, nullable=False, default=0)
    illustration = db.Column(db.Text, nullable=False, default=' ')
    
    drug = db.relationship('drug', backref=db.backref('fixedrecipeItems', cascade='all, delete-orphan'))
    fixedrecipe = db.relationship('fixedrecipe', backref=db.backref('fixedrecipeItems', cascade='all, delete-orphan'))
    #primary key (FRITid)

    @classmethod
    def get_all(self, data):
        tempList = []
        for (i, temp) in enumerate(data['objects']):
            tempList.append({})
            tempList[i]["FRITid"] = temp['FRITid']
            tempList[i]["FREPid"] = temp['FREPid']
            tempList[i]["DRUGid"] = temp['DRUGid']
        data['objects'] = tempList
        return data
