from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello world"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")  # templateフォルダを読み込む
    if request.method == "POST":
        return "login!!"


# @app.route("/users/<name>")
# def hi(name):
#     return f"Hi.{name}!!"


@app.route("/use/<name>")
def hi_use(name):
    return f"Hi.{name}!!"


if __name__ == '__main__':
    app.run(debug=True, port=5001)
