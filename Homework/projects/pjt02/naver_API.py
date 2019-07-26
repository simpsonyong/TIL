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


""" def send_naver_movie_img(movie_name):
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
    return response.json()['items'][0]['image'] """
