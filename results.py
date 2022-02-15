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


@app.route('/promotion_image')
def promotion_image():
    list_ = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
             'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    url_pic = url_for('static', filename='img/mars.png')
    url_style = url_for('static', filename='css/style.css')

    return f'''<!doctype html>
                    <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_style}" />
                            <title>Колонизация</title>
                        </head>
                        <body>
                            <h1>Жди нас, Марс!<h1> 
                            <img src = "{url_pic}">
                            <div class="alert alert-dark" role="alert">
                                {list_[0]}
                            </div> 
                            <div class="alert alert-success" role="alert">
                                {list_[1]}
                            </div>
                            <div class="alert alert-secondary" role="alert">
                                {list_[2]}
                            </div>
                            <div class="alert alert-warning" role="alert">
                                {list_[3]}
                            </div>
                            <div class="alert alert-danger" role="alert">
                                {list_[4]}
                            </div>
                         </body>
                    </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                    <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
                            <title>Результаты</title>
                        </head>
                        <body>
                            <h1>Результаты отбора на участие в миссии</h1>
                            <h2>Претендент: {nickname}</h2>
                            <div class='alert alert-primary' role='alert'>
                                Поздравляем! Вы прошли {level} этап отбора!
                            </div>
                            <div class='alert alert-success' role='alert'>
                                Ваш рейтинг составляет {rating}!
                            </div>
                            <div class='alert alert-warning' role='alert'>
                                Желаем удачи!
                            </div>
                        </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
