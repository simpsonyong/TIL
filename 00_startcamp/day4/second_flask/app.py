from flask import Flask, render_template, request
from iexfinance.stocks import Stock
import random
# html로 끌기 위해서 render템플릿 꺼내고 flask를 쓰기
# 위해서 그다음 폴더 밑에 templates 폴더 만들기
# 그냥 flask가 이렇게 작동하니 그냥 알아만 둘것
import datetime
import requests
import json
from art import *

app = Flask(__name__)


@app.route('/')  # '/' 의미: 아무 말도 없을 때라는 특별한 의미
def index():
    return render_template('index.html')


@app.route('/send')
def send():
    return render_template('send.html')


# @app.route('/add')
# def add():
#     # pass # add.html 숫자 2개 받는다

#     return render_template('add.html')

@app.route('/art')
def add():
    # pass # add.html 숫자 2개 받는다

    return render_template('art.html')

# 글꼴 아트버전


@app.route('/result')
def result():
    # 이 안에 있는거 전부 다 꺼낼게 *:와일드 카드)
    input_text = request.args.get('input_text')
    font = request.args.get('font')
    result = text2art(input_text, font=font)
    return render_template('result.html', result=result)

# 덧셈버전
# @app.route('/result')
# def result():
#     # pass # result.html -> input_data 의 합 더한결과
#     add_data1 = request.args.get('msg1')
#     add_data2 = request.args.get('msg2')
#     result_data = int(add_data1)+int(add_data2)
#     return render_template(
#         'result.html',
#         r_data=result_data
#     )


# @app.route('/receive', methods=['POST']) => 취급주의
# data = request.form.get('msg')= args=>폼으로 바뀜
# form 형식( 사용자가 입력한 값이 url에 안적혀있음)

@app.route('/receive', methods=['POST'])
def receive():
    token = 'pk_63c229409ff14b67a6cc81e38927f1c4'
    data = request.form.get('msg')
    stock = Stock(data, token=token).get_quote()
    company_name = stock['companyName']
    latest_price = stock['iexRealtimePrice']
    url = 'http://api.manana.kr/exchange/rate/KRW/JPY,USD,KRW.json'
    response = requests.get(url).text
    KR_data = int(''.join(response[-9:-5]+response[-4:-2]))/100
    KR_value = int(latest_price) * KR_data
    # data = request.args.get('msg') 아까 data 변수를 설정하지 않아서 오류가 뜸
    # request.args.get('msg') msg라는 name을 가진 데이터를 꺼낸다
    # requests(또 다른외장함수 기능)와 request(라우트를 통해 receive로 받은 신호가 담겨진 박스/외장함수
    #  import 해야함) 주의할것
    Korea_price = latest_price
    return render_template(
        'receive.html',
        c_name=company_name,
        l_price=latest_price,
        Kr=str(KR_value),
        Kr_d=KR_data
    )


@app.route('/dday')  # 라우트는 길을 뚫어준다는 의미
def dday():
    today = datetime.datetime.now()
    end_date = datetime.datetime(2019, 11, 29)
    left = end_date - today
    # return f'SSAFY 2기 1학기 종료일까지 {left.days} 일 남았습니다.'
    return render_template('dday.html', left_days=left.days)


@app.route('/boxoffice')  # 박스오피스라는 html이라는 것을 만들거고 일단 templates 만들자
def boxoffice():
    top_5 = [
        '스파이더맨 파 프롬 홈',
        '알라딘',
        '토이스토리4',
        '존윅3',
        '라이온킹',
    ]

    return render_template('boxoffice.html', movies=top_5)

if __name__ == "__main__":
    app.run(debug=True)
