fh = open('mbox-short.txt')
count = 0
average = 0
i = float(average)
counts = dict()
for line in fh:
    if not line.startswith("From ") : continue
    count = count + 1
    line = line.rstrip()
    line = line.split()
    #pos = line.find('@')
    pe = line[1]
    #e = float(pe)
    #line = line.rstrip()
    #separar = pe.split()
    counts[pe] = counts.get(pe, 0) + 1


print (counts)
#print('---------', separar)
bigcount = None
bigword = None
for words, valor in counts.items() :
    if bigcount is None or valor > bigcount :
        bigword = words
        bigcount = valor

print (bigword, bigcount)

print('linhas: ',counts)

    #i += e





#for data in line :
#    pos = data.find(':')
#    pe = data[pos+1:]
#    print(pe)
#w = i / 27

#print(i)
#print (w)
