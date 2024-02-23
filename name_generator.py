import random
import string

name_quantity = int(input('How many EC2 instances do you need names for? '))
department_name = input('What department do you work in? ')

for _ in range(name_quantity):
    random_numbers = random.randint(9999, 33333333)
    random_chars = ''.join(random.choices(string.ascii_letters, k=3))
    instance_name = f"{department_name} {random_chars}_{random_numbers}"
    print(instance_name)
