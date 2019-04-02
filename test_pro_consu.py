def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[Consumer] Consuming %s ...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[Producer] Producing %s ...' % n)
        r = c.send(n)
        print('[Producer] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
