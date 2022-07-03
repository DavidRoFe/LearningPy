user = {'name': None,
        'age': None,
        'gender': None
        }

user["name"] = input('What is your name? ')
user["age"] = input('What is your age? ')
user["gender"] = input('What is your gender? ')

print(
    f'Hi {user["name"]}, your age is {user["age"]} and you are {user["gender"]}')
