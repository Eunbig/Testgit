from flask import Flask, jsonify, g, request
import sqlite3
from flask import render_template
DATABASE = './db/test.db'
app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None: db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def init_db():
    with app.app_context():
        db = get_db()
        print (db)
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def add_student(name, age, sex):
    sql = "INSERT INTO students (name, sex, age) VALUES('%s', '%s', %d)" % (name, sex, int(age))
    print sql
    db = get_db()
    db.execute(sql)
    res = db.commit()
    return res

def find_student(name):
    sql = "select * from students where name = '%s' limit 1" %(name)
    print sql
    db = get_db()
    rv = db.execute(sql)
    res = rv.fetchall()
    rv.close()
    return res[0]

def update_student(name, age):
    sql = "update students set age = '%d' where name is '%s'" % (int(age), name)
    print sql
    db = get_db()
    db.execute(sql)
    res = db.commit()
    return res

def del_student(name):
    sql = "delete from students where name = '%s' limit 1" % (name)
    print sql
    db = get_db()
    db.execute(sql)
    res = db.commit()
    return res

@app.route('/')
def users():
    return jsonify(hello='world')

@app.route('/add', methods=['POST', 'GET'])
def add_user():
    if request.method == 'GET':
        return render_template('add.html')
    else:
        req_name = request.form.get('name')
        req_age = int(request.form.get('age'))
        req_sex = request.form.get('sex')
        print req_name, req_age, req_sex
        add_student(req_name, req_age, req_sex)
    return ''

@app.route('/del', methods=['GET'])
def del_user():
    name = request.args.get('name')
    res = del_student(name)
    return 'Success'

@app.route('/update', methods=['GET'])
def update_user():
    name = request.args.get('name')
    age = request.args.get('age')
    res = update_student(name, age)
    return 'Success'

@app.route('/find_user')
def find_user_by_name():
    name = request.args.get('name')
    student = find_student(name)
    return jsonify(name=student['name'], age=student['age'], sex=student['sex'])

if __name__ == '__main__':
#    init_db()
    app.run(debug=True, host='0.0.0.0', port = 8989)
