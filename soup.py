import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

counts = 0

url = 'http://py4e-data.dr-chuck.net/known_by_Klein.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')

for tag in tags:
    counts += 1
    print(tag.get('href', None))
    if counts == 18 :
        quit()


print(counts)
