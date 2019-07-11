import requests
import json
url = 'http://api.manana.kr/exchange/rate/KRW/JPY,USD,KRW.json'
response = requests.get(url).text

response = json.loads(response)
print(response[2]['rate'])
# 내가 한 것 json 제외하고 함
# KR_data = int(''.join(response[-9:-5]+response[-4:-2]))/100 => 1172.55로 가져온다
# 개선법1: float함수를 이용하면 그냥 해결할 수 있다. 몰랐음;;
# 개선법2: json 외장함수를 이용하여 딕셔너리에서 값을 가져온다
# import json
# json.loads(requests.get(url).text)(제이슨을 통해서 전부 텍스트화 되어있는 값을 
# 리스트와 딕셔너리로 바꾼다)
# 딕셔너리 가져오기 response[2]['rate']
# response[2]의 딕셔너리에서 => 'rate'키 값을 가지고 있는 value값을 찾는다
