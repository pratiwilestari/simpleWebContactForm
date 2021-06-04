from swcf import app
from flask import render_template
from swcf.dao.indexDAO import *

@app.route("/", methods=['GET'])
def index():
    coba = selectOne()
    print(coba)
    return render_template("layout.html")