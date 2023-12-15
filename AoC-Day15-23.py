with open('inputs/input15.txt') as i: input = i.read().split(",")

sum = 0

for i in input:
    curr_val = 0
    for c in i:
        curr_val += ord(c)
        curr_val *= 17
        curr_val %= 256
    sum += curr_val
print(sum)