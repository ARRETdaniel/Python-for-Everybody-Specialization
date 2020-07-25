import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = ' http://py4e-data.dr-chuck.net/comments_429913.xml'

data = urllib.request.urlopen(url).read()

tree = ET.fromstring(data)

counts = tree.findall('comments/comment/count')

total = 0
for count in counts:
    total += int(count.text)

print ('total: ', total)
