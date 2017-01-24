import csv

with open('iitbhu_prof_data.csv','r',newline="") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        try:
            print(str(row[0]).encode('utf-8'))
        except:
            pass
