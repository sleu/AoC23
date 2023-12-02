sum1 = 0
sum2 =0

red = 12
green = 13
blue = 14
color = str()
#Game # = row+1?
with open('inputs/input02.txt') as i:
    input = i.read().splitlines()

for g, line in enumerate(input):
    rMax = 0
    gMax = 0
    bMax = 0

    input_list = line.split(' ')
    i=3
    while i < len(input_list):
        v=input_list[i]
        n=input_list[i-1]
        if i==len(input_list)-1:
            color = v
        else:
            color = v[:-1]
        match color:
            case "red":
                if int(n) > rMax:
                    rMax = int(n)
            case "green":
                if int(n) > gMax:
                    gMax = int(n)
            case "blue":
                if int(n) > bMax:
                    bMax = int(n)
        i+=2
    if rMax <= red and gMax <= green and bMax <= blue:
        sum1 += g+1
    
    sum2 += rMax * gMax * bMax
print("Part 1: %d " % sum1)
print("Part 2: %d " % sum2)