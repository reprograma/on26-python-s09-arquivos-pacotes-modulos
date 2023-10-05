import csv

data = ['Cintia', 34, 9], ['Kenison', 38, 7], ['Kaua', 16, 8]

with open('students.csv', 'w', newline='') as file_csv:
    writer_csv = csv.writer(file_csv)
    writer_csv.writerows(data)

with open('students.csv', 'r') as file:
    reader_csv = csv.reader(file)
    
    total_notes = 0
    total_students = 0

    for line in reader_csv:
        name, age, note = line
        note = float(note)
        total_notes += note
        total_students += 1

    if total_students > 0:
        average = total_notes / total_students
        print(f'The average grade is: {average}')
    else:
        print(f'There are no students in the file')