# https://blog.csdn.net/soonfly/article/details/78361819

# yield/send
def gen():
    print("enter gen")
    value = 0
    while True:
        recv = yield value
        if recv == 'e':
            break
        value = 'got %s' % recv


g = gen()  # 这里并没有启动 gen 生成器
print(g.send(None)) # 这行启动了生成器(并且启动的时候只能传递None,传递其他值会报错)
print(g.send('Hello'))
print(g.send(11111))
print(g.send('e'))

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
