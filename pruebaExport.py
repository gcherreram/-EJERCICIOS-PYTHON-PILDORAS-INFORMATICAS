import csv

keep_list = keep_three_states()

with open("data/afv.csv","w", newline:¿'') as new_file:
	for line in keep_list:
		wr = csv.writer(new_file)
		wr.writerow(line)