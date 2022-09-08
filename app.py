from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "secret_key_1755"

@app.route("/hello")
def index():
    flash("what's your name bro?")
    return render_template("index.html")

@app.route("/greet", methods=["POST","GET"])
def greet():
    flash("Hello " + request.form['name_input'] + "! Shout-out to u!")
    return render_template("index.html")
 