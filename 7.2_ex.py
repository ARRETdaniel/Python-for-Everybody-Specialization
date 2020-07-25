# Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
fh = open('mbox-short.txt')
count = 0
average = 0
i = float(average)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    pos = line.find(':')
    pe = line[pos+2:]
    e = float(pe)
    print (e)
    i += e
#for data in line :
#    pos = data.find(':')
#    pe = data[pos+1:]
#    print(pe)
w = i / 27

print(count)
print(i)
print (w)
