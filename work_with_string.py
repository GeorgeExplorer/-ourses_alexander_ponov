dict_data = {
    "key1": "value1",
    "key2": 2,
    "key3": True,
    "key4": 50.5,
    "key5": None
}

data_string = dict_data['key1']

modify_dict_data = f'Key 1 has a value equal {dict_data["key3"]}'
print(modify_dict_data)