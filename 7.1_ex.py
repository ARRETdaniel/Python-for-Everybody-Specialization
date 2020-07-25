fname = input ('enter the file name: ')
count = 0
try:
  fhand = open(fname, 'r')
except:
  print ('File cannot be opened:', fname)
  quit()

#inp = fhand.read()
#print (len(inp))


for file in fhand :
    #count = count + 1
    fi = file.rstrip()
    print(fi.upper())

#print(count)
