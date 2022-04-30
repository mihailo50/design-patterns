

def mydecorator(function):

    def wrapper(*args, **kwargs):
        return_val =  function(*args, **kwargs)
        print("Decorating function.")
        return return_val

    return wrapper

@mydecorator # python way
def hello(person):
    return f'Hello {person}!'

#mydecorator(hello)() # wrong way

hello('Mike')

print('--------------------------')
# practical ex1 -> Logging

def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('/home/mihailo/Desktop/Advanced/logfile.txt', 'a+') as f:
            fname = function.__name__
            f.write(f"{fname} return value {value}")
        return value
    return wrapper

@logged
def add(x, y):
    return x + y

print(add(10, 20))


# practical ex2 -> Timing
import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after-before} s to execute.")
        return value
    return wrapper

@timed
def count(steps):
    i=0
    for i in range(0,steps):
        i+=1
        print(f"\n{i}")

count(10000)