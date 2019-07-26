import requests
import time
from datetime import datetime, timedelta
from decouple import config
import csv
import json

with open('director.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['peopleCd', 'peopleNm', 'filmoNames', 'repRoleNm']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    API_KEY = config('API_KEY')
    director_codes = []

    with open('movie.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        director_codes = []
        for row in reader:
            director_codes.append(row['directors'])

    for director_code in director_codes:
        URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={API_KEY}&peopleNm={movie_code}'
        director_data = requests.get(URL).json()
        result = []  # peopleCd를 CSV로 저장할 리스트 자료

        if len(director_data) == 1:
            result['movieCd'] = director_data["movieInfoResult"]['movieInfo']['movieCd']  # 대표코드
            result['movieNm'] = director_data['movieInfoResult']['movieInfo']['movieNm']  # 영화명(국문)
            result['movieNmEn'] = director_data['movieInfoResult']['movieInfo']['movieNmEn']  # 영화명(영문)
        else:
            director_data['movieInfoResult']['movieInfo']['movieNmOg']: