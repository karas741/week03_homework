import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
baseball = soup.select('.tbl_box > table > tbody > tr')

# movies (tr들) 의 반복문을 돌리기
for kbo in baseball:
    # kbo 안에 a 가 있으면,
    span_tag = kbo.select_one('td.tm > div > span')
    if span_tag is not None:
        rank = kbo.select_one('th > strong').text
        team = span_tag.text  # a 태그 사이의 텍스트를 가져오기
        # tar = kbo.select_one('td.point').text  # td 태그 사이의 텍스트를 가져오기
        print(rank, team)
