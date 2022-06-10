from flask import Flask

app = Flask(__name__)
# server = app.server


@app.route('/')
def hello_world():
    return 'Hello, Prashant!'

if __name__ == "__main__":
     app.run(host="0.0.0.0")