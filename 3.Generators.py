# seq 1 to 9 000 000
import sys

def generator(n):
    for i in range(n):
        yield i ** 3

values = generator(100000)

for i in values:
    print(i)
    print(sys.getsizeof(values))