fh = open('mbox-short.txt')

counts = dict()
for line in fh:
    if not line.startswith("From ") : continue
    line = line.rstrip()
    li = line.split()
    pe = li[5]
    pos = pe.find(':')
    eita = pe[0:2]
    counts[eita] = counts.get(eita, 0) + 1

c = counts
tmp = list()

for k, v in c.items() :
    tmp.append((k, v))

tmp.sort()

for k, v in tmp :
    print(k, v)
