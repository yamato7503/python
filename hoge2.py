class Hoge(object):
    pass

def initialize(obj, a, b):
    obj.a = a
    obj.b = b

hoge = Hoge()
initialize(hoge, 10, 'hoge')
print (hoge.a)
print (hoge.b)
