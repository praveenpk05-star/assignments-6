import csv

with open('emp.csv', 'w', newline='') as file:
     writer = csv.writer(file, lineterminator =' \r\n' )
     writer.writerow(['id', 'name', 'sal'])
     writer.writerow([101, "anna", "5500"])
     writer.writerow(["", "jones", "4500"])
     writer.writerow([102, "smith", ""])
     writer.writerow([103, "", "6500"])
     writer.writerow([104, "alice", "3500"])

with open('emp.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # print(row[0], row[1], row[2])
        if ((row[2]) ==  " "):
            print(row[0],row[1],row[2])
    file.close()










