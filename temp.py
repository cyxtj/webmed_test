#coding=utf-8
from models import *


newdrug = drug(DRUGid='e28b7d9c-e817-47c1-b227-97d8eca021a7', code='2062', name='杏仁', unit='克', alias=' ', py='xr', wb='sw', isClassical='1', SPETid=' ', illustration='', createDay='2008-03-25 01=42=59.000', optrid='c6543358-354b-4986-a06f-bd61b0cde15d', state='3')
db.session.add(newdrug)

new_fixedrecipe = fixedrecipe(FREPid='65dd5753-aad0-4261-94d3-09a67bd4f9a1', code='378', name='华盖散', effect='', py='HGS', wb='WUA', isClassical='1', SPETid=' ', illustration='', createDay='2008-03-25 02:05:10.000', optrid='c6543358-354b-4986-a06f-bd61b0cde15d', state='3')
db.session.add(new_fixedrecipe)
db.session.commit()

new_fixedrecipeItem = fixedrecipeItem(FRITid='9c18a29f-faa1-494d-839c-7a89cba439e8', DRUGid='e28b7d9c-e817-47c1-b227-97d8eca021a7', FREPid='65dd5753-aad0-4261-94d3-09a67bd4f9a1', quality='9.0000', sequence='0', illustration='')
db.session.add(new_fixedrecipeItem)
db.session.commit()
