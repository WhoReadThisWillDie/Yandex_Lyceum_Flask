from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Миссия колонизация Марса'


@app.route('/index')
def index_1():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    list_ = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
             'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(list_)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
