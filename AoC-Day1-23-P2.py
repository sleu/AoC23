sum = 0
word_dict = {"one": "o1ne", "two": "t2wo", "three": "th3ree", "four": "fo4ur", "five": "fi5ve", "six": "si6x", "seven": "se7ven", "eight": "ei8ght", "nine": "ni9ne"}

with open('inputs/input01.txt') as i:
    read_list = i.read().splitlines()
for l in read_list:
    for word, num in word_dict.items():
        l = l.replace(word, num)
    numbers = [int(i) for i in l.replace(word, num) if i.isdigit()]
    value = str(numbers[0]) + str(numbers[-1])
    sum += int(value)
    print(sum)