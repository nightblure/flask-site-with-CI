import json


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