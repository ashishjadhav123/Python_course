import pyodbc
con = pyodbc.connect("Driver={SQL Server};"
                      "Server=LAPTOP-K9QFULHI\SQLEXPRESS;"
                      "Database=RPA;"
                      "Trusted_Connection=yes;")

cursor = con.cursor()
cursor.execute('select * from emp_details;')

for row in cursor:
    print('row = %r' % (row,))
    print(row)