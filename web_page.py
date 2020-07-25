import urllib.request, urllib.parse, urllib.errors
pip install beautifulsoup4 
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand :
    print(line.decode().strip())
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)
