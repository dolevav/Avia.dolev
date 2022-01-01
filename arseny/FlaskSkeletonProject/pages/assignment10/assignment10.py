from flask import Blueprint, render_template, request, redirect, Flask

from app import app
from interact_with_DB import interact_db

# assignment10 blueprint definition
assignment10 = Blueprint('assignment10', __name__, static_folder='static',
                  template_folder='templates')


# Routes
@assignment10.route('/assignment10')
def assignment10_func():
    query = 'select * from users'
    users = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=users)


@app.route('/insert_user', methods=['POST'])
def insert_user_func():
    # get the data
    name = request.form['name']
    age = request.form['age']
    password = request.form['password']
    # insert to DB
    query = "INSERT INTO users(name, age, password) VALUES ('%s', '%s', '%s')" % (name, age, password)
    interact_db(query=query, query_type='commit')
    # come back to assignment10
    return redirect('/assignment10')

@app.route('/update_user', methods=['POST'])
def update_user_func():
    # get the data
    name = request.form['name']
    age = request.form['age']
    password = request.form['password']
    # update to DB
    user_id = request.form['id']
    query = "UPDATE users SET name='%s', age='%s', password='%s' WHERE id='%s';" % (name, age, password, user_id)
    interact_db(query=query, query_type='commit')
    # come back to assignment10
    return redirect('/assignment10')

@app.route('/delete_user', methods=['POST'])
def delete_user_func():
    user_id = request.form['id']
    query = "DELETE FROM users WHERE id='%s';" % user_id
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')