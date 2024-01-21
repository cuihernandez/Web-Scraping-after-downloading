import requests
from bs4 import BeautifulSoup


cookies = {
    's2_uLang': 'en',
    's2_theme_ui': 'red',
    'PHPSESSID': '7km4000fle7su7f2vbj9lsiop5',
    's2_uGoo': '8c6bc9f56abd972da2cb9813e2ae0bbe0328bd2d',
    'sh': '93.1',
    'sw': '110.8',
}

headers = {
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 's2_uLang=en; s2_theme_ui=red; PHPSESSID=7km4000fle7su7f2vbj9lsiop5; s2_uGoo=8c6bc9f56abd972da2cb9813e2ae0bbe0328bd2d; sh=93.1; sw=110.8',
    'Origin': 'https://myip.ms',
    'Referer': 'https://myip.ms/browse/sites/1/own/376714/cntVisitors/100/cntVisitorsii/3000',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'getpage': 'yes',
    'lang': 'en',
}

response = requests.post(
    'https://myip.ms/ajax_table/sites/11302/own/376714/cntVisitors/100/cntVisitorsii/3000',
    cookies=cookies,
    headers=headers,
    data=data,
)
print(response.text)
soup = BeautifulSoup(response.text, features="html5lib")
websites = soup.find_all('td', class_='row_name')

for website in websites:
    website_url = website.get_text(strip=True)
    print(f"Websites URL: {website_url}")
    
