#!/bin/python

class A:
    def fun(self):
        raise Exception()
    def add(self, a, b):
        print 'a+b= %d' % (a+b)
        return a + b

class B(A):
    def fun(self):
        print '-----B-----fun'

    def dec(self, a, b):
        print 'a-b= %d' % (a - b)
        return a - b

    @staticmethod
    def pprint():
        return self.dec(9,7)

import ipdb; ipdb.set_trace() ### XXX BREAKPOINT
a=B()
a.fun()
a.dec(9,4)
