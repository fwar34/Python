# https://zhuanlan.zhihu.com/p/59621713
def example(name):
    print('example start')
    while True:
        x = yield name
        if x is None:
            return 'AAAA None'
        print('recv {} from send'.format(x))

c = example('test')
print('-----------')
print('next return value:', next(c)) # next 启动 c，返回第一次 yield 的值
print('send return value:', c.send(6))
if __name__ == '__main__':
    try:
        c.send(None)
    except StopIteration as e:
        print('return value:', e.value)
