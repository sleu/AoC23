sum = 0
with open('inputs/input01.txt') as i:
    read_list = i.read().splitlines()
for l in read_list:
    numbers = [int(i) for i in l if i.isdigit()] #extract digits
    value = str(numbers[0]) + str(numbers[-1])
    sum += int(value)
print(sum)