from flask import Flask
from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = 'admin123'

basic_auth = BasicAuth(app)
@app.route('/secret')
@basic_auth.required
def secret_view():
    return 'Authentication Success'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)

