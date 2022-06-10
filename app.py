from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    return "<h1>Welcome Prashant!</h1>"

    

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host="0.0.0.0")