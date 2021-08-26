from bs4 import BeautifulSoup
import requests
import hashlib

# Grab html

raw_html = requests.get('http://[IP_GOES_HERE]').text

#Grab text from specific element in html (.text) and return string
soup = BeautifulSoup(raw_html, 'lxml')
str_from_html = soup.h3.text
print(str_from_html)

#Use hashlib to encrypt string with md5

result = hashlib.md5(str_from_html.encode())
print(result.hexdigest())

# Post the returned hexdigest
