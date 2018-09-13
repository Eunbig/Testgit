from flask import request, Flask, render_template

app = Flask(__name__)

@app.route('/ex4', methods=['GET'])
def ex_4():
    if request.method == 'GET':
        req_url = request.args.get('url')
        return render_template('ex4.html', url=req_url)
    else:
        return render_template('ex4.html')
    return ''

if __name__ == '__main__':
    app.run(debug=True, port=8989, host='0.0.0.0')

