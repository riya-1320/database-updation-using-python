import csv
import MySQLdb

import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

mydb = MySQLdb.connect(host="127.0.0.1", user="root", password="", database="student_db")

f = open('error.csv', 'w')          
with open('Machine_readable_file.csv') as csv_file:
    csvfile = csv.reader(csv_file, delimiter=",")
    all_value = []
    for row in csvfile:
        value = (row[0], row[1], row[2])
        var_convt = int(value[1])
        if var_convt > 1000000000 and var_convt < 9999999999:
            if(re.fullmatch(regex, value[2])):
                all_value.append(value)
            else:
                writer = csv.writer(f)
                error_list = [value[0], value[1], "Please enter valid email address"]
                writer.writerow(error_list)
        else:
            if(re.fullmatch(regex, value[2])):
                writer = csv.writer(f)
                error_list1 = [value[0], "Please enter 10 digits only", value[1]]
                writer.writerow(error_list1)
            else:
                writer = csv.writer(f)
                error_list2 = [value[0], "Please enter 10 digits only", "Please enter valid email address"]
                writer.writerow(error_list2)
            

                    

                


            

      
# Create the INSERT INTO sql query
query = "insert ignore into `info` (`name`,`contact`,`email`) VALUES (%s, %s,%s)"


# Get the cursor, which is used to traverse the database, line by line
mycursor = mydb.cursor()
mycursor.executemany(query, all_value)

# Commit the transaction
mydb.commit()
f.close()

