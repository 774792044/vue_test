from flask import Flask
from flask_cors import *
from flask import request, jsonify
import os


app = Flask(__name__)
CORS(app, resources=r'/*')


@app.route('/get_image_path', methods=['GET'])
def get_image_path():
    '''
    文件命名必须是 数字.jpg
    '''
    result = {'image_path_list': []}
    try:
        path = request.args.get("path")
        image_list = os.listdir(path)
        image_list.sort(key=lambda x:int(x.split('.')[0]))
        result['image_path_list'] = image_list
    except Exception as e:
        print(e)
    return result

@app.route('/crawl_image', methods=['GET'])
def crawl_image():
    url = request.args.get("url")
    print(url)

    return "OK"

if __name__ == '__main__':
    app.run(debug=True)
