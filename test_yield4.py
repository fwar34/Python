# https://blog.csdn.net/soonfly/article/details/78361819
# 生成器一定是迭代器iterator，迭代器一定是可迭代对象iterabl
# yield from
# yield from iterable本质上等于for item in iterable: yield item的缩写版 
def g1():
    yield range(5)  #yield就是将range这个可迭代对象直接返回了。

def g2():
    yield from range(5) #而yield from解析了range对象，将其中每一个item返回了。yield from iterable本质上等于for item in iterable: yield item的缩写版 

it1 = g1()
it2 = g2()

for x in it1:
    print(x)

print('---------------')

for x in it2:
    print(x)

# 再强调一遍：yield from后面必须跟iterable对象(可以是生成器，迭代器)
