c = [5, 4, 45, 3]
for i in c :
    print (i)

print('--------------------------------------')

largest_so_far = None
print('Before', largest_so_far)
for the_num in [6, 41, 12, 3, 74, 13] :
    if largest_so_far is None :
        largest_so_far = the_num
    elif the_num < largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far)


print ('-----------------------------------')

zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)
