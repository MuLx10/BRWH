#!flask/bin/python


import os,json
import simplejson
import traceback
from flask import Flask, request, render_template, redirect, url_for, send_from_directory, make_response
from flask_bootstrap import Bootstrap
from collections import Counter
import pandas as pd
import numpy as np
from BRWH import get_rank
from BRWH import user_repos_company
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['UPLOAD_FOLDER'] = 'data/'
app.config['THUMBNAIL_FOLDER'] = 'data/thumbnail/'
# app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

bootstrap = Bootstrap(app)



@app.route('/', methods= ['GET','POST'])
def search():
    data = get_rank.get_rank()
    if request.method == 'POST':
        print(request.form)
        val = request.form["id"]
        newdata = [ x for x in data if val in x["name"]]
        return render_template('index.html', results = newdata)
    return render_template('index.html', results = data)
    
@app.route('/recomend', methods= ['GET','POST'])
def recomend():
    data = user_repos_company.get_recomend()
    return render_template('recomend.html', results = data)
    
@app.route('/tree', methods= ['GET','POST'])
def tree():
    return render_template('treeindex.html')
   
@app.route('/table', methods= ['GET','POST'])
def table():
    f = open('data/stats.json','r')
    stats = json.load(f)
    f.close()
    print(stats[:10])
    cc = ["row header green", "row header red", "row header blue"]
    data = []
    for i in range(0,len(stats),10):
        data.append({"item":stats[i:i+10], "color":cc[int((i/10)%3)]})
    return render_template('tableindex.html', data= data)

@app.route('/chartL', methods= ['GET','POST'])
def chartL():
    f = open('data/language.json','r')
    data = json.load(f)
    f.close()
    return render_template('chartindexL.html', results = data)    
 
@app.route('/chartLc', methods= ['GET','POST'])
def chartLc():
    f = open('data/license.json','r')
    data = json.load(f)
    f.close()
    return render_template('chartindexLc.html', results = data)  
    
if __name__ == '__main__':
    app.run(debug=True)
