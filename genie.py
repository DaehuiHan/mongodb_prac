import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
# # body-content > div.newest-list > div > table > tbody > tr:nth-child(1)
# # body-content > div.newest-list > div > table > tbody > tr:nth-child(2)
# 이렇게 해서 줄 전체에 대해 trs를 모아온다
# 그 후에 tr에서 제목 랭킹 가수를 한개씩만 찾아서 뽑아준다

for tr in trs:
    title = tr.select_one('td.info > a.title.ellipsis').text.strip()
# body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
# body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.number
# body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
    rank = tr.select_one('td.number').text[0:3].rstrip()
# body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
    singer = tr.select_one('td.info > a.artist.ellipsis').text
    print(rank, title, singer)
