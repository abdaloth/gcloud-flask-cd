from flask import Flask
from flask import render_template
import pandas as pd


app = Flask(__name__)

@app.route('/')
def hello():
    """simple landing Page."""
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
