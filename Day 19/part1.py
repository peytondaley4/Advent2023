f = open('input.txt')

rules = dict()
parts = []

for line in f:
    if line[0] == '{':
        temp = []
        for i in range(4):
            num = line.split(',')[i].split('=')[1]
            if i == 3:
                temp.append(int(num[:-2]))
            else:
                temp.append(int(num))
        parts.append(temp)
    elif line != '\n':
        name = line.split('{')[0]
        conds = line.split('{')[1][:-2]
        temp = []
        for c in conds.split(','):
            temp.append(c)
        rules[name] = temp
total = 0
for part in parts:
    rule = 'in'
    while True:
        if rule == 'A':
            total += sum(part)
            break
        elif rule == 'R':
            break
        conds = rules[rule]
        for c in conds:
            if len(c) > 1 and c[1] in ['<', '>']:
                val = int(c.split(':')[0][2:])
                dest = c.split(':')[1]
                if c[0] == 'a':
                    index = 2
                elif c[0] == 'm':
                    index = 1
                elif c[0] == 'x':
                    index = 0
                else:
                    index = 3
                if c[1] == '<' and part[index] < val:
                    rule = dest
                    break
                if c[1] == '>' and part[index] > val:
                    rule = dest
                    break
            else:
                rule = c
print(total)