import random

def generate_NIF():
    letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    dni = ""
    for i in range(8):
        dni += str(random.randint(0, 9))
    nif = dni + letters[int(dni) % 23]
    return nif

print(generate_NIF())