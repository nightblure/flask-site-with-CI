import os
from flask import Flask, render_template, redirect, request
from functions import get_data, save_data, get_new_item_id
from functions import get_data_item_by_id, get_item_index_by_id

BASE_DIR = os.getcwd()
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

CSRF_ENABLED = True
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/home")
def index():
    data = get_data()
    return render_template('home.html', data=data)


@app.route("/new_item")
def create_new_item():
    return render_template('new_item.html')


@app.route("/create_new", methods=['POST'])
def create():
    data = get_data()

    data_item = {
        'id': get_new_item_id(),
        'name': request.form.get('name'),
        'phone': request.form.get('phone'),
        'email': request.form.get('email'),
        'address': request.form.get('address')
    }

    data = list(data)
    data.append(data_item)
    save_data(data)
    return redirect('/home')


@app.route('/edit/<int:id>', methods=['GET'])
def edit(id):
    data_item = get_data_item_by_id(id)
    return render_template('edit_page.html', data_item=data_item)


@app.route('/edit/action/<int:id>', methods=['POST'])
def save(id):
    data = get_data()
    index = get_item_index_by_id(id)

    if request.form['form_btn'] == 'save':
        data_item = get_data_item_by_id(id)
        data_item['name'] = request.form.get('name')
        data_item['phone'] = request.form.get('phone')
        data_item['email'] = request.form.get('email')
        data_item['address'] = request.form.get('address')
        data[index] = data_item
        save_data(data)

    if request.form['form_btn'] == 'delete':
        del data[index]
        save_data(data)

    return redirect('/home')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
