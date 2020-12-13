from pymongo import MongoClient
from flask import Flask, render_template, session, request, redirect
from flask import Flask, jsonify, render_template, url_for
from flask_charts import GoogleCharts, Chart, ChartData
from flask_googlecharts.utils import prep_data
import json
from random import randint
import pandas as pd #import pandas

import datetime

import matplotlib.pyplot as plt

app = Flask(__name__)
charts = GoogleCharts(app)
myclient = MongoClient(
    "mongodb+srv://binay_99:Watson%4099@bdat1004cluster.n5kgy.mongodb.net/test?authSource=admin&replicaSet=atlas-fxanzx-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
mydb = myclient["Bank_Chrun"]
mycol = mydb["Chrun"]
Gender_Male = mycol.find({"Gender": "M"}).count()
Gender_Female = mycol.find({"Gender": "F"}).count()
c_grad = mycol.find({"Education_Level": "Graduate"}).count()
c_hs = mycol.find({"Education_Level": "High School"}).count()
c_ue = mycol.find({"Education_Level": "Uneducated"}).count()
c_c = mycol.find({"Education_Level": "College"}).count()
c_pg = mycol.find({"Education_Level": "Post-Graduate"}).count()
c_Dc = mycol.find({"Education_Level": "Doctorate"}).count()

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/education")
def education():
    return render_template("education.html",c_grad = c_grad, c_hs = c_hs, c_ue =c_ue, c_c=c_c, c_pg = c_pg , c_Dc=c_Dc)

@app.route("/Credit")
def Credit():
    card_blue = mycol.find({"Card_Category": "Blue"}).count()
    card_Gold = mycol.find({"Card_Category": "Gold"}).count()
    card_Platinium = mycol.find({"Card_Category": "Platinium"}).count()
    card_Silver = mycol.find({"Card_Category": "Silver"}).count()
    return render_template("Credit.html",card_blue = card_blue, card_Gold = card_Gold, card_Platinium = card_Platinium, card_Silver = card_Silver)

@app.route('/Income')
def Income():
    income_cat = mycol.distinct("Income_Category")
    return render_template("income.html",income_cat = income_cat)

@app.route("/")
def index():
    customer_list = mycol.find()
    total_trans = mycol.find({"Total _Amount _Of_Transactions":42})
    sum_trans = sum(total_trans)
    return render_template('index.html', customer_list = customer_list,male_count = Gender_Male,female_count = Gender_Female,sum_trans=sum_trans)

if __name__ == "__main__":
    app.run(debug=True)