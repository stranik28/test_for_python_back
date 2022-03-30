from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def sample():
    a = request.args['name']
    b = request.args['message']
    return a + '! <br/>' + b

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8000')