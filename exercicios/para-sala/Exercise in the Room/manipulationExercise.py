import csv
import json

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


data = [["Beyonce", 42, 10], ["Bruna  ", 27, 10]]

# with open("dataExerciceStudants.csv", "w", newline= "") as arq_csv:
#       writer_csv = csv.writer(arq_csv)
#       writer_csv.writerows(data)

total_grade = 0
total_studants = 0

with open("dataExerciceStudants.csv", "r") as arq:
    reader_csv = csv.reader(arq)
    for line in reader_csv:
        name, age, grade = line
        grade = float(grade)
        total_grade = total_grade + grade
        total_studants = total_studants + 1
    
    if total_studants > 0:
        average = grade / total_studants
        print(f"Average grade: {average}")
    
    else:
        print("No have studants in arquive")