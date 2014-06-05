#!/usr/bin/env python
from OpenSSL.crypto import load_privatekey, FILETYPE_PEM, sign
import base64

key = load_privatekey(FILETYPE_PEM, open("pp.py", 'r').read())
content = 'test_message'

import ipdb; ipdb.set_trace() ### XXX BREAKPOINT
d =  sign(key, content, 'sha1')
b = base64.b64encode(d)
print b
