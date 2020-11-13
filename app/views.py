from app import app
from flask import render_template


@app.route('/')
def welcome():
    return render_template('public/welcome.html')


@app.route('/current_features/')
def features():
    return render_template('public/features.html')


@app.route('/data_customization/')
def customization():
    return render_template('public/customization.html')
