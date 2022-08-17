from bs4 import BeautifulSoup
import requests


URL = "https://www.geeksforgeeks.org/data-structures/"
r = requests.get(URL)
print(r.content)

