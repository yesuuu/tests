# class Borg(object):
#
#     stateDict = {}
#
#     def __init__(self):
#         if not self.stateDict:
#             print 'init!'
#             self.bingbing = 2
#             self.stateDict = self.__dict__
#         else:
#             print 'copy...'
#             self.__dict__ = self.stateDict
#
# a = Borg()
# print a.stateDict
# print Borg.stateDict
# b = Borg()
#
# print id(a)
# print id(b)
# print a.bingbing
# print b.bingbing
# a.bingbing = 1
# print a.bingbing
# print b.bingbing

def singleton(cls):
    instances = {}
    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

@singleton
class MyClass4(object):
    def __init__(self, x=0):
        self.x = x

@singleton
class MyClass4(object):
    a = 1
    def __init__(self, x=0):
        self.x = x

one = MyClass4()
two = MyClass4(x = 1)

two.a = 3
print one.a
#3
print id(one)
#29660784
print id(two)
#29660784
print one == two
#True
print one is two
#True
one.x = 12
print one.x
#1
print two.x
#1
