from flask import Flask
from flask_middleware_jwt import Middleware, middleware_jwt_required

app = Flask(__name__)

app.config['MIDDLEWARE_URL_IDENTITY']     = 'http://0.0.0.0:5000'
app.config['MIDDLEWARE_VERIFY_ENDPOINT']  = '/token/verify'
app.config['MIDDLEWARE_BEARER']           = True
app.config['MIDDLEWARE_VERIFY_HTTP_VERB'] = 'GET'
app.config['JWT_SECRET']                  = 'super-secret'

middleware = Middleware(app)

@app.route("/")
@middleware_jwt_required
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(port=5001)