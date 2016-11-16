# --- --- -- --- --- --- #
# --- Import Modules --- #
# --- --- -- --- --- --- #

from flask import Flask, make_response, g, send_from_directory
from flask import render_template as render
from flask import url_for, request, redirect, flash, jsonify
from flask import session as login_session

import random, string, httplib2, json, logging
import os, sys, cgi, re, hmac, hashlib, smtplib, requests, datetime
from datetime import timedelta
from functools import wraps
from werkzeug.utils import secure_filename
from threading import Timer

from bson.objectid import ObjectId
import pymongo
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')

db = client['app-database']

collections = {
    'users': db.users
}


# --- --- -- --- --- #
# --- Setop Code --- #
# --- --- -- --- --- #

app = Flask(__name__)
app.secret_key = 'superkey'

current_dir = os.path.dirname(os.path.abspath(__file__))

def login_required(f):
    ''' Checks If User Is Logged In '''
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' in login_session:
            return f(*args, **kwargs)
        else:
            # flash('You are not allowed to access there')
            return redirect('/login')
    return decorated_function



# --- --- -- --- --- --- #
# --- Routes & Views --- #
# --- --- -- --- --- --- #

@app.route("/", methods=['GET'])
def welcomePage():
    if request.method == 'GET':
        return render('welcome.html')


@app.route("/error", methods=['GET'])
def errorPage():
    if request.method == 'GET':
        return render('')


@app.route("/login", methods=['GET', 'POST'])
def loginPage():
    if request.method == 'GET':
        return render('login.html')


@app.route("/signup", methods=['GET', 'POST'])
def signupPage():
    if request.method == 'GET':
        return render('signup.html')


# --- --- -- --- --- #
# --- Initialize --- #
# --- --- -- --- --- #

if __name__ == '__main__':
    app.debug = True
    app.run( host = '0.0.0.0' , port = 4000 )
