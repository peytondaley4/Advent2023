def hash_str(string):
    curr_val = 0
    for char in string:
        num = ord(char)
        curr_val += num
        curr_val = (curr_val * 17) % 256
    return curr_val
f = open('input.txt')
data = f.readline().strip().split(',')
total = 0
boxes = [[] for i in range(256)]
for d in data:
    if '=' in d:
        s = d.split('=')[0]
        foc = int(d.split('=')[1])
        h = hash_str(s)
        found = False
        for el in boxes[h]:
            if el[0] == s:
                found = True
                boxes[h][boxes[h].index(el)] = (s, foc)
        if not found:
            boxes[h].append((s, foc))
    else:
        s = d[:len(d)-1]
        h = hash_str(s)
        for el in boxes[h]:
            if el[0] == s:
                boxes[h].remove(el)

total = 0
for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        total += (i + 1) * (j + 1) * boxes[i][j][1]
        
print(total)