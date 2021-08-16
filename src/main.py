import os
from flask import Flask



app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return {'result': True}


if __name__ == '__main__':
    app.run(
        debug=bool(os.environ.get('FLASK_DEBUG')),
        host='0.0.0.0',
        port='5000'
    )