# async和await
# 弄清楚了asyncio.coroutine和yield from之后，在Python3.5中引入的async和await就不难理解了：可以将他们理解成
# asyncio.coroutine/yield from的完美替身。当然，从Python设计的角度来说，async/await让协程表面上独立于生成器而存在，
# 将细节都隐藏于asyncio模块之下，语法更清晰明了。
# 加入新的关键字 async ，可以将任何一个普通函数变成协程

import time
import asyncio
import random

async def mygen(alist):
    while len(alist) > 0:
        c = random.randint(0, len(alist) - 1)
        print(alist.pop(c))
        await asyncio.sleep(1)

str_list = ['aa', 'bb', 'cc']
int_list = [1, 3, 5, 6]
gen1 = mygen(str_list)
gen2 = mygen(int_list)
print(gen1)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [gen1, gen2]
    loop.run_until_complete(asyncio.wait(tasks))
    print('All task finished.')
    loop.close()
