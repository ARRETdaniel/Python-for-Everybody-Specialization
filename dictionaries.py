name = input ('Enter file: ')
handle = open(name)

counts = dict()
for line in handle :
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items() :
    if bigcount is None or count > bigcount :
        bigword = word
        bigcount = count

print (bigword, bigcount)




















counts = dict ()
names = ['csev','cwen', 'csev', 'zqian', 'cwen']
for name in  names :
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1

print(counts)

print('+++++++++++++++++++++++++++++++++++++++++++++++++')
###################################
counts = dict()
names = ['csev','cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)
######################################

###################################
print('++++++++++++++++++++++++++++++++++++++++++')
if name in counts :
    x = counts[name]
else :
    x = 0

x = counts.get(name, 0)

print('++++++++++++++++++++++++++++++++++++++++++')

counts = dict()
print ('Enter a line:')
line = input('')

words = line.split()

print('Words:', words)

for word in words
    counts[word] = counts.get(word, 0) + 1

print('Counts: ', counts)

##########################################

jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
    for aaa,bbb in jjj.items() :
        print(aaa, bbb)

##################
