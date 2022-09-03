# -*- coding: utf-8 -*-

from model.group import Group
#from sys import maxsize


#import pytest
#from fixture.application import Application

#@pytest.fixture()
#def app(request):
 #    fixture = Application()
  #   request.addfinalizer(fixture.destroy)
   #  return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    old_groups=app.group.get_group_list()
    group=Group(name="testgroup", header="group", footer="group")
    app.group.create(group)
    #assert len(old_groups) + 1 == len(new_groups)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    app.session.logout()

#def test_add_empty_group(app):
 #   app.session.login(username="admin", password="secret")
  #  old_groups = app.group.get_group_list()
   # group = Group(name="", header="", footer="")
    #app.group.create(group)
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) + 1 == len(new_groups)
    #old_groups.append(group)
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    #app.session.logout()

