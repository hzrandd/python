# -*- coding: utf-8 -*-
import StringIO
import cStringIO
s1 = StringIO.StringIO("rdd is a handsome boy")
s1.write("hi,i love u!")
s1.seek(-1, 1)
s1.write("中国")
s1.seek(0)

print s1.read()

s1.seek(-4,2)
#print s1.read()
