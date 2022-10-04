from datetime import datetime
import email
from operator import imod
from pyexpat import model
from statistics import mode
from flask import Flask,render_template,flash
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

        #user = {'fname':_fname,'lname':_lname, 'email':_email, 'password':_password}
        if(db.session.query(models.User).filter_by(email=_email).count() == 0):
            user = models.User(first_name = _fname, last_name = _lname, email = _email)
            user.set_password(_password)
            db.session.add(user)
            db.session.commit()
            return render_template('signUpSuccess.html', user = user)
        else:
            flash('Email {} is already exsists!'.format(_email))
            return render_template('signup.html', form = form)

    #return render_template('signup.html')
    return render_template('signup.html', form = form)
        
def show():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1',port='8080',debug=True)