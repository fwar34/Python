# https://blog.csdn.net/soonfly/article/details/78361819
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

# 假设要在fab()的基础上实现一个函数，调用起始都要记录日志
def wrapper(fun_iterable):
    print('start')
    for item in fun_iterable:
        yield item
    print('end')

wrap = wrapper(fab(5))
for i in wrap:
    print(i, end = ' ')

# 现在使用yield from代替for循环
def wrapper2(fun_iterable):
    print('start')
    yield from fun_iterable #注意此处必须是一个可生成对象
    print('end')

wrap2 = wrapper2(fab(5))
for i in wrap2:
    print(i, end = ' ')
