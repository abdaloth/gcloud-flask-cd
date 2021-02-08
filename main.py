from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def hello():
    """simple landing Page."""
    return render_template('hello_gcp.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
