from flask import Flask, render_template

app = Flask(__name__)

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
