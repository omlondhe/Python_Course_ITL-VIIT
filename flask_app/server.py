from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sayhello/<name>")
def say_hello(name):
    return render_template("say_hello.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
