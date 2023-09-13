import json


def read_file():
    with open('D-POO-300_07_nobelLaureates.json', 'r') as myjsonfile:
        data = json.load(myjsonfile)
        return data


if __name__ == '__main__':
    print(read_file())
