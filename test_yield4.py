# yield from
def g1():
    yield range(5)  #yield就是将range这个可迭代对象直接返回了。

def g2():
    yield from range(5) #而yield from解析了range对象，将其中每一个item返回了。yield from iterable本质上等于for item in iterable: yield item的缩写版 

it1 = g1()
it2 = g2()

for x in it1:
    print(x)

for x in it2:
    print(x)
