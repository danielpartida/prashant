from run import app

@app.route('/')
@app.route('/index')
def hello_world():
    return 'Hello, Prashant!'