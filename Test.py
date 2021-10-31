import random

array = ['orange', 'apple', 'starwbery', 'lemon', 'grape', 'Bird', 'tomatoe']
random_number = random.randrange(8)

while 5 > len(random_number):
    array[random_number] = 'O'
    break


print(array)
