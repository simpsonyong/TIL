import requests
import json
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'

response = requests.get(url).text

data = json.loads(response)  # print(type(data), data)

print(data['bnusNo'])

real_numbers = []

for key, value in data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)

print(real_numbers)

d = {1: 'aaa', 2: 'xv', 3: 12312323, 4: 555}
for key in d:  # 기본적으로 키 값만 튀어나오게 되어있다.
    print(key)

'''
{
"totSellamnt":81961886000,      # 총 판매금액
"returnValue":"success",        # 응답가능여부
"drwNoDate":"2019-07-06",       # 추첨일
"firstWinamnt":2240409000,      # 1등 금액
"drwtNo6":39,                   # no4
"drwtNo4":34,                   # no6
"firstPrzwnerCo":9,             # 1등 당첨자수
"drwtNo5":37,                   # no5
"bnusNo":12,                    # 보너스
"firstAccumamnt":20163681000,   # 이번회차 누적금
"drwNo":866,                    # 회차
"drwtNo2":15,                   # no2
"drwtNo3":29,                   # no3
"drwtNo1":9                     # no1
}
'''
