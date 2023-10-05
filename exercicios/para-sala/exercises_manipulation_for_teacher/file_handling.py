#with open('./dice.txt', 'r') as file:
    #content = file.read()
    #print(content)
    #lines = file.readlines()
    #print(lines[2])

#with open('./dice1.txt', 'w') as file:
    #file.write("End of the line")

#dice = ['Name', 'Age'], ['Alice', 30], ['Bob', 25]

#import csv
#with open('people.csv', 'w', newline='') as file_csv:
    #writer_csv = csv.writer(file_csv)
    #writer_csv.writerows(dice)

#with open('people.csv', 'r') as file:
    #reader_csv = csv.reader(file)
    #for line in reader_csv:
        #print(line)

import json

#dice = {'Name': 'Alice', 'Age': 30, 'City:': 'Campo Grande'}

#with open('dice.json', 'w', newline='') as line_json:
    #json.dump(dice, line_json)

with open('dice.json', 'r') as line_json:
    dice = json.load(line_json)
    print(dice)