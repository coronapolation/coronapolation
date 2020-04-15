import csv
with open('All_raw_test1.csv', newline='', errors='ignore', encoding='utf-16') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
         print(row)
