# First install Faker using command --> pip install Faker
#  'Faker' library, which is designed for generating fake data, including names.

# from faker import Faker
#
# # Initialize the Faker object
# fake = Faker()
#
# # Generate and print a random name
# random_name = fake.name()
# print("Random Name:", random_name)




import random

# Lists of vowels and consonants
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

def generate_name(length):
    name = ''
    for i in range(length):
        if i % 2 == 0:
            name += random.choice(consonants)
        else:
            name += random.choice(vowels)
    return name.capitalize()

# Generate and print a random name with a specified length
name_length = 6
random_name = generate_name(name_length)
print(random_name)