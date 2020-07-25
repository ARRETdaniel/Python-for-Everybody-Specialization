fname = input ('Enter file name: ')
try:
    file = open (fname)
except:
    print ('Erro.')
    quit()

st1 = list()

for line in file:
    line = line.rstrip()
    line = line.split()
    for i in line :
        if i not in st1:
            st1.append(i)

st1.sort()
print(st1)
