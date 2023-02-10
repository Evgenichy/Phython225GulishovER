from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g
import sqlite3
import os
from PDataBase import PDataBase

DATABASE = '/tmp/flask.db'
DEBUG = True
SECRET_KEY = 'ee97969d74cf574e054895bea0cb8268965da55d'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'pshp.db')))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route('/index')
def index():
    db = get_db()
    dbase = PDataBase(db)

    return render_template('index.html', title='Главная', menu=dbase.get_menu(), goods=dbase.get_goods_announce())


@app.route('/add_goods', methods=['POST', 'GET'])
def add_goods():
    db = get_db()
    dbase = PDataBase(db)

    if request.method == 'POST':
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.add_goods(request.form['name'], request.form['post'], request.form['url'])
            if not res:
                flash('Ошибка добавления товара', category='error')
            else:
                flash('Товар добавлен успешно', category='success')
        else:
            flash('Ошибка добавления товара', category='error')

    return render_template('add_goods.html', menu=dbase.get_menu(), title='Добавление товара')


@app.route('/about')
def about():
    db = get_db()
    dbase = PDataBase(db)

    return render_template('about.html', title='О нас', menu=dbase.get_menu())


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = PDataBase(db)

    return render_template('page404.html', title='Страница не найдена', menu=dbase.get_menu()), 404


if __name__ == '__main__':
    app.run(debug=True)
