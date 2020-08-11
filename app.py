from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug = True)

