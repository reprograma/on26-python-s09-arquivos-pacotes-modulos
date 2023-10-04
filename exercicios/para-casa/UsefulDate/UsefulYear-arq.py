import csv
import json

data = []
def add_info_in_usefull():
      year_born = input("Enter the year you were born \n")    
      
      list ={year_born: int()}
      
      data.append(list)
  
      with open("dataYEARBORN.py", "w", newline= "") as arq_csv:
            writer_csv = csv.writer(arq_csv)
            writer_csv.writerows(data)            
            return data

add_info_in_usefull()