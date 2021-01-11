import csv


with open('emp.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # print(row[0], row[1], row[2])
        if ((row[2])  > "3500.0"):
            print(row[0],row[1],row[2])
    file.close()


