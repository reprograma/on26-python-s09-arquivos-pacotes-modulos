import json

data = {
    'Book': 'Harry Potter', 
    'Author': 'J.K. Rolling', 
    'Year of publication:': 1995
    }

with open('data.json', 'w', newline='') as line:
    json.dump(data, line)

with open('data.json', 'r') as line:
    data_read = json.load(line)
    print(data_read)