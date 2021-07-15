from flask.helpers import flash
from flask.wrappers import Request
from swcf import app
from flask import render_template, redirect, request, url_for
from swcf.dao.indexDAO import *

@app.route("/", methods=['GET'])
def index():
    return render_template("layout.html")

@app.route("/sendPost", methods=['POST'])
def sendPost():
    print('masuk sini')
    name = request.form['name']
    email = request.form['email']
    issue = request.form['issue']
    content = request.form['fillContent']
    print(name, email, issue, content)
    hInsert = insertPost(name, email, issue, 'content')
    print(hInsert)
    if hInsert['flag'] == 'T':
        flash("Proses insert berhasil", 'success')
    else : 
        flash("Tidak dapat melakukan proses insert", 'error')
    
    return render_template("layout.html")