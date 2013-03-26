#coding=utf-8
#note : api/fixedrecipeItem is wrong
#       api/fixedrecipe_item is right

import unittest
import json
from views import app
from models import *

class TestFixedrecipeItem(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        db.drop_all()
        db.create_all()
        self.client = app.test_client()

    def tearDown(self):
        pass
#        db.drop_all()

    def test_fixedrecipe_data_number(self):
        r = self.client.get('/api/fixedrecipe')
        self.assertEqual(json.loads(r.data)['num_results'], 0)

    def test_fixedrecipe_add(self):
        fixedrecipe = {"FREPid":"45e053e0-d0a5-43ac-b325-25b28aba97bb","code":"386","name":"九味羌活汤","effect":"","py":"JWQHT","wb":"VKUII","isClassical":1,"SPETid":"","illustration":"","createDay":"1990-1-1","optrid":"c6543358-354b-4986-a06f-bd61b0cde15d","state":"3"}
        r = self.client.post('/api/fixedrecipe', data='fixedrecipe')
        print r.__dict__
        r = self.client.get('/api/fixedrecipe')
        self.assertEqual(json.loads(r.data)['num_results'], 1)
       
    def test_drug_data_number(self):
        r = self.client.get('/api/drug')
        self.assertEqual(json.loads(r.data)['num_results'], 0)

    def test_fixedrecipeItem_data_number(self):
        r = self.client.get('/api/fixedrecipe_item')
        self.assertEqual(json.loads(r.data)['num_results'], 0)

if __name__ == '__main__':
    unittest.main()
