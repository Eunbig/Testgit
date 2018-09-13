from flask import Flask, request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world~'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        login_id = request.form.get('login_id')
        login_pw = request.form.get('password')
        return_str = "ID: {}, PW: {}".format(login_id, login_pw)
        return return_str

@app.route('/gugu', methods=['GET', 'POST'])
def gugu():
    if request.method == 'GET':
        return render_template('gugu.html')
    else:
        gugu_input1 = request.form.get('gugu_input1')
        gugu_input2 = request.form.get('gugu_input2')
        return_str = "{} * {} = {}".format(gugu_input1, gugu_input2,int(gugu_input1)*int(gugu_input2))
        return return_str

if __name__ == '__main__':
    app.run(debug=True, port=8989, host='0.0.0.0')
