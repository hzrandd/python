class A(object):
    # class A: here will raise TypeError --> must be type, not classobj
    # we use the 'super' in new style class
    def __init__(self):
        print("Enter A")
        print("Leave A")

    def func(self):
        print 'A.....func called'

class B(A):
    def __init__(self):
        print("Enter B")
        super(B, self).__init__()
        print("Leave B")

class C(A):
    def __init__(self):
        print("Enter C")
        super(C, self).__init__()
        print("Leave C")

class D(A):
    def __init__(self):
        print("Enter D")
        super(D, self).__init__()
        print("Leave D")

class E(B, C, D):
    msg = 'old'
    def __init__(self):
        print("Enter E")
        super(E, self).__init__()
        print("Leave E")

    def func(self):
        super(E, self).func()
        print 'E ...func called.'

    def print_msg(self, msg):
        print self.msg
        self.msg = msg
        print self.msg

e = E()
e.func()
e.print_msg('new')

