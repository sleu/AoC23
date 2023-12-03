sum = 0
the_map = []
row_length = 0
col_length = 0

def is_symbol(value):
    if not value.isdigit() and not value == ".":
        return True
    else:
        return False

def check_right(x,y):
    number = ""
    z=1
    while x+z < row_length:
        position = the_map[y][x+z]
        if position.isdigit():
            number.join(str(position))
            position = "."
            z+=1
        else:
            z+=row_length
    if number != "":
        sum += int(number)

def check_left(x,y):
    number = ""
    z=1
    while x-z >= 0:
        position = the_map[y][x-z]
        if position.isdigit():
            number.join(str(position))
            position = "."
            z+=1
        else:
            z+=row_length
    if number != "":
        sum += int(number)
def check_up(x,y):
    number = ""
    z=1
    while y-z >= 0:
        position = the_map[y-z][x]
        if position.isdigit():
            number.join(str(position))
            position = "."
            z+=1
        else:
            z+=col_length
    if number != "":
        sum += int(number)
def check_down(x,y):
    number = ""
    z=1
    while y+z < col_length:
        position = the_map[y+z][x]
        if position.isdigit(): #check left and right to build number properlys
            number+=str(position)
            
            position = "."
            z+=1
        else:
            z+=col_length
    if number != "":
        return int(number)
    else:
        return 0

def check_adjacent(x,y):
    total = 0
    #check_up(x,y)
    total += check_down(x,y)
    #check_left(x,y)
    #check_right(x,y)
    return total




with open('inputs/sample.txt') as i: input = i.read().splitlines()

for line in input: #builds map
    row = []
    for value in line:
        row.append(value)
    the_map.append(row)
    #print(row)

row_length = len(the_map[0])
col_length = len(the_map)

for y,row in enumerate(the_map):
    for x,value in enumerate(row):
        if is_symbol(value):
            print("value:", value)
            sum += check_adjacent(x,y)
print(sum)

#number isn't being build
#number could be in left or right or center direction
#fix then account for diagnals