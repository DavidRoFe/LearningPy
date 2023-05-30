# Importing modules
from re import T
import urllib.request
from random import randint

# Class definition
class Cat:

    word_site = 'https://www.mit.edu/~ecprice/wordlist.10000'
    species = 'mammal'

    def __init__(self, name, age):

        self._name = name
        self._age = age
    # End __init__()

    @classmethod
    def random_cat(cls):

        response = urllib.request.urlopen(Cat.word_site)
        long_txt = response.read().decode()
        words = long_txt.splitlines()

        return cls(words[randint(1, 9999)], randint(1, 100))
    # End random_cat()

    @staticmethod

    def get_oldest(cat_list):

        cat_oldest = cat_list[0]
        for item in cat_list[1::]:

            if item._age > cat_oldest._age:

                cat_oldest = item

        return cat_oldest
    # End get_oldest()

    def create_cats(cats_no):

        cat_list = []
        cats_count = 0
        while cats_count < cats_no:

            cat_list.append(Cat.random_cat())

            cats_count += 1

        return cat_list
    # End create_cats()


# Main Logic
while True:

    cats_no = int(input(f'How many cats do you want? '))

    if cats_no < 1 or cats_no > 99:

        print('Enter a number between 1 and 99')

    else:

        break

cat_list = Cat.create_cats(cats_no)

cat_oldest = Cat.get_oldest(cat_list)

print(f'The oldest cat is {cat_oldest._age} years old and it\'s name is {cat_oldest._name}')
