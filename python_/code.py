
#def wraper(f):
#    'print wrapper...start'
#    f()
#    'print wrapper...end'

#def second():
#    a = A()
#    a.fun()
#    print 'second.....'


#'before call second.......'
#second()
#'after call second.......'
#class A():
#    def fun(self):
#        first()
#        print 'A.....fun'


#@wraper
#def first():
#    print 'first...'


#a= A()
#a.fun()
#second()

def wraper(f):
    import ipdb; ipdb.set_trace() ### XXX BREAKPOINT
    'print wrapper...start'
    f()
    'print wrapper...end'

#@wraper
def fun():
    import ipdb; ipdb.set_trace() ### XXX BREAKPOINT
    print 'fun called'
    return 2

class A():
    def func(self):
        print 'AAAAAAAAAAAA..........func'
#fun()
#qq=A()
#qq.func()


class Q():
    def fun(self):
        print 'QQQQQQQQ.....fun'
    def fuck(self):
        raise NotImplementedError()

q = Q()
q.fuck()

