from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')  # '/' 의미: 아무 말도 없을 때라는 특별한 의미
def login():
    return render_template('login.html')

# @app.route('/')
# def hello():
#     return 'Hello World!'

if __name__ == "__main__":
    app.run(debug=True)
