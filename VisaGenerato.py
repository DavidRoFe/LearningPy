import random

def generate_visa():
    """
    Generates a random Visa credit card number
    """
    # Initialize the card number with the prefix 4
    card_number = "4"

    # Generate the next 14 digits randomly
    for i in range(14):
        card_number += str(random.randint(0, 9))

    # Calculate the checksum digit using the Luhn algorithm
    checksum = 0
    for i, digit in enumerate(card_number):
        if (i + 1) % 2 == 0:
            temp = int(digit) * 2
            checksum += temp if temp < 10 else temp - 9
        else:
            checksum += int(digit)
    card_number += str((10 - checksum % 10) % 10)

    return card_number

# Example usage
print(generate_visa())