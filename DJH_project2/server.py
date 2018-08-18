from flask import request
from flask import Flask, render_template, send_from_directory
import mysql.connector
import json
from models import db


db.create_store_list()

app = Flask(__name__, static_folder='static')


@app.route('/', methods=['GET'])
def renderHtml():
    return render_template('index.html', name=None)


@app.route('/secondpage', methods=['GET'])
def renderHtml2():
    return render_template('index2.html', name=None)


@app.route('/storename', methods=['POST'])
def post_store_menu():

    content = json.loads(request.data)

    db.create_store_entry(content['store'])
    # db.create_menu(content['store'], content['menu'])

    # Insert store name to store_list if not exists
    # Create store menu if not exists, else update menu

    return json.dumps(content, ensure_ascii=False)


@app.route('/getfile/<path:filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory('./',
                               filename, as_attachment=True)
    print(filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
