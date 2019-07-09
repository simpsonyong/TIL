import bs4
import requests
import csv

url = 'https://www.melon.com/chart/index.htm'

headers = {'User-Agent': ':)'} # 헤더값 : :)

response = requests.get(url, headers=headers).text # header 값 입력을 통해 사이트 자료 가져옴
text = bs4.BeautifulSoup(response, 'html.parser') # parser를 통해서 예쁘게 꾸며준다
rows = text.select('.lst50') # lst50 하나하나 랭크를 가져온다

writer = csv.writer(open('melon50.csv', 'w', encoding='utf-8' , newline=''))
writer.writerow(['순위', '제목', '가수'])

for row in rows:
    rank = row.select_one('td:nth-child(2) > div > span.rank').text
    title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    # print(rank, title, artist)
    # f.write(f'{rank},{title},{artist}\n')
    # f.write(r'' + ',' + r'' + ',' + r'' + '\n')
    writer.writerow([rank, title, artist])
