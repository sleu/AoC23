sum1 = 0
sum2 = 0
the_map = []
row_length = 0
col_length = 0

def is_symbol(value):
    if not value.isdigit() and value != ".":
        return True
    else:
        return False

def is_gear(value):
    if value == "*":
        return True
    else:
        return False

def check_right(x,y):
    number = ""
    z=1
    while x+z < row_length:
        if the_map[y][x+z].isdigit():
            number += str(the_map[y][x+z])
            the_map[y][x+z] = "."
            z+=1
        else:
            z+=row_length
    if number != "":
        return int(number)
    else:
        return 0

def check_left(x,y):
    number = ""
    z=1
    while x-z >= 0:
        if the_map[y][x-z].isdigit():
            number += str(the_map[y][x-z])
            the_map[y][x-z] = "."
            z+=1
        else:
            z+=row_length
    if number != "":
        number_reverse = number[::-1]
        return int(number_reverse)
    else:
        return 0

def check_up(x,y):
    number = ""
    if y <= 0: #at top, no higher
        return 0
    else:
        up1 = y-1
    if the_map[up1][x].isdigit():
        if x-1 >= 0: #<---
            if the_map[up1][x-1].isdigit():
                if x-2 >= 0:
                    if the_map[up1][x-2].isdigit():
                        number += str(the_map[up1][x-2])
                        the_map[up1][x-2] = "."
                number += str(the_map[up1][x-1])
                the_map[up1][x-1] = "."
        number += str(the_map[up1][x]) #center
        the_map[up1][x] = "."
        if x+1 < col_length: #--->
            if the_map[up1][x+1].isdigit():
                number +=str (the_map[up1][x+1])
                the_map[up1][x+1] = "."
                if x+2 < col_length:
                    if the_map[up1][x+2].isdigit():
                        number += str(the_map[up1][x+2])
                        the_map[up1][x+2] = "."
    if number != "":
        return int(number)
    else:
        return 0

def check_down(x,y):
    number = ""
    if y >= col_length-1: #at bottom, no down
        return 0
    else:
        down1 = y+1
    if the_map[down1][x].isdigit():
        if x-1 >= 0: #<---
            if the_map[down1][x-1].isdigit():
                if x-2 >= 0:
                    if the_map[down1][x-2].isdigit():
                        number += str(the_map[down1][x-2])
                        the_map[down1][x-2] = "."
                number += str(the_map[down1][x-1])
                the_map[down1][x-1] = "."
        number += str(the_map[down1][x]) #center
        the_map[down1][x] = "."
        if x+1 < col_length: #--->
            if the_map[down1][x+1].isdigit():
                number += str(the_map[down1][x+1])
                the_map[down1][x+1] = "."
                if x+2 < col_length:
                    if the_map[down1][x+2].isdigit():
                        number += str(the_map[down1][x+2])
                        the_map[down1][x+2] = "."
    if number != "":
        return int(number)
    else:
        return 0

def check_adjacent(x,y):
    total = 0
    total += check_up(x,y)
    total += check_down(x,y)
    total += check_left(x,y)
    total += check_right(x,y)
    total += check_right(x,y+1) #lower right corner
    total += check_right(x,y-1) #upper right corner
    total += check_left(x,y+1) #lower left corner  
    total += check_left(x,y-1) #upper left corner
    return total

def gear_ratio(x,y):
    values = []
    up = check_up(x,y)
    if up > 0: values.append(up)

    down = check_down(x,y)
    if down > 0: values.append(down)

    left = check_left(x,y)
    if left > 0: values.append(left)
    
    if len(values) < 3:
        right = check_right(x,y)
        if right > 0: values.append(right)

    if len(values) < 3: 
        lright = check_right(x,y+1)
        if lright > 0: values.append(lright) #lower right corner

    if len(values) < 3: 
        uright = check_right(x,y-1)
        if uright > 0: values.append(uright) #upper right corner
        
    if len(values) < 3: 
        lleft = check_left(x,y+1)
        if lleft > 0: values.append(lleft) #lower left corner
        
    if len(values) < 3: 
        uleft = check_left(x,y-1)
        if uleft > 0: values.append(uleft) #upper left corner
    
    if len(values) == 2:
        return values[0] * values[1]
    else:
        return 0

with open('inputs/input03.txt') as i: input = i.read().splitlines()

for line in input: #builds map
    row = []
    for value in line:
        row.append(value)
    the_map.append(row)

row_length = len(the_map[0])
col_length = len(the_map)

for y,row in enumerate(the_map):
    for x,value in enumerate(row): #comment out due to map clears on each use; can only run one
        """if is_symbol(value):
            sum1 += check_adjacent(x,y)"""
        if is_gear(value):
            sum2 += gear_ratio(x,y)

print("Part 1:", sum1)
print("Part 2: ", sum2)