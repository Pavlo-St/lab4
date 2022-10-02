from flask import Flask
from flask import make_response
from waitress import serve

app = Flask(__name__)

status_code: int = 200


@app.route('/api/v1/hello-world-23')
def index():
    return make_response(f"Hello World 23", status_code)



serve(app, port=5000)
