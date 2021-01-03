# Get cracking Helena!
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import requests
from requests_html import HTMLSession

url = "https://www.oliverbonas.com/homeware/white-palma-ceramic-mug-315587"

session = HTMLSession()
resp = session.get(url)
resp.html.render()
raw_html = resp.html.html

soup = BeautifulSoup(raw_html, "html.parser")

#text = soup.get_text()
prices = soup.find_all("span", class_="price-value")
for thing in prices:
	print(thing.string)