import sys
from saying import hello
if len(sys.argv)==2:
    hello(sys.argv[1])

# We have seen i import only one but in the output all things print from the imported file