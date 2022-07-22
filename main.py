from flask import Flask,render_template, request
import json


app=Flask(__name__)

with open('config.json', 'r') as c:
    params = json.load(c)["params"]


@app.route('/')
def home():
    return render_template('index.html',params=params)

@app.route('/about')
def about():
    return render_template('about.html',params=params)

@app.route('/contact',methods=('Get','Post'))
def contact():
    

    return render_template('contact.html',params=params)

@app.route('/post')
def post():
    return render_template('post.html',params=params)

app.run(debug=True)
