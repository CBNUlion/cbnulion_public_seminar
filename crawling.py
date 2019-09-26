import csv
import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent

url = "https://datalab.naver.com/keyword/realtimeList.naver?where=main"
headers = {"User-Agent": UserAgent().chrome}
response = requests.get(url, headers=headers)

# 요청한 페이지 확인하기
# print(response.content)

html = bs(response.text.encode("utf-8"), "lxml")
cols = html.select(".rank_list.v2")
titles = html.select(".rank_title.v2")

header_list = ["순위", "검색어"]
for col, title in zip(cols, titles):
    with open("{}.csv".format(title.get_text()), "wt", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header_list)
        for idx, v in enumerate(col.find_all("span", {"class": "title"}), 1):
            writer.writerow([idx, v.get_text()])
