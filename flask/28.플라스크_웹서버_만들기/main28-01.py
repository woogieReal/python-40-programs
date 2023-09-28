"""
flask로 간단한 웹서버 만들고 구동하는 코드 만들기
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

def main():
    # flask 웹서버를 실행
    app.run(debug=True, port=3000)

# 코드를 직접 실행 시 main() 함수를 실행
# __name__은 코드를 직접 실행 시 이름이 __main__이다
if __name__ == '__main__':
    main()