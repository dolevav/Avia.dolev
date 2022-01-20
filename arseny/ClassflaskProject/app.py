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

@app.route('/logout')
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


@app.route('/users')
def users_func():
    users = interact_db(query...)
    return render_template('users.html', users= )

@app.route('/insert_user', methods=['POST'])
def insert_user_func():
    # get the data
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    # insert to DB
    query = "INSERT INTO users(name, email, password) VALUES ('%s', '%s', '%s')" % (name, email, password)
    ineract_db(query=query, query_type='commit')

    # come back to users
    return redirect('/users')

@app.route('/delete_users', methods=['POST'])
def delete_users_func():
    user_id = request.form['id']
    query = "DELETE FROM users WHERE id='%s';" % user_id
    insert_db(query=query,query_type='commit')
    return redirect('users.html')

@app.route('request_For_fronted')
def fronted_func():
    return render_template('request_For_fronted.html')

def get_pockemons(num):
    pokemons = []
    for i in range(num):
        random_n = random.randint(1, 100)
        res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{random_n}')
        # res = requests.get('https://pokeapi.co/api/v2/pokemon/%s' % random_n)
        res = res.json()
        pokemons.append(res)
    return pokemons

@app.route('request_For_backend')
def fronted_func():
    num = 3
    if "number" in request.args:
         num = int(request.args['number'])
    pockemons = get_pockemons(num)
    return render_template('req_backend.html', pockemons=pockemons)
    return render_template('request_For_backend.html')

@app.route('/assignment12', defaults={'USER_ID': -1})
@app.route('/assignment12/<int:USER_ID>')
def get_users_func(USER_ID):
    if USER_ID == -1:
        return_dict = {}
        query = 'select * from users;'
        users = interact_db(query=query, query_type='fetch')
        for user in users:
            return_dict[f'user_{USER_ID}'] = {
                'status': 'success',
                'id': users.id,
                'name': users.name,
                'age': users.age,
            }
    else:
        query = 'select * from users where id=%s;' % USER_ID
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
    app.run()
