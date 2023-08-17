from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Sample Secret'

class NamerForm(FlaskForm):
    name = StringField("Enter Your Name : ", validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    #return '<h1> Hello World!!</h1>'
    pizza = ['1','2',3,'4']
    return render_template('index.html', pizza=pizza)

@app.route('/user/<name>')
def user(name):
#    return '<h1>Hello {}!!!  </h1>'.format(name)
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash(f"Hi {name} Form submitted Successfully!!")
    return render_template('name.html',
                           name = name,
                           form = form)


if __name__=='__main__':
    app.run(debug=True)