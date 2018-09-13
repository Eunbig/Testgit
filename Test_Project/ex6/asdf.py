from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        req_first = request.form.get('first')
        req_second = request.form.get('second')
        data = subprocess.Popen([req_first,req_second], stdout=subprocess.PIPE)
        return render_template('index.html', data=data.communicate())

if __name__ == '__main__':
    app.run(debug=True, port=8989, host='0.0.0.0')
