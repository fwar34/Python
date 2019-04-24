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
