import json
import urllib.request, urllib.parse, urllib.error
import urllib
count = 0

url = "http://py4e-data.dr-chuck.net/comments_429914.json"
print ("retrieving URL. Stand by.")
#uh = urllib.urlopen(url)
#data= uh.read()
data = urllib.request.urlopen(url).read()

info = json.loads(data)
for item in info["comments"]:
	#print item["count"]
	number = int(item["count"])
	count = count + number
print (count)
