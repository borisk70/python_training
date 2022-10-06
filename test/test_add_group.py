# -*- coding: utf-8 -*-

from model.group import Group
##import pytest
##from data.groups import constant as testdata
#from data.add_group import testdata
#import random
#import string



#from fixture.application import Application
#@pytest.fixture()
 #  def app(request):
  #    fixture = Application()
   #   request.addfinalizer(fixture.destroy)
   #   return fixture

#def random_string(prefix, maxlen):
       #symbols = string.ascii_letters + string.digits + " "*10
        #return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


#testdata = [Group(name="", header="", footer="")] + [
 #       Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
  #      for i in range(5)
#]

#@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])

#def test_add_group(app, json_groups):
def test_add_group(app, db, json_groups):
        group = json_groups
        app.session.login(username="admin", password="secret")
        #old_groups=app.group.get_group_list()
        old_groups = db.get_group_list()
        app.group.create(group)
        #assert len(old_groups) + 1 == app.group.count()
        #new_groups = app.group.get_group_list()
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        app.session.logout()


