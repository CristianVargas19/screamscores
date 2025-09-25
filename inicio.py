from flask import Flask

app = Flask(screamscore)

@app.route("/")
def inicio():
    return "<h1>Hello World</h1>"
