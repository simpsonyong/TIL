import requests
from decouple import config
import csv
import json
# 감독 찾을 때 먼저 기존movie.csv에서 감독이름을 찾아와야 하기에,불러오는 코드를 쳤습니다. 그리고 불러온 이름들을 담을 빈 리스트를 만들어
# for을 쓰기에 더 유용하게 만들었습니다.
director_names= []

f = open('movie.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

for line in rdr:
   director_names.append(line[9])

f.close()
# director_names 리스트의 0번째 값과, 1번째 값이 '분류명'과 ','이기에 순수히 감독 이름으로만 이루어진 리스트로 덮어씌웠습니다.
director_names = director_names[2:]
print(director_names)


API_KEY = config('API_KEY')

with open('director.csv', 'w', encoding = 'utf-8', newline='') as f:
   fieldnames = ['peopleCd', 'peopleNm', 'filmoNames', 'repRoleNm']
   writer = csv.DictWriter(f, fieldnames=fieldnames)
   writer.writeheader()

  # 계속 코드가 틀린줄 알고 고쳤는데.. URL이 2번과 달랐더라구요..URL을 수정해 director_names의 항목과 결합하도록 했습니다.
   URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={API_KEY}&peopleNm='

   result = {}

# 이후, 3번코드는 2번과 별 다를 게 없었습니다.
   for name in director_names:
       director_data = requests.get(URL + name).json()

       result['peopleCd'] = director_data['peopleListResult']['peopleList'][0]['peopleCd']
       result['peopleNm'] = director_data['peopleListResult']['peopleList'][0]['peopleNm']
     # filmoNames이 없는 경우가 있기에, if director_data['peopleListResult']['peopleList'][0]['filmoNames']:를 설정해서 있는 경우에만 찾도록 했습니다.
       if director_data['peopleListResult']['peopleList'][0]['filmoNames']:
           result['filmoNames'] = director_data['peopleListResult']['peopleList'][0]['filmoNames']
      # 마찬가지로 repRoleNm이 없는 경우가 있기에, if director_data['peopleListResult']['peopleList'][0]['repRoleNm']:를 설정해서 `True`인 경우에만 찾도록 했습니다.
       if director_data['peopleListResult']['peopleList'][0]['repRoleNm']:
           result['repRoleNm'] = director_data['peopleListResult']['peopleList'][0]['repRoleNm']

       writer.writerow(result)