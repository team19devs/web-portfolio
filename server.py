from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/<string:get_page>")
def page(get_page):
	return render_template(get_page)

