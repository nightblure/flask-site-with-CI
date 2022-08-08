import json


def get_new_item_id():
    data = get_data()
    max_id = -1
    for data_item in data:
        if max_id < data_item['id']:
            max_id = data_item['id']
    return max_id + 1


def get_item_index_by_id(id):
    data = get_data()

    for index, data_item in enumerate(data):
        if data_item['id'] == id:
            return index


def get_data():
    with open('data.json', encoding='utf8') as file:
        data = file.read()
        obj_list = json.loads(data)
    return obj_list


def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)


def get_data_item_by_id(id):
    data = get_data()
    data_item = None

    for item in data:
        if item['id'] == id:
            data_item = item

    return data_item
