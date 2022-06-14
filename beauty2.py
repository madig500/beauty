# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
veces= int(input('Enter Count: '))
position= int(input('Enter Position: '))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
cuenta=1
kkk=1
while kkk <= veces:
    for tag in tags:

        if cuenta == position :
            print(tag.get('href', None))
            url=tag.get('href', None)
            html = urllib.request.urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup('a')
            cuenta=1
            break
        cuenta=cuenta+1
    kkk=kkk + 1
