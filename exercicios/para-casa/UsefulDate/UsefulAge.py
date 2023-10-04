import csv
import json

data = []
def add_info_in_usefull():
      age = input("Enter u age \n")   
      
      list ={age: int()}
      
      data.append(list)
      
      with open("dataAGE.py", "w", newline= "") as arq_csv:
            writer_csv = csv.writer(arq_csv)
            writer_csv.writerows(data)            
            return data

add_info_in_usefull()