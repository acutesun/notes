#yield 不但可以返回一个值, 还可以接收调用者发出的参数
def consumer():
    r = ''
    while True:
        print('before yield')
        n = yield r
        print('after yield')
        if not n:
            return 
        print('[CONSUMER] consuming %s.....' % n)
        r = '200 OK'
 
def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n+1
        print('[PRODUCER] producing %s.....' % n)
        r = c.send(n)
        print('[[RODUCER] consumer return:%s' % r)
    c.close()
c = consumer()
produce(c)
