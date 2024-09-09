import random
import string
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
length = int(input("Enter the length of the random string: "))
random_string = generate_random_string(length)
print("Random string:", random_string)
