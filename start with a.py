import csv
with open('emp.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:

        if ((row[1]).startswith("a")):
            print(row[0],row[1],row[2])
    file.close()
