from flask.wrappers import Request
from swcf import app
from flask import render_template, redirect, request, url_for
from swcf.dao.indexDAO import *

@app.route("/", methods=['GET'])
def index():
    coba = selectOne()
    print(coba)
    return render_template("layout.html")

@app.route("/sendPost", methods=['POST'])
def sendPost():
    print('masuk sini')
    name = request.form['name']
    email = request.form['email']
    issue = request.form['issue']
    # content = request.form['content']
    print(name, email, issue)
    hInsert = insertPost(name, email, issue, 'content')
    if hInsert['flag'] == 'T':
        return render_template("layout.html")