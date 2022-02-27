import random

numbers = []
i = 0

while True:
    input_num = input('enter length: ')
    if input_num.isdigit() and int(input_num) > 0:
        n = int(input_num)
        break
    else:
        print("you didn't enter valid number")


while i < n:
    x = random.choice(range(1000))
    if x not in numbers:
        numbers.append(x)
        i += 1
