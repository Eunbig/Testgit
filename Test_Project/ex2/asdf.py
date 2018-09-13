from flask import render_template, Flask, jsonify, g, request
import sqlite3

app = Flask(__name__)
@app.route('/')
def index():
    data = 'Hello world jinja2'
    return render_template('index.html', body_data=data)

@app.route('/ex2', methods=['GET'])
def ex_2():
    with open('/etc/passwd','r') as f:
        data=f.readlines()
    return render_template('ex2.html', data=data)

if __name__ == '__main__':
    app.run(debug=True , host='0.0.0.0', port= 8989)
