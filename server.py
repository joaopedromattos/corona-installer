from flask import Flask
from flask import render_template
from process_data import process_data


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_data')
def data():
    success = process_data()
    return {"success": success}
