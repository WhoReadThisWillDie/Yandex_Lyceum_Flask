from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


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


class LoginForm(FlaskForm):
    id = StringField('Id астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    cap_id = StringField('Id капитана', validators=[DataRequired()])
    cap_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/login')
def login_form():
    form = LoginForm()
    return render_template('login_form.html', form=form)


@app.route('/distribution')
def distribution():
    return render_template('distribution.html')


@app.route('/table/<gender>/<int:age>')
def table(gender, age: int):
    return render_template('table.html', gender=gender, age=age)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
