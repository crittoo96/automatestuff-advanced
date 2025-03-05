### beautifulsoup4を利用して、
### https://github.com/oreilly-japan/automatestuff2-ja/blob/main/ch16/example.csvをダウンロードして、
### sample.csvとして保存するスクリプト

import requests
from bs4 import BeautifulSoup

# website_url = 'https://github.com/oreilly-japan/automatestuff2-ja/blob/main/ch16/'
# response = requests.get(website_url)
# response.raise_for_status()

# soup = BeautifulSoup(response.text, 'html.parser')
# excel_link = soup.select('a[href*="example.csv"]')[0]


## 直接CSVファイルのURLを指定する
excel_link_url = "https://github.com/oreilly-japan/automatestuff2-ja/raw/refs/heads/main/ch13/censuspopdata.xlsx"

response = requests.get(excel_link_url)
response.raise_for_status()

with open("dl_censuspopdata.xlsx", "wb") as file:
    for chunk in response.iter_content(100000):
        file.write(chunk)

print("dl_censuspopdata.xlsxをダウンロードしました。")
