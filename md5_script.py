from bs4 import BeautifulSoup
import requests
import hashlib


url = 'http://46.101.14.69:30636' # YOUR IP HERE
# Grab html

raw_html = requests.get(url).text

#Grab text from specific element in html (.text) and return string
soup = BeautifulSoup(raw_html, 'lxml')
str_from_html = soup.h3.text
print(str_from_html)

#Use hashlib to encrypt string with md5

result = hashlib.md5(str_from_html.encode())
hashed = result.hexdigest()

# Post the returned hexdigest

r = requests.post(url, data=hashed)

print(r.content)
