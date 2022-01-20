import json

from flask import Flask, redirect, url_for, render_template, request, session, jsonify
import requests
import random

from interact_with_DB import interact_db

app = Flask(__name__)
app.secret_key = '123'


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
    # db
    return render_template('assignment8.html', my_profile={'name': 'avia', 'second': 'dolev'},
                           university='BGU', fav_books=['harry potter', 'me before you', 'jack richer'],
                           hobbies=('music', 'sport', 'friends'))


@app.route('/assignment9', methods=['GET', 'POST'])
def ass9_func():
    users = [
        {'firstname': 'avia', 'secondname': 'dolev', 'age': '26'},
        {'firstname': 'michal', 'secondname': 'lee', 'age': '22'},
        {'firstname': 'sharon', 'secondname': 'cohen', 'age': '25'},
        {'firstname': 'tal', 'secondname': 'fun', 'age': '33'},
        {'firstname': 'mor', 'secondname': 'gil', 'age': '30'},
    ]
    if request.method == 'GET':
        if 'firstname' in request.args:
            firstname = request.args['firstname']
            secondname = request.args['secondname']
            age = request.args['age']
            return render_template('assignment9.html', fn=firstname, sn=secondname, ag=age, users=users)
        return render_template('assignment9.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # db
        session['username'] = username
        return render_template('assignment9.html', username=username)


@app.route('/logout')
def logout_func():
    session['username'] = ''
    return render_template('assignment9.html')


@app.route('/users_ex11')
def users_ex11_func():
    query = "SELECT * FROM users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('users_ex11.html', users=query_result)


def get_users(num):
    users = []
    for i in range(num):
        random_n = random.randint(1, 100)
        res = requests.get(f'https://reqres.in/api/users/{num}{random_n}')
        res = res.json()
        users.append(res)
    return users


@app.route('/outer_source_ex11')
def outer_source_ex11_func():
        num = 3
        if "number" in request.args:
            num = int(request.args['number'])
        users = get_users(num)
        return render_template('outer_source_ex11.html', users=users)


@app.route('/assignment12', defaults={'USER_ID': 1})
@app.route('/assignment12/<int:USER_ID>')
def get_users_func(USER_ID):
    query = 'select * from users where id="%s";' % USER_ID
    users = interact_db(query=query, query_type='fetch')
    if len(users) == 0:
        return_dict = {
            'status': 'failed',
            'massage': 'User not found'
        }
    else:
        return_dict = {
            'status': 'success',
            'id': users[0].id,
            'name': users[0].name,
            'age': users[0].age,
        }
    return jsonify(return_dict)


if __name__ == '__main__':
    app.run(debug=True)
