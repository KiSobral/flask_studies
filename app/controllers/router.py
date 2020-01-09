from flask import render_template
from app import app

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html', user=name)

@app.route("/login")
def login():
    return render_template('base.html')