
#python3 myscript.py [filename]

import sys

#    [filename]
# sys.argv[0]

filename = sys.argv[0]
message = sys.argv[1]

with open(filename, 'w+')as f:
    f.write(message)

