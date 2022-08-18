from bs4 import BeautifulSoup
import requests

#google custom search api key =  AIzaSyCMpSXq4lDaVOIjqH5_Wywox4f4XHmQ4MQ 
url = "https://www.bookdepository.com/bestsellers"
response = requests.get(url)

html = response.content
soup = BeautifulSoup(html, "lxml")
print(soup.title.get_text())