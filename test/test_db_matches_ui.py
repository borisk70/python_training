
from model.group import Group
from timeit import timeit


def test_group_list(app, db):
    app.session.login(username="admin", password="secret")
    #ui_list = app.group.get_group_list()
    print(timeit(lambda:app.group.get_group_list(), number=1))
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    #db_list = map(clean, db.get_group_list())
    print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
    assert False
    #assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
    app.session.logout()
