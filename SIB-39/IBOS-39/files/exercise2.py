import sys
import os

dirs = next(os.walk(sys.argv[1]))[1]
count = 0
for i in dirs:
    print(i)
    count+=1
print(count," Files in folder")