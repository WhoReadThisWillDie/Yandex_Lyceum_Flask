from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/list_prof/<param>')
def list_prof(param):
    list_ = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
             'климталог', 'специалист по радиационной защите', 'астрогеолог', 'гляцеолог', 'инженер жизнеобеспечения',
             'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов']
    return render_template('list_prof.html', list=list_, param=param)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    surname = 'Watny'
    name = 'Mark'
    education = 'выше среднего'
    profession = 'штурман марсохода'
    gender = 'male'
    motivation = 'Всегда мечтал застрять на Марсе!'
    check = True
    return render_template('auto_answer.html', surname=surname, name=name, education=education, profession=profession,
                           gender=gender, motivation=motivation, check=check)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
