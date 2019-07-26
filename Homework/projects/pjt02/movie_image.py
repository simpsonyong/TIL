import requests
import csv
import time  # 네이버 디도스 인식을 방지하기 위해 time.sleep 기능 활용

movie_url_reader = csv.reader(open('./movie_naver.csv', 'r', encoding='utf-8'))  # ./: 내 위치 안에 있는
next(movie_url_reader, None)  # 헤더 줄을 읽지 않음

movie_url_list = []  # 영화 이미지 URL주소 리스트 완성
movie_cd_list = []  # 영화 cd리스트 오나성
for data in movie_url_reader:
    movie_url_list.append(data[2])  # 3번째 'image'열 data를 리스트로 추가
    movie_cd_list.append(data[0])

for url in movie_url_list:
    time.sleep(0.5)
    image = requests.get(url, stream=True).content  # 사진이 담김
    moviecd = movie_cd_list[movie_url_list.index(url)]
    # 순환하는 동안 각각의 url 값을 가지고 있는 movie_url_list의 순번과 일치하는
    # movie_naver.moviecd_list의 값을 moviecd라는 변수로 저장
    open(f'./images/{moviecd}.jpg', 'wb').write(image)  # 이미지를 wb옵션으로 저장함
