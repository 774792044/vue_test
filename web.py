from flask import Flask
from flask_cors import *
from flask import request, jsonify
import os


app = Flask(__name__)
CORS(app, resources=r'/*')


@app.route('/get_image_path', methods=['GET'])
def hello_world():
    result = {}
    path = request.args.get("path")
    print(type(os.listdir(path)))
    result['image_path_list'] = os.listdir(path)
    return result

if __name__ == '__main__':
    app.run(debug=True)
