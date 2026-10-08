import json

def get_config(data):
    with open('config.json') as json_data:
        config = json.load(json_data)

        return config[data]

