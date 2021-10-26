from flask import Flask, render_template, request, flash
from werkzeug.utils import redirect
import sqlite3
from sqlite3 import Error

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')


@app.route('/menu', methods=['GET', 'POST'])
def menu():
    if request.method == 'GET':
        return render_template('menuPlatos.html')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')