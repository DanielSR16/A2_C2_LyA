import csv
import io
            
import unicodedata
 
# def filt(word):
#     return unicodedata.normalize('NFKD', word).encode('ascii', errors='ignore').decode('ascii')

with open('datos.csv', newline='') as File:  
    reader = csv.reader(File)
    auxLit = []
    for row in reader:
        for datos in row:
                f = open("test", mode="r", encoding="utf-8")
                print(f)
                auxLit.append(datos)
        print(auxLit)
        auxLit = []     
        
          
