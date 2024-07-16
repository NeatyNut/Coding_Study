input_number = input().split(" ")
number = int(input_number[0])
count = int(input_number[1])

number += 1
while len(set(str(number))) != count:
    number += 1

print(number)