from flask import Flask, request, jsonify
from os import getenv

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/json', methods=['GET'])
def json():
    return jsonify({'message': 'Hello, python world!'})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=getenv('LISTEN_PORT', 8080))
