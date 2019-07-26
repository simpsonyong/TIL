import requests
import csv
from decouple import config

with open('movie.csv', 'w', encoding='utf-8', newline='') as f:  # movie.csv 작성
    fieldnames = ['movieCd', 'movieNm', "movieNmEn", "movieNmOg", 'watchGradeNm', 'showTm', 'prdtYear', 'genres', 'directors']
    # 영화 대표코드 , 영화명(국문) , 영화명(영문) , 영화명(원문) , 관람등급 , 개봉연도 , 상영시간 , 장르 , 감독명
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    API_KEY = config('API_KEY')
    movie_codes = []

    with open('boxoffice.csv', 'r', encoding='utf-8') as f:  # boxoffice.csv를 불러옴
        for row in csv.DictReader(f):
            movie_codes.append(row['movieCd'])  # movieCd열을 movie_codes의 리스트에 저장

    for movie_code in movie_codes:
        URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={API_KEY}&movieCd={movie_code}'
        source = requests.get(URL).json()["movieInfoResult"]['movieInfo']
        result = {}  # CSV로 저장할 최종 딕셔너리 자료
        result['movieCd'] = source['movieCd']  # 대표코드
        result['movieNm'] = source['movieNm']  # 영화명(국문)
        result['movieNmEn'] = source['movieNmEn']  # 영화명(영문)
        if source['movieNmOg']:
            result['movieNmOg'] = source['movieNmOg']  # 영화명(원문)
        if source['audits']:  # 관람등급
            result['watchGradeNm'] = source['audits'][0]['watchGradeNm']
        result['showTm'] = source['showTm']  # 상영시간
        result['prdtYear'] = source['prdtYear']  # 개봉연도
        if source['genres']:  # 장르
            result['genres'] = source['genres'][0]['genreNm']
        if source['directors']:  # 감독명
            result['directors'] = source['directors'][0]['peopleNm']
        writer.writerow(result)
