import time

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    print("i recive request")
    time.sleep(5)
    print("i ready answer to request")
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, threaded=False)

