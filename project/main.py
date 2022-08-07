import os
import sys
from flask import Flask, render_template, redirect, request
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from functions import get_data, save_data, get_data_item_by_id

BASE_DIR = os.getcwd()
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
FLATPAGES_ROOT = 'build'

CSRF_ENABLED = True
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
app = Flask(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)


@app.route("/")
def index():
    data = get_data()
    return render_template('index.html', data=data)


# @app.route("/new_item")
# def create_new_item():
#     return render_template('new_item.html')


@app.route("/create_new", methods=['POST'])
def create():

    data = get_data()

    data_item = {
        'id': len(data) + 1,
        'name': request.form.get('name'),
        'phone': request.form.get('phone'),
        'email': request.form.get('email'),
        'address': request.form.get('address')
    }

    data = list(data)
    data.append(data_item)
    save_data(data)
    return redirect('/')


# @freezer.register_generator
# def edit():
#     for data_item in get_data():
#         yield {'id': data_item['id']}
#
#
# @app.route('/edit/<int:id>', methods=['GET'])
# def edit(id):
#     page_path = os.path.join(TEMPLATES_DIR, 'edit_page')
#     path = f'/{page_path}/{id}'
#     data_item = flatpages.get_or_404(path)
#
#     #data_item = get_data_item_by_id(id)
#     return render_template('edit_page.html', data_item=data_item)



# @freezer.register_generator
# def save():
#     data = get_data()
#     for data_item in data:
#         yield f"/edit/action/{data_item['id'] - 1}"


#@app.route('/edit/action/<int:id>', methods=['POST'])
# def save(id):
#
#     page_path = os.path.join(TEMPLATES_DIR, 'edit_page')
#     path = f'/{page_path}/{id}'
#     data_item = flatpages.get_or_404(path)
#
#     data = get_data()
#
#     if request.form['form_btn'] == 'save':
#         name = request.form.get('name')
#         data_item = get_data_item_by_id(id)
#         data_item['name'] = name
#         data_item['phone'] = request.form.get('phone')
#         data_item['email'] = request.form.get('email')
#         data_item['address'] = request.form.get('address')
#         data[id - 1] = data_item
#         save_data(data)
#
#     if request.form['form_btn'] == 'delete':
#         del data[id - 1]
#         save_data(data)
#
#     return redirect('/')


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(host='127.0.0.1', port=8000, debug=True)
