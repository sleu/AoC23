seeds = []
seed_locations = []
almanac = []

def locate(seed, section):
    for i,m in enumerate(almanac[section]):
        start = int(m[1])
        end = int(m[1])+int(m[2])+1
        dest = seed
        #print("Seed %d, Start %d, End %d, section %d" % (seed, start, end, section))
        if seed in range(start,end) and section < len(almanac)-1: #more sections, match
             dest = seed - int(m[1]) + int(m[0])
             return locate(dest, section+1)
        elif seed in range(start,end) and section == len(almanac)-1: #last section, match
            dest = seed - int(m[1]) + int(m[0])
            return dest
        elif section == len(almanac)-1 and i == len(almanac[section])-1: #last section, no match
            return dest
        elif i == len(almanac[section])-1: #no match
            return locate(dest, section+1)
    return dest

with open('inputs/input05.txt') as i: input = i.read().splitlines()
input_list = [line.strip().split(" ") for line in input]
seeds = input_list[0][1:]

m = []
for list in input_list[3:]:
    if list[0].isdigit():
        m.append(list)
    elif not list[0].isdigit() and len(list) == 1:
        almanac.append(m)
        m = []
    if list == input_list[-1]:
        almanac.append(m)
for s in seeds:
    seed_locations.append(locate(int(s),0))

#for seeds, get smallest
print(min(seed_locations))