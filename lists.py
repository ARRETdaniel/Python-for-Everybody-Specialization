#######################################
friends = ['Joseph', 'Glen']

for friend in friends :
    print ('Happy new year: ', friend)

for i in range(len(friends)) :
    friend = friends[i]
    print ('happy new year: ', friend)

#######################################


t = [9,9,9,5,4,23,63]
print(t[:])

9 in t

100 not in t

print (len(t))

print(max(t))

print(min(t))

print (sum(t))

print (sum(t)/len(t))


#####################################


numlist = list()
while True :
    inp = input('Enter num: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

averege = sum(numlist) / len(numlist)
print('Averege: ', averege)


#####################################

abc = 'With three words'
stuff = abc.split() #pode usar ;(e outras coisas) como parametro de split
print(stuff)
print(len(stuff))
print (stuff[0])
print(stuff)
for w in stuff :
    print (w)
