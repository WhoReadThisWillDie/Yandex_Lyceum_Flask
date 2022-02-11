from flask import Flask, url_for

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


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.png">
                    <div>Вот она какая, красная планета.</div>
                </body>
            </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
