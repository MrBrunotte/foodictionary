#----------------#
# DEPENDENCIES
#----------------#
import os
import pymongo
import math  # remove?
import random  # remove?
from flask import Flask, render_template, redirect, request, url_for, request, session, g, abort, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

#-----------------------------#
# CONNECT TO MONGODB DATABASE
#-----------------------------#

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'foodictionary'
# app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.config['MONGO_URI'] = 'mongodb+srv://mrbrunotte:mrUSERbrunotte@foodictionary-gckbp.mongodb.net/foodictionary?retryWrites=true&w=majority'
app.secret_key = '9893869affbf35907d0e7f0f20a72bc9'
# Add secret key:   app.secret_key = os.getenv('SECRET', 'randomstring123')

mongo = PyMongo(app)

#-----------#
# VARIABLES
#-----------#

userDB = mongo.db.users


#----------#
# HOMEPAGE
#----------#

# base.html and root route
@app.route('/')
@app.route('/home')
def home():
    # returns everything from tasks in task_manager DB
    return render_template('base.html')

#-----------------------------#
# USER LOGIN AND REGISTRATION
#-----------------------------#


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/signup', methods=['POST'])
def signup():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)
    author_name = request.form.get('author_name')
    username = request.form.get('username').lower()
    password = generate_password_hash(request.form.get('password'))
    session['username'] = username
    user = userDB.find_one({'username': username})

    if user is None:
        userDB.insert_one({
            'author_name': author_name,
            'username': username,
            'password': password
        })
        session['logged_in'] = True
        flash('Welcome to FOODictionary ' + author_name + '!')
        return login()
    else:
        session['logged_in'] = False
        flash('Username already exists, please try again.')
    return register()


@app.route('/login')
def login():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('base.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username'].lower()
    password = request.form['password']
    session['username'] = username
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)
    user = userDB.find_one({'username': username})

    if not user:
        session['logged_in'] = False
        flash('User ' + session['username'] +
              ' is not registered. Please try again.')
        return signin()
    elif not check_password_hash(user['password'], password):
        session['logged_in'] = False
        flash('Wrong Password, please try again.')
        return signin()
    else:
        session['logged_in'] = True
        flash('Welcome back ' + user['author_name'].capitalize() + '!')
        return render_template('base.html')


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return render_template('base.html', page_title='Logout from FOODictionary')

#-------------#
# Error Pages
#-------------#

# @app.errorhandler(404)
# def page_not_found(error):
#    return render_template('404.html',recipeCategory=recipeCategory.find(), page=1, page_title='404 Error Page, FOODictionary'), 404


# @app.errorhandler(500)
# def something_wrong(error):
    # return render_template('500.html',recipeCategory=recipeCategory.find(), page=1, page_title='500 Error Page, FOODictionary'), 500


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)  # change to False when finished!
