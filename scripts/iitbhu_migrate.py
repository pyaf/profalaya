import csv
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR, 'data/done/iitbhu_prof_data.csv')
print(path, BASE_DIR)
from professor_info.models import *

def run():
    # College.objects.all().delete()
    # Professor.objects.all().delete()
    # Department.objects.all().delete()
    try:
        with open(path,'r',newline="") as csvfile:
            file = csv.reader(csvfile,delimiter=';')
            i=1
            for row in file:
                try:
                    name = row[0].strip()
                    email = row[1].strip()
                    designation = row[2].strip()
                    department = row[3].strip()
                    college = row[4].strip()
                    phone = row[5].strip()
                    area_of_interest = row[6].strip()
                    profile_link = row[7].strip()
                    display_picture = row[8].strip()
                    try:
                        prof = Professor(name=name,email=email,designation=designation,phone=phone,area_of_interest=area_of_interest,profile_link=profile_link,display_picture=display_picture)
                        try:
                            col = College.objects.get(name=college)
                            print("got col", col)
                        except:
                            print("wtf is the prob?")
                            col= College(name=college,address="Varanasi-221005, India")
                            col.save()
                        try:
                            dept = Department.objects.get(name=department)
                            print("got dept",dept)
                        except:
                            dept = Department(name=department)
                            dept.save()

                        prof.department = dept
                        prof.college = col
                        print("wtf is prob")
                        prof.save()
                        print(i,"done")
                        i+=1
                    except Exception as e:
                        print(e)
                        break

                except Exception as e:
                    print(row)
                    print(e)

    except Exception as e:
        print(e)
