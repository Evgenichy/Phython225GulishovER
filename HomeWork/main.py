from flask import Flask, render_template, url_for

app = Flask(__name__)

menu = [
    {'name': 'Главная', 'url': 'index'},
    {'name': 'Магазин', 'url': 'shop'},
    {'name': 'Доставка', 'url': 'delivery'},
    {'name': 'О нас', 'url': 'about'},
    {'name': 'Обратная связь', 'url': 'contact'},
]


@app.route('/index')
@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', title='Главная', menu=menu)


@app.route('/shop')
def shop():
    print(url_for('shop'))
    return render_template('shop.html', title='Магазин', menu=menu)


@app.route('/delivery')
def delivery():
    print(url_for('delivery'))
    return render_template('delivery.html', title='Доставка', menu=menu)


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='О нас', menu=menu)


@app.route('/profile/<username>')
def profile(username):
    return f'Пользователь: {username}'


if __name__ == '__main__':
    app.run(debug=True)

