import pyodbc
import csv

cnxn = pyodbc.connect("DRIVER={MySQL}; SERVER={127.0.0.1};DATABASE={mysql}; UID={root}; PASSWORD={L4rd_erix};")
crsr = cnxn.cursor()

insert_str = 'select * from user'
print('insert_str')
crsr.execute(insert_str)
cnxn.commit()
out = crsr.fetchall()
print('end')
