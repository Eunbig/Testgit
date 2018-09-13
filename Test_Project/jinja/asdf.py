from flask import render_template, Flask, jsonify, g, request
import sqlite3

DATABASE = './db/test.db'
app = Flask(__name__)

def init_db():
    with app.app_context():
        db = get_db()
        print db
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.route('/')
def index():
    data = 'Hello world jinja2'
    return render_template('index.html', body_data=data)

@app.route('/ex1', methods=['POST','GET'])
def ex_1():
    if request.method == 'GET':
        req_data = request.args.get('getdata')
        if req_data:
            return render_template('ex1.html', data=req_data)
        else:
            req_data = ''
            return render_template('ex1.html', data=req_data)
    else:
        req_data = request.form.get('postdata')
        req_data.split('b')
        return render_template('ex1.html', data=req_data)
    return ''

@app.route('/ex2', methods=['GET'])
def ex_2():
    with open('/etc/passwd','r') as f:
        data=f.read()
    return render_template('ex2.html', data=data)

@app.route('/ex3', methods=['GET', 'POST'])
def ex_3():
    if request.method == 'GET':
        sql = "select * from students"
        db = get_db()
        db.execute(sql)
        res = db.commit()
        return render_template('ex3.html', data=res)
    else:
        req_name = request.form.get('name')
        sql = "insert into students (name) values ('%s')" % (name)
        db = get_db()
        db.execute(sql)
        res = db.commit()
        return redirect(url_for('ex3'))
    return ''

if __name__ == '__main__':
    init_db()
    app.run(debug=True , host='0.0.0.0', port= 8989)
