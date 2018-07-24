import csv
import random

count_1 = 0 
count_2 = 0

with open('train.csv', 'r', newline = '') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter = ',')
	
	for row in csv_reader:
		count_1 += 1
		
n_split = int(((count_1-1) * 10) / 100)
f = open('validation.csv', 'w', newline = '')
validation_file = csv.writer(f, delimiter = ',')

for i in range(1, n_split + 1):
	chose = random.randint(1, count_1-1)
	
	with open('train.csv', 'r', newline = '') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter = ',')
		
		for row in csv_reader:
			count_2 += 1
			
			if count_2 == chose:
				validation_file.writerow(row)
		
		count_2 = 0		
		
f.close()