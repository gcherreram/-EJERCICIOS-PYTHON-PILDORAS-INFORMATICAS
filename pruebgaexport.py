new_list = ["1","2","4"]
import csv

with open("out.csv","w", newline='') as pruebaexp:

    for line in new_list:
        wr = csv.writer(pruebaexp)
        wr.writerow(line)