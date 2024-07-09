import sys
import os
import base64

if len(sys.argv) != 3:
    print("Use next syntax: python3 exercise4.py encode|decode text")
elif sys.argv[1] == "encode":
    print(base64.b64encode(sys.argv[2].encode('ascii')).decode('ascii'))
elif sys.argv[1] == "decode":
    print(base64.b64decode(sys.argv[2].encode('ascii')).decode('ascii'))
else:
    print("Use next syntax: python3 exercise4.py encode|decode text")



