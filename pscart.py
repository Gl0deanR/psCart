import requests
from bs4 import BeautifulSoup
import csv
import re

session = requests.Session()

payload = {'_username':'user_name',
        '_password':'password'}

#authenticate on the auth page
r = session.get("https://example.com/authentication, data=payload)
#get the session to the cart page
r = session.get("https://example.com/cart")

soup = BeautifulSoup(r.text, 'html.parser')

category = []
size = []
price = []
floor = []

#look for what you need under class, ID etc.
for item in soup.findAll('div', {'class': 'card cart-summary'}):
    category.append(item.get_text(strip=True))

print(category)
