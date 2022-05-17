from flask import Flask, render_template, request, url_for

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "1234",
    database = "buy_sell_books"
)

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo.db'
app.config['SECRET_KEY'] = '3eae2639343d45cf56a6'

from web import routes