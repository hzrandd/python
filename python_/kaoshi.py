import copy
import types

class B(object):
    def __init__(self, name):
        self.name = name


class A(object):
    def __init__(self):
        self.apps = {}

    def create_app(self, name):
        app = B(name)
        if name not in self.apps:
            self.apps[name] = app
        return app

a = A()

b1 = a.create_app("111")
b2 = a.create_app("222")
b3 = a.create_app("333")


B.get_name = lambda x: x.name

for name, app in a.apps.items():
    new_name = types.MethodType(lambda x: x.name, app, app.__class__)
    app.get_name2 = new_name


print(b1.get_name())
print(b2.get_name())
print(b3.get_name())

print(b1.get_name2())
print(b2.get_name2())
print(b3.get_name2())

class Foo:
      pass # dummy class

x = Foo()
Foo.bar = lambda self: 42

print x.bar()

from pipe import *

@Pipe
def should_equal(obj, val):
    if obj==val: return True
    return False

class dummy: pass
item=dummy()
item.value=19.99

print item.value | should_equal(19.99)
