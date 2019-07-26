import requests
from datetime import datetime, timedelta
from decouple import config
import csv

director_reader = csv.DictReader(open('movie.csv', 'r', encoding='utf-8'))
director_names = []  # movie.csv에서 불러온 감독이름을 저장하기 위한 빈 리스트
for row in director_reader:
    director_names.append(row['directors'])


with open('director.csv', 'w', encoding='utf-8', newline='') as f:  # director.csv 생성
    fieldnames = ['peopleCd', 'peopleNm', 'filmoNames', 'repRoleNm']
    # 영화인 코드 , 영화인명 , 분야 , 필모리스트
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    API_KEY = config('API_KEY')
    URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={API_KEY}&peopleNm='

    for name in director_names:  # 감독명을 통한 조회
        result = {}
        if requests.get(URL + name).json()['peopleListResult']:
            director_data = requests.get(URL + name).json()['peopleListResult']['peopleList'][0]  # 감독명을 통한 주소로 director_data를 받음
            result['peopleCd'] = director_data['peopleCd']
            result['peopleNm'] = director_data['peopleNm']
            if director_data['filmoNames']:  # filmoNames이 없는 경우 오류 방지
                result['filmoNames'] = director_data['filmoNames']
            if director_data['repRoleNm']:   # repRoleNm이 없는 경우 오류 방지
                result['repRoleNm'] = director_data['repRoleNm']
            writer.writerow(result)
