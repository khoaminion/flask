from datetime import datetime
import email
from operator import imod
from flask import Flask,render_template
from flask import request
from forms import SignUpForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Khoaminion Flask web app'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)
import models


@app.route('/')
def main():
    todolist=[
        {
            'name': 'Buy milk',
            'description': 'Buy 2 liters of milk in Coopmart.'
        },
        {
            'name': 'Get money',
            'description': 'Get 500k from ATM'
        }
    ]
    return render_template('index.html',todolist = todolist)


@app.route('/signup', methods=['GET','POST'])
def showSignup():
    form = SignUpForm()
    if  form.validate_on_submit():
        _fname = form.inputFirstName.data
        _lname = form.inputLastName.data
        _email = form.inputEmail.data
        _password = form.inputPassword.data

        user = {'fname':_fname,'lname':_lname, 'email':_email, 'password':_password}
        return render_template('signUpSuccess.html', user = user)
        
    #return render_template('signup.html')
    return render_template('signup.html', form = form)
        
def show():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1',port='8080',debug=True)