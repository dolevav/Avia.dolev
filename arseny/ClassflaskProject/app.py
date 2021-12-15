from flask import Flask, redirect, url_for, render_template
from flask import render_template
from flask import request
from flask import session

app = Flask(__name__)
app.secret_key= '123'


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/home_page')
@app.route('/home')
@app.route('/')
def home_func():
    # return render_template
    found=true
    if found:
        return render_template('index.html', name='Avia')
    else:
        return render_template('index.html')

@app.route('/about')
def about_func():
    # return render_template
    name = 'Avia'
    second_name = 'dolev'
    uni = 'BGU'
    return render_template('about.html',
                           profile={'name':'avia', 'second_name':'dolev'},
                            university='BGU',
                            degress=['Bsc, Msc'],
                            hobbies=('art', 'music'))

@app.route('/index')
def index_func():
    return ''

@app.route('/catalog')
def catalog_func():
    if 'user_inside' in session:
         if session['user_inside']:
          print('user inside')
    if 'product' in request.args:
        product = request.args['product']
        size = request.args['size']
        return render_template('catalog.html', p_name=product, s_name=size)
    return render_template('catalog.html')

@app.routh('/logout')
def logout_func():
    session['username']= ''
    return render_template('index.html')


@app.route('login', methods= ['GET', 'POST'])
def login_func():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        # DB
        found = True
        if found:
            session['username'] = username
            return redirect(url_for('home_func'))
        else:
            return render_template('login.html')

if __name__ == '__main__':
    app.run()
