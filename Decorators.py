#Decorators
import re
from time import time

def my_decorator(func):

    def wrap_func(*args, **kwargs):

        print('************')
        func(*args, **kwargs)
        print('************')
    
    return wrap_func

@my_decorator
def hello(greeting, emoji):

    print(greeting, emoji)

hello('Hi!', ' :D')

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'Took {t2-t1} ms')
        return result    
    return wrapper

@performance
def long_time():

    for i in range  (10000):

        i*5

long_time()

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
  def wrapper(*args, **kwargs):
    if args[0]['valid']:
        fn(*args, **kwargs)
  return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)