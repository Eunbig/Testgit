from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/test', methods=['GET', 'POST'])
def mytest():
    if request.method == 'GET':
        print request.args
        return request.args['get_args']
    else:
        return "asdfsad"

if __name__=='__main__':
    app.run(debug=True, port=8989, host='0.0.0.0')
