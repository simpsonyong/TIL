import requests
import time
from datetime import datetime, timedelta
from decouple import config
import csv
import json

with open('movie.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['movieCd', 'movieNm', "movieNmEn", "movieNmOg", 'openDt', 'watchGradeNm', 'showTm', 'openDt', 'movie_data', 'directors']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    API_KEY = config('API_KEY')
    movie_codes = []

    with open('boxoffice.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        movie_codes = []
        for row in reader:
            movie_codes.append(row['movieCd'])

    for movie_code in movie_codes:
        URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={API_KEY}&movieCd={movie_code}'
        movie_data = requests.get(URL).json()
        result = {}  # CSV로 저장할 최종 딕셔너리 자료
        result['movieCd'] = movie_data["movieInfoResult"]['movieInfo']['movieCd']  # 대표코드
        result['movieNm'] = movie_data['movieInfoResult']['movieInfo']['movieNm']  # 영화명(국문)
        result['movieNmEn'] = movie_data['movieInfoResult']['movieInfo']['movieNmEn']  # 영화명(영문)
        if movie_data['movieInfoResult']['movieInfo']['movieNmOg']:
            result['movieNmOg'] = movie_data['movieInfoResult']['movieInfo']['movieNmOg']  # 영화명(원문)
        result['openDt'] = movie_data['movieInfoResult']['movieInfo']['openDt']  # 개봉일자
        if movie_data['movieInfoResult']['movieInfo']['audits']:  # 관람등급
            result['watchGradeNm'] = movie_data['movieInfoResult']['movieInfo']['audits'][0]['watchGradeNm']
        result['showTm'] = movie_data['movieInfoResult']['movieInfo']['showTm']  # 상영시간
        result['openDt'] = movie_data['movieInfoResult']['movieInfo']['openDt']  # 개봉연도
        if movie_data['movieInfoResult']['movieInfo']['genres']:  # 장르
            result['movie_data'] = movie_data['movieInfoResult']['movieInfo']['genres'][0]['genreNm']
        if movie_data['movieInfoResult']['movieInfo']['directors']:  # 감독명
            result['directors'] = movie_data['movieInfoResult']['movieInfo']['directors'][0]['peopleNm']
        writer.writerow(result)
