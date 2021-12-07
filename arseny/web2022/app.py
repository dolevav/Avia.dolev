from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route("/home")
def home():
    return redirect(url_for('Login'))
@app.route("/Login")
def Login():
    return "good!! You are redirected to the Login Page"

@app.route('/redirectonly')
def hello():
    return redirect('/you_were_redirected Hello')

@app.route("/you_were_redirected Hello")
def redirected():
    return "you_were_redirected Hello"


if __name__ == '__main__':
    app.run()

