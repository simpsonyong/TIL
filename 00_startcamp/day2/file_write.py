restaurants = {
    '양자강': '02-557-4211',
    '김밥카페': '02-553-3181',
    '순남시래기': '02-508-0887'
}

with open('restaurant.csv', 'w', encoding = 'utf-8') as f: # w는 코드 실행할수록 계속 쓰기가 되어 덮어쓰기 된다.
    f.write('식당이름, 전화번호\n')
    for name, phone in restaurants.items():
        f.write(f'{name}, {phone}\n')
