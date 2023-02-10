from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g
import sqlite3
import os
from FDataBase import FDataBase

DATABASE = '/tmp/flask.db'
DEBUG = True
SECRET_KEY = 'ee97969d74cf574e054895bea0cb8268965da44b'


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
    {'name': 'Магазин', 'url': 'shop'},
    {'name': 'Доставка', 'url': 'delivery'},
    {'name': 'О нас', 'url': 'about'},
    {'name': 'Обратная связь', 'url': 'contact'},
]


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route('/index')
@app.route('/')
def index():
    db = get_db()
    dbase = FDataBase(db)

    return render_template('index.html', title='Главная', menu=dbase.get_menu(), posts=dbase.get_posts_anonce())


@app.route('/shop')
def shop():
    db = get_db()
    dbase = FDataBase(db)

    return render_template('shop.html', title='Магазин', menu=dbase.get_menu())


@app.route('/delivery')
def delivery():
    db = get_db()
    dbase = FDataBase(db)

    return render_template('delivery.html', title='Доставка', menu=dbase.get_menu())


@app.route('/add_post', methods=['POST', 'GET'])
def add_post():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == 'POST':
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.add_post(request.form['name'], request.form['post'], request.form['url'])
            if not res:
                flash('Ошибка добавления товара', category='error')
            else:
                flash('Товар добавлен успешно', category='success')
        else:
            flash('Ошибка добавления товара', category='error')

    return render_template('add_post.html', menu=dbase.get_menu(), title='Добавление товара')


@app.route('/post/<alias>')
def show_post(alias):
    db = get_db()
    dbase = FDataBase(db)
    title, post = dbase.get_post(alias)
    if not title:
        abort(404)

    return render_template('post.html',  menu=dbase.get_menu(), title=title, post=post)


@app.route('/about')
def about():
    db = get_db()
    dbase = FDataBase(db)

    return render_template('about.html', title='О нас', menu=dbase.get_menu())


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Товар добавлен успешно', category='success')
        else:
            flash('Ошибка добавления', category='error')
        # print(request.form)
        # context = {
        #     'username': request.form['username'],
        #     'email': request.form['email'],
        #     'message': request.form['message'],
        # }
        # return render_template('contact.html', **context, menu=menu)
    return render_template('contact.html', title='Обратная связь', menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)

    return render_template('page404.html', title='Страница не найдена', menu=dbase.get_menu()), 404


@app.route('/profile/<username>')
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f'Пользователь: {username}'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'evg' and request.form['psw'] == '123':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html', title='Авторизация', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
