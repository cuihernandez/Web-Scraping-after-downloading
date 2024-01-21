import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.vivehealth.com/"
r = requests.get(URL).text

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html5lib")

text = soup.body.get_text(separator= '\n', strip=True)
print(text)