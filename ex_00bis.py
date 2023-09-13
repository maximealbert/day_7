import json


def show_data():
    with open('D-POO-300_07_nobelPrizes.json', 'r') as myjsonfile:
        data = json.load(myjsonfile)
        category_list = []
        for element in data['prizes']:
            category_list = category_list + [element['category']]
        category_list = list(set(category_list))
        print(sorted(category_list))

    with open('D-POO-300_07_nobelLaureates.json', 'r') as myjsonfilelaureates:
        data = json.load(myjsonfilelaureates)
        laureates_list = []
        for element in data['laureates']:
            try:
                laureates_list = laureates_list + [element['firstname']+' '+element['surname']]
            except:
                laureates_list = laureates_list + [element['firstname']]
        print(sorted(laureates_list))

    with open('D-POO-300_07_nobelCountries.json', 'r') as myjsonfilecountry:
        data = json.load(myjsonfilecountry)
        country_list = []
        for element in data['countries']:
            try:
                country_list = country_list + [(element['name'], element['code'])]
            except :
                country_list = country_list + [(element['name'], 'N/A')]
        sorted_list = sorted(country_list, key=lambda x: x[0])
        print(sorted_list)


if __name__ == '__main__':
    show_data()
