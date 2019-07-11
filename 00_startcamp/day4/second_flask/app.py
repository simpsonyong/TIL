from flask import Flask, render_template
#html로 끌기 위해서 render템플릿 꺼내고 flask를 쓰기 
# 위해서 그다음 폴더 밑에 templates 폴더 만들기 
# 그냥 flask가 이렇게 작동하니 그냥 알아만 둘것
import datetime

app = Flask(__name__)


@app.route('/')#'/' 의미: 아무 말도 없을 때라는 특별한 의미
def index():
    return render_template('index.html')


@app.route('/dday')#라우트는 길을 뚫어준다는 의미
def dday():
    today = datetime.datetime.now()
    end_date = datetime.datetime(2019, 11, 29)
    left = end_date - today
    # return f'SSAFY 2기 1학기 종료일까지 {left.days} 일 남았습니다.'
    return render_template('dday.html', left_days=left.days)


@app.route('/boxoffice')#박스오피스라는 html이라는 것을 만들거고 일단 templates 만들자
def boxoffice():
    top_5 = [
        '스파이더맨 파 프롬 홈',
        '알라딘',
        '토이스토리4',
        '존윅3',
        '라이온킹',
    ]

    return render_template('boxoffice.html', movies=top_5)

if __name__=="__main__":
    app.run(debug=True)
