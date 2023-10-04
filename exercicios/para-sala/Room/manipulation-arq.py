import csv
# with open("./data.txt", "r") as arq: #read
#     content = arq.read()
#     print(f"{content} - Teacher")
#     line = arq.readlines()
#     print(line[2])

    
# with open("./dataOne.txt", "w") as arquive:
#     arquive.write("End line.")


# data = [["name", "age"], ["Beyonce", 42], ["Bruna", 27]]

# with open("people.csv", "w", newline= "") as arq_csv:
#      writer_csv = csv.writer(arq_csv)
#      writer_csv.writerows(data)

 
# with open("people.csv", "r") as arq:
#     reader_csv = csv.reader(arq)
#     for line in reader_csv:
#         print(line)


import json

# data = [{"name": "Beyonce", "age": 42, "city": "Houston Texas"},
#         {"name": "Bruna", "age": 27, "city": "Sao Paulo"}]

# with open("data.json", "w") as arquive_json:
#     json.dump(data, arquive_json)

# with open("data.json", "r") as arquive_json:
#     data = json.load(arquive_json)
#     print(data)

#Exercise

# with open("./dataExerciseOne.txt", "r") as arq: #read
#      content = arq.read()
#      print(f"{content} - Bodecam")

    
# data = [{"Name": "Beyonce", "Age": 42, "City": "Houston Texas", "Profission": "Singer, Performer and Actor",
#          "Resume": "American singer, songwriter, and businesswoman. Known as Queen Bey, she has been widely recognized for her boundary pushing artistry, vocals, and performances. Her contributions to music and visual media and her concert performances have led her to become a prominent cultural figure of the 21st century. She was named the eighth greatest singer of all time by Rolling Stone in 2023."}]
# with open("dataExerciseTwo.json", "w") as arquive_json:
#      json.dump(data, arquive_json)
# with open("dataExerciseTwo.json", "r") as arquive_json:
#      data = json.load(arquive_json)
#      print(data)


data = [["Name", "Age", "Grade"], ["Beyonce", 42, 10], ["Bruna", 27, 10]]

with open("dataExerciceStudants.csv", "w", newline= "") as arq_csv:
      writer_csv = csv.writer(arq_csv)
      writer_csv.writerows(data)

with open("dataExerciceStudants.csv", "r") as arq:
     reader_csv = csv.reader(arq)
     for line in reader_csv:
         print(line)
