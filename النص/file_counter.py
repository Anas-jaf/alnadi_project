import os 
import sys
from pathlib import Path

from os import listdir
from os.path import isfile, join


# count = 0

# for path in pathlib.Path(".").iterdir():

#     if path.is_file():

#         count += 1


# print(count)

listoffiles = os.listdir()
listoffiles1 = sorted(listoffiles)

# typeof=type(listoffiles)

print('\n'.join(map(str, listoffiles1)))

# print (listoffiles1)




