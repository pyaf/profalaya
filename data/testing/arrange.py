import csv

with open('test2.csv', 'r', newline='') as csvfile:
    file = csv.reader(csvfile)
    i = 0
    data = []
    for row in file:
        try:
            data.append(" ".join(row))
        except:
            pass

    print(data)
    with open('test1.csv', 'w', newline='') as csvfile:
        file = csv.writer(csvfile)

        while True:
            try:
                c = 'School of Material Science and Technology; Indian Institute of Technology (Banaras Hindu University)'
                # print(i)
                w = [data[i],data[i+8],data[i+2],c,data[i+6], data[i+4]]
                w = ";".join(w)
                print(w)
                file.writerow([w])
                i+=10
            except Exception as e:
                print(e)
                break
    # print(type(list(file)))
    # for row in list(file):
    #     print(row)
