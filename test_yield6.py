# https://blog.csdn.net/soonfly/article/details/78361819
# asyncio.coroutine 和 yield from

import asyncio
import random

@asyncio.coroutine
def smart_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = random.uniform(0, 0.2)
        yield from asyncio.sleep(sleep_secs)
        print('Smart one think {} secs to get {}' . format(sleep_secs, b))
        a, b = b, a + b
        index += 1

@asyncio.coroutine
def stupid_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = random.uniform(0, 0.4)
        yield from asyncio.sleep(sleep_secs)
        print('Stupid one think {} secs to get {}' . format(sleep_secs, b))
        a, b = b, a + b
        index += 1

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [smart_fib(10), stupid_fib(10)]
    loop.run_until_complete(asyncio.wait(tasks))
    print('All fib finished.')
    loop.close()
        

# yield from asyncio.sleep(sleep_secs) 这里不能用time.sleep(1)因为time.sleep()返回的是None，它不是iterable，
# 还记得前面说的yield from后面必须跟iterable对象(可以是生成器，迭代器)。
# 所以会报错：
#    yield from time.sleep(sleep_secs)
#    TypeError: ‘NoneType’ object is not iterable
