import json

with open('data.json', 'r', encoding = 'utf8') as jsonFile:
    data = json.load(jsonFile)
    print(data)
    print(type(data))

    for i in data['employees']:
        print(i)

with open('data_another.json', 'w', encoding = 'utf8') as anotherjsonFile:
    json.dump(data, anotherjsonFile)