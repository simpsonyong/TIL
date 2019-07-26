## 네이버 영화 검색 API - movie_naver.py

### 사용 파일 

- movie.csv

- movie_naver.py

  ```
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
  
  ```

- naver_API.py

  ```
  from decouple import config
  import requests
  
  
  def send_naver_movie(movie_name):
      naver_client_id = config('NAVER_CLIENT_ID')
      naver_client_secret = config('NAVER_CLIENT_SECRET')
      BASE_URL = 'https://openapi.naver.com/v1/search/movie.json'
      URL = BASE_URL + '?query=' + movie_name
  
      # headers has to be a dict
      headers = {
          'X-Naver-Client-Id': naver_client_id,
          'X-Naver-Client-Secret': naver_client_secret,
      }
      # how to request : headers에 hearders 딕셔너리를 넘긴다
      # return 값이 없으므로 response에 담는다
      response = requests.get(URL, headers=headers)
      return response.json()
  
  ```

### 결과 파일 

- movie_naver.csv

## 영화 포스터 이미지 저장 - movie_image.py

### 사용파일

- movie_image.py

```
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
```