from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_base():
    return "<p>Hello, Base!</p>"

@app.route("/<path>")
def hello_world(path):
    print(path)
    return f"<p>Hello, World! -- {path}</p>"

@app.route("/<path>/<other>")
def hello_some(path, other):
    print(path, other)
    return f"<p>Hello, Other! ({other}) -- {path}</p>"

def create_app():
    return app
