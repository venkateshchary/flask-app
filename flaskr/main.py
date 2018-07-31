import os

from flask import Flask

app = Flask(__name__)


@app.route('/home')
def home():
    return 'This is the home page'
@app.route('/webpage')
def webpage():
    return '<h2> This is webpage tag</h2>'

if __name__ == "__main__":
    app.run(debug=True)
