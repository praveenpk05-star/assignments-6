import csv

with open('emp.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if((row[0]) != ""):
            if ((row[1]) != ""):
                if ((row[2]) != " "):
                    print(row[0], row[1], row[2])


    file.close()
