from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello World</h1>"


@app.route("/page")
def page():
    return "<h1>Page is here</h1>"

@app.route("/about")
def about():
    return "<h1>This is a great page</h1>"

if __name__ == "__main__":
    app.run(debug=True)
