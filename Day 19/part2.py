def evaluate(part, rule):
    total = 0
    print(part, rule)
    for c in rules[rule]:
        if c[0] == 'A':
            tot = 1
            for p in part:
                tot *= p[1] - p[0] + 1
            return total + tot
        if c[0] == 'R':
            return total
        if ':' not in c:
            return total + evaluate(part, c)
        dest = c.split(':')[1]
        val = int(c.split(':')[0][2:])
        p2 = part.copy()
        index = marks[c[0]]
        if c[1] == '<':
            if part[index][0] >= val:
                continue
            high = min(p2[index][1], val-1)
            p2[index] = (p2[index][0], high)
            total += evaluate(p2, dest)
            if part[index][1] < val:
                return total
            part[index] = (val, part[index][1])
        else:
            if part[index][1] <= val:
                continue
            low = max(p2[index][0], val+1)
            p2[index] = (low, p2[index][1])
            total += evaluate(p2, dest)
            if part[index][0] > val:
                return total
            part[index] = (part[index][0], val)
        
f = open('input.txt')

rules = dict()
marks = {'x':0, 'm':1, 'a':2, 's':3}

for line in f:
    if line != '\n' and line[0] != '{':
        name = line.split('{')[0]
        conds = line.split('{')[1][:-2]
        temp = []
        for c in conds.split(','):
            temp.append(c)
        rules[name] = temp
        
rules['A'] = 'A'
rules['R'] = 'R'
total = 0
rule = 'in'
part = [(1,4000),(1,4000),(1,4000),(1,4000)]
print(evaluate(part, rule))