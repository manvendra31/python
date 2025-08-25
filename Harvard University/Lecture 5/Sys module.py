'''
import sys

try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("To few arrgument")
'''

import sys

if len(sys.argv) < 2:  # Check if an argument is provided
    print("Too few arrgumrents")
elif len(sys.argv)>2:
    print("Too many arrguments")
else:
    print("Hello my name is",sys.argv[1])


import sys
print(sys.version)