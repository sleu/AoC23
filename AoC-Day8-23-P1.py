nodes = {}
with open('inputs/input08.txt') as i: input = i.read().splitlines()
input_list = [line.strip().split(" ") for line in input]
directions = [*input_list[0][0]]
for line in input_list[2:]:
    nodes[line[0]] = [line[2][1:4],line[3][:3]]

current_node = input_list[2][0]
dir = 0
steps = 0
print(directions)
while current_node != "ZZZ":
    steps += 1
    #print(current_node)
    if directions[dir] == "L":
        current_node = nodes[current_node][0]
    else:
        current_node = nodes[current_node][1]
    
    if dir == len(directions)-1:
        dir = 0
    else:
        dir += 1
print(steps)
