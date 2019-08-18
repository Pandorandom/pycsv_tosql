#!/usr/bin/env python
#
#
#
# TOOL NAME: py_csv
# WRITTEN BY: tacree
# DATE: 8/17/19
# REV:
# First Worked:
# Purpose: the purpose of this script is to create a sql database with multiple columns and read cve_data.csv, importing the data to the sql database. Future development will involve a web app to display the tables and eventually output to a pdf.
#
# REV LIST:
# BY:
# DATE:
# CHANGES MADE:
#
#
#

import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='tacree',
    passwd='',
    db='PyCSV')

cursor = mydb.cursor()

csv_data = csv.reader(file('cve_data.csv'))
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
for row in csv_data:

    cursor.execute('INSERT INTO testcsv(name, \
          verified_date, vm_ip, cve_fixed )' \
          'VALUES("%s", "%s", "%s", "%s")',
          row)
		print(mycursor.rowcount, "was inserted.")


mydb.commit()
cursor.close()
