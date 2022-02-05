from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello world"


# @app.route("/login")
# def login():
#     return "login!!"


@app.route("/users/<name>")
def hi(name):
    return f"Hi.{name}!!"


if __name__ == '__main__':
    app.run(debug=True, port=5001)
