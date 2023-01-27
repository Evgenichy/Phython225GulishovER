import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, session, redirect, abort

DATABASE = '/tmp/flask.db'
DEBUG = True
SECRET_KEY = '4k3jh525h3d4dd64dfg36g3bh3kh643j6h3k440d9fds7gsd9'


app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


menu = [
    {'name': 'Главная', 'url': 'index'},
    {'name': 'О нас', 'url': 'about'},
    {'name': 'Обратная связь', 'url': 'contact'}
]


@app.route('/index')
@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', title='Главная', menu=menu)


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='О нас', menu=menu)


@app.route('/profile/<int:username>')
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f'Пользователь: {username}'


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Отправленно успешно', category='succsess')
        else:
            flash('Ошибка отправки', category='error')
        # print(request.form['username'])
        # context = {
        #     'username': request.form['username'],
        #     'email': request.form['email'],
        #     'message': request.form['message'],
        # }
        # return render_template('contact.html', **context, title='Обратная связь', menu=menu)
    return render_template('contact.html', title='Обратная связь', menu=menu)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'evgeniy' and request.form['psw'] == '1357':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html', title='Авторизация', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
