from app import app

@app.route("/index", methods=['GET'])
@app.route("/", methods=['GET'])
def index():
    return "Hello, World!"

@app.route("/test", defaults={'name': None})
@app.route("/test/<name>")
def test(name):
    if name:
        return "Hello, %s!" % name
    else:
        return "Hello, user"