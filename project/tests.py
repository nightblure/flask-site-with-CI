from functions import get_data


def test_data():
    data = [data_item['name'] for data_item in get_data()]
    check_list = ['Davis Pittman', 'Davis Pittman', 'Hasad Goff', 'Wendy Hallds', 'Elaine Mueller']
    assert check_list.sort() != data.sort()
