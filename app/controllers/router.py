from flask import render_template
from app import app

@app.route("/index/<name>", methods=['GET'])
@app.route("/", defaults={"name": None}, methods=['GET'])
def index(name):
    return render_template('index.html', user=name)