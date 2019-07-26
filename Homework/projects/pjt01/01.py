import requests
import time
import csv
from datetime import datetime, timedelta
from decouple import config
with open('boxoffice.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['movieCd', 'movieNm', 'audiAcc']
    csv.DictWriter(f, fieldnames=fieldnames).writeheader()

    API_KEY = config('API_KEY')
    movie_codes = []
    URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={API_KEY}&weekGb=0&targetDt='

    for i in range(0, 50):
        d = datetime(2019, 7, 13) - timedelta(weeks=i)
        targetDt = d.strftime("%Y%m%d")

        URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={API_KEY}&weekGb=0&targetDt={targetDt}'

        data = requests.get(URL).json()

        result = {}

        for movie in data.get('boxOfficeResult').get('weeklyBoxOfficeList'):
            if movie.get('movieCd') not in movie_codes:
                movie_codes.append(movie.get('movieCd'))
                result['movieCd'] = movie.get('movieCd')
                result['movieNm'] = movie.get('movieNm')
                result['audiAcc'] = movie.get('audiAcc')
                writer.writerow(result)
            else:
                pass
