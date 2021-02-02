from flask import Flask
from flask import jsonify
import pandas as pd
import wikipedia


app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return '<h3>follow the light to find the truth</h3>\n<a href="/light">Light</a>'

@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

@app.route('/html')
def html():
    """Returns some custom HTML"""
    return """
    <title>This is a Hello World World Page</title>
    <p>Hello</p>
    <p><b>World</b></p>
    """
@app.route('/light')
def light():
    return """<h1> A hot dog is a sandwich</h1>
    
    <img src='https://i.scdn.co/image/3f927022317b36fa20ecfdb589dec30f682600c2'>
    """



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
