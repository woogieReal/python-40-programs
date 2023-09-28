"""
flask를 이용하여 html 파일을 서버로 만들어 보여주는 코드 만들기
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/map')
def map():
    # /map에 접속하면 [templates] 폴더의 uni_map.html 파일을 응답
    return render_template("uni_map.html")

def main():
    # flask 웹서버를 실행
    app.run(debug=True, port=3000)

# 코드를 직접 실행 시 main() 함수를 실행
# __name__은 코드를 직접 실행 시 이름이 __main__이다
if __name__ == '__main__':
    main()