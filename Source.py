from flask import Flask , render_template, request
import pandas as pd
import os

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
csvfolderpath = os.path.join(APP_ROOT, 'OutputFolder')
@app.route('/')
def home():
    files = os.listdir(csvfolderpath)
    return render_template('index.html', files=files, fileName='')

@app.route('/Login')
def Login():
    return render_template('login.html')

@app.route('/<string:name>')
def show(name):
    csvFile = os.path.join(csvfolderpath, name)
    files = os.listdir(csvfolderpath)
    table = pd.read_csv(csvFile)
    return render_template('index.html', files=files, fileName= name, data=table.to_html())

if __name__ == '__main__':
    app.run()
