from flask import Flask, url_for, request, render_template

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


@app.route('/choice/<planet_name>')
def choice(planet_name):
    list_ = []
    if planet_name == 'Марс':
        list_ = ['Эта планета близка к Земле', 'На ней есть вода и атмосфера', 'Наконец, она просто красива!']
    elif planet_name == 'Земля':
        list_ = ['Шучу, ха-ха', 'Ну а что, зачем нам куда-то улетать?', 'Нам и здесь отлично живётся!']
    elif planet_name == 'Венера':
        list_ = ['Эта планета близка к Земле и схожа с ней по размеру', 'Лететь ближе, чем до Марса',
                 'Мы можем создать там условия, подходящие для жизни человека']
    return f'''<!doctype html>
                    <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
                            <title>Варианты выбора</title>
                        </head>
                        <body>
                            <h1>Мое предложение: {planet_name}</h1>
                            <div class='alert alert-primary' role='alert'>
                                {list_[0]}
                            </div>
                            <div class='alert alert-warning' role='alert'>
                                {list_[1]}
                            </div>
                            <div class='alert alert-success' role='alert'>
                                {list_[2]}
                            </div>
                        </body>
                    </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style_1.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>На участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <label for="email" ></label>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="educationSelect">Какое у Вас образование?</label>
                                        <select class="form-select" id="educationSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                     <div class="form-group">
                                        <label for="form-check">Какие у Вас есть профессии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="engineer_1" value="enigineer_1">
                                          <label class="form-check-label" for="engineer_1">
                                            Инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="engineer_2" value="engineer_2">
                                          <label class="form-check-label" for="engineer_2">
                                            Инженер-строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="pilot" value="pilot">
                                          <label class="form-check-label" for="pilot">
                                            Пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="meteo" value="meteo">
                                          <label class="form-check-label" for="meteo">
                                            Метеоролог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="engineer_3" value="engineer_3">
                                          <label class="form-check-label" for="engineer_3">
                                            Инженер по жизнеобеспечению
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="engineer_4" value="engineer_4">
                                          <label class="form-check-label" for="engineer_4">
                                            Инженер по радиационной защите
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="doctor" value="doctor">
                                          <label class="form-check-label" for="doctor">
                                            Врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="biologist" value="biologist">
                                          <label class="form-check-label" for="biologist">
                                            Экзобиолог
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male">
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form['profession'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form['accept'])
        return "Анкета отправлена"


@app.route('/load_photo', methods=['GET', 'POST'])
def load_photo():
    file = url_for('static', filename='img/1.png')
    if request.method == 'POST':
        f = request.files['file']
        with open(f'static/img/{f.filename}', 'wb') as file:
            file.write(f.read())
        file = url_for('static', filename=f'img/{f.filename}')
    return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet" 
                                href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity=
                                "sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" 
                                href="{url_for('static', filename='css/style.css')}" />
                                <title>Загрузка файла</title>
                              </head>
                              <body>
                                <h1 align="center">Загрузка фотографии</h1>
                                <h3 align="center">для участия в миссии</h3>
                                <div>
                                    <form class="login_form" method="post" enctype="multipart/form-data">
                                       <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <img src="{file}" alt="Фото">
                                        <br>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                 href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                                 integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                                 crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" >
                                <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" 
                                integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" 
                                crossorigin="anonymous"></script>
                                <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" 
                                integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" 
                                crossorigin="anonymous"></script>
                                <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" 
                                integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" 
                                crossorigin="anonymous"></script>
                                <title>Пейзажи Марса</title>
                              </head>
                              <body>
                                <h1 align="center">Пейзажи Марса</h1>
                                <div align="center" id="carousel-example-generic" class="carousel slide" 
                                data-ride="carousel">
                                  <ol class="carousel-indicators">
                                    <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
                                    <li data-target="#carousel-example-generic" data-slide-to="1"></li>
                                    <li data-target="#carousel-example-generic" data-slide-to="2"></li>
                                  </ol>
                                  <div class="carousel-inner" role="listbox">
                                    <div class="carousel-item active">
                                      <img src="/static/img/mars_1.png" alt="First slide">
                                    </div>
                                    <div class="carousel-item">
                                      <img src="/static/img/mars_2.png" alt="Second slide">
                                    </div>
                                    <div class="carousel-item">
                                      <img src="/static/img/mars_3.png" alt="Third slide">
                                    </div>
                                  </div>
                                  <a class="left carousel-control" href="#carousel" role="button" data-slide="prev">
                                    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                                    <span class="sr-only">Previous</span>
                                  </a>
                                  <a class="right carousel-control" href="#carousel" role="button" data-slide="next">
                                    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                                    <span class="sr-only">Next</span>
                                  </a>
                                </div>
                            </div>
                              </body>
                            </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
