from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template("index.html")

@app.route('/out.csv')
def data():
  data = open(os.path.join(os.path.dirname(__file__), 'out.csv'), 'r').read()
  data = 'x_value,y_value\n' + data
  return data

if __name__ == '__main__':
  app.run()
