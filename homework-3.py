import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서 불러오기
musicSum = soup.select('#body-content > div.newest-list > div > table > tbody > tr > td.info')
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis

#rank = 1
#for music in musicSum:
#    title = music.find(class_='title ellipsis').text
#    artist = music.find(class_='artist ellipsis').text
#    print(rank, title, artist)
#    rank += 1

rank = 1
for music in musicSum:
    title = music.select_one('a.title.ellipsis').text
    artist = music.select_one('a.artist.ellipsis').text
    print(rank, title, artist)
    rank += 1

