sort = True

numbers = input('enter your numbers seprated by ",": ')

numbers = numbers.split(',')
num_list = [int(i) for i in numbers]

for i in range(1, len(num_list)):
    if num_list[i-1] > num_list[i]:
        sort = False
        break

if sort:
    print('list is sorted')
else:
    print("list isn't sorted")
