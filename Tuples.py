
c = {'a' : 10, 'b' : 1, 'c' : 22}

print (sorted( [ (v, k) for k, v in c.items() ] ) )

##########################################
d = dict()

d['cdev'] = 2
d['cwen'] = 4
for (k,v) in d.items() :
    print(k, v)

tups = d.items()
print(tups)


##############################################

c = {'a' : 10, 'b' :1, 'c' :22}
tmp = list()

for k, v in c.items()
    tmp.append((v, k))

print(tmp)

tmp = sorted(tmp, reverse=True)
print (tmp)

###############################################

fhand = open('romeo.txt')
counts = dict()

for line in fhand :
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

st1 = list()
    for key, val in counts.items() :
        newtup = (val, key)
        st1.apeend(newtup)

st1 = sorted(st1, reverse=True)

for val, key in st1[:10] :
    print(key, val)
