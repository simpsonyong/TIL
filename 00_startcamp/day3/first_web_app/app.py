# import flask                    # 필통을 꺼낸다(연필 칼 다 가능)
# random.choice([1, 2, 3, 4, 5])  # 꺼낸 필통에서 연필 사용한다

# from random import choice       #필통에서 연필만 꺼낸다(칼 지우개 불가)
# choice([1, 2, 3, 4, 5], 2)      #연필을 사용한다
from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')  # 라우트 이게 붙으면
def index():
    return render_template('index.html')  # 이 일을 해라


@app.route('/pick_lotto')  # 라우트 이게 붙으면
def pick_lotto():
    numbers = range(1, 46)
    lucky = random.sample(numbers, 6)
    # index든 hi이든 상관없음, 하지만 /백슬래시 다음 이름으로 통상 붙임
    return str(lucky)


# @app.route('/get_lotto/<int:num>')  # 라우트 이게 붙으면
# def get_lotto_1():
#     # 1회차 로또정보


@app.route('/hello/<name>')  # 라우트 이게 붙으면
def hello(name):
    return f'hi, {name}'


@app.route('/pick_lunch/<int:count>')  # 라우트 이게 붙으면
def pick_lunch(count):
    menus = [
        '짜장면',
        '짬뽕',
        '탕수육',
        '볶음밥',
        '사천탕면',
        '쟁반짜장'
    ]
    picks = random.sample(menus, count)
    return str(picks)


@app.route('/cube/<int:num>')  # 들어온 숫자의 세제곱
def cube(num):
    cube_num = num ** 3
    return str(cube_num)


if __name__ == '__main__':
    app.run(debug=True)
