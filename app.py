from flask import Flask, render_template
import os
from flask import flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from glob import glob
import predictresult

UPLOAD_FOLDER = 'temp/data/'
ALLOWED_EXTENSIONS = {'txt', 'csv'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/model1')
def model1():
    return render_template('model1.html')

@app.route('/model2')
def model2():
    return render_template('model2.html')


@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/gender')
def genderanalysis():
    return render_template('gender.html')

@app.route('/predictmodel')
def predictmodel():
    # change this to take the data from the form to pass into
    inputfile ="temp/data/testing.csv"
    y = predictresult.prediction(inputfile)
    return render_template('test.html', heart_prediction=y.to_html())


if __name__ == '__main__':
    app.run(debug = True)

