from functools import reduce

def capitalizer(item):

    return str(item).upper()

def is_over_50p(item):

    return item > 50

def accumulator(total, item):

    return total + item

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

print(list(map(capitalizer, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

my_numbers.sort()
print(list(zip(my_strings, my_numbers)))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

print(list(filter(is_over_50p, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

print(reduce(accumulator, scores, 0))
print(reduce(accumulator, my_strings, 'Let\'s spell '))

#5 Square
my_list = [5, 4, 3]

print(list(map(lambda num: num**2, my_list)))

#6 List sorting
a = [(0,2),(4,3),(9,9),(10,-1)]

a.sort(key=lambda x: x[1])
print(a)
