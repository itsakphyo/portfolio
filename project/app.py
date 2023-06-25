from flask import Flask, render_template
from flask_session import Session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/skill")
def skill():
    return render_template("skill.html")