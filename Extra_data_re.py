
import re
fname = 'regex_sum_429909.txt'
x = open(fname)
w = dict()
numlist = list()
for line in x :
    line = line.rstrip()
    #li = line.split()
    y = re.findall ('[0-9]+', line)
    if len(y) < 1 : continue #######################################
    #numlist.append(y)
    #print(y)
    for i in range(len(y)):
        num = int(y[i])
        numlist.append(num)

#print(numlist)
print(sum(numlist))
    #print(y)
#print (numlist)

##print(numlist)
#r = numlist.split()

#for x in numlist:
#    w = re.findall ('[0-9]+', numlist)
#    print(w)
    #print(y)
