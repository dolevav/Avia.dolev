from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!!'

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

@app.route('/cv')
def cv_func():
    return render_template('cv_exc8.html')

@app.route('/assignment8')
def ass8_func():
    #db
    return render_template('assignment8.html', my_profile={'name': 'avia', 'second': 'dolev'},
                           university='BGU', fav_books=['harry potter', 'me before you', 'jack richer'], hobbies=('music', 'sport', 'friends'))



if __name__ == '__main__':
    app.run(debug=True)

