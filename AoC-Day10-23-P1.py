import math
with open('inputs/input10.txt') as i: input = i.read().splitlines()

start = [] #x,y,direction
map = []
count = 0
for i, line in enumerate(input):
    map.append(list(line))
    if "S" in line: start = [line.index("S"), i]

def first_shape(): #doesn't check edges
    if map[start[1]][start[0]+1] in "-J7": #check east
        return [start[0]+1,start[1], "east"]
    elif map[start[1]+1][start[0]] in "|LJ": #check south
        return [start[0],start[1]+1, "south"]
    elif map[start[1]][start[0]-1] in "|-LF": #check west
        return [start[0]-1,start[1], "west"]
    elif map[start[1]-1][start[0]] in "|7F": #check north
        return [start[0],start[1]-1, "north"]
    else:
        return [0,0,""]

def next_shape(pos):
    #print(map[pos[1]][pos[0]])
    dir = pos[2]
    match map[pos[1]][pos[0]]:
        case "|":
            if dir == "south":
                pos[2] = "south"
                pos[1] +=1
            else:
                pos[2] = "north"
                pos[1] -=1
        case "-":
            if dir == "west":
                pos[2] = "west"
                pos[0] -=1
            else:
                pos[2] = "east"
                pos[0] +=1
        case "L":
            if dir == "south":
                pos[2] = "east"
                pos[0] +=1
            else:
                pos[2] = "north"
                pos[1] -=1
        case "J":
            if dir == "south":
                pos[2] = "west"
                pos[0] -=1
            else:
                pos[2] = "north"
                pos[1] -=1
        case "7":
            if dir == "north":
                pos[2] = "west"
                pos[0] -=1
            else:
                pos[2] = "south"
                pos[1] +=1
        case "F":
            if dir == 'north':
                pos[2] = "east"
                pos[0] +=1
            else:
                pos[2] = "south"
                pos[1] +=1
    return pos

position = first_shape()
count = 0
while map[position[1]][position[0]] != "S":
    count+=1
    position = next_shape(position)
furthest = math.ceil(count/2)
print(furthest)