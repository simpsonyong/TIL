import requests
import csv
import time  # 네이버 디도스 인식을 방지하기 위해 time.sleep 기능 활용
from naver_API import send_naver_movie  # naver_API 모듈 사용

movienm_reader = csv.reader(open('./movie.csv', 'r', encoding='utf-8'))  # ./: 내 위치 안에 있는
next(movienm_reader, None)  # 헤더 줄을 읽지 않음

movienm_list = []  # 영화 제목 리스트 완성
moviecd_list = []  # 영화 대표코드 리스트 완성
for data in movienm_reader:
    moviecd_list.append(data[0])  # 1번째 'movieCd'열 data를 리스트로 추가
    movienm_list.append(data[1])  # 2번째 'movieNm'열 data를 리스트로 추가

# 영진위 영화 대표코드 , 하이퍼텍스트 link , 영화 썸네일 이미지의 URL , 유저 평점
fieldnames = ['movieCd', 'link', 'image', 'userRating']
movie_naver = csv.DictWriter(open('movie_naver.csv', 'w', encoding='utf-8', newline=''), fieldnames=fieldnames)
movie_naver.writeheader()

result = {}
# movie_naver.csv에 입력할 result라는 Dict 생성
for name in movienm_list:
    time.sleep(0.5)  # 0.5초 term을 넣어서 네이버측 서버 차단을 방지함
    source = send_naver_movie(name)  # Naver_API.py 모듈을 통해 data값 받기
    result['movieCd'] = moviecd_list[movienm_list.index(name)]
    result['link'] = source['items'][0]['link']
    if source['items'][0]['image']:  # 영화 썸네일 이미지의 URL 이 없는 경우 저장하지 않음
        result['image'] = source['items'][0]['image']
    result['userRating'] = source['items'][0]['userRating']
    movie_naver.writerow(result)
