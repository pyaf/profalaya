import csv
with open('iitbhu_prof_data.csv','r',newline="") as csvfile:
    file = csv.reader(csvfile,delimiter=';')
    i=1
    for row in file:
        try:
            print(i,row[7].strip())
            i+=1
        except:
            pass
