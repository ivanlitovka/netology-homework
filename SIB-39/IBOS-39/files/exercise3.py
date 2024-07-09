import sys
import os

if os.path.isdir(sys.argv[1]):
    print("this directory")
elif os.path.isfile(sys.argv[1]):
    print("this file")
else:
    print("Object not exist")