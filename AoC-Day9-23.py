with open('inputs/sample.txt') as i: input = i.read().splitlines()
input_list = [line.strip().split(" ") for line in input]

def play(list):
    diff_list = []
    for i, v in enumerate(list[:len(list)-1]):
        diff_list.append(int(list[i+1]) - int(v))
    #store list
    if diff_list.count(0) == len(diff_list):
        #found 0s
        return 0

for i in input_list:
    play(i)