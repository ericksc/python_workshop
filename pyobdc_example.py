import pyodbc
import csv
from pypika import Query, Table, Field

cnxn = pyodbc.connect("DRIVER={MySQL}; "
                      "SERVER={127.0.0.1};"
                      "DATABASE={exampledb}; "
                      "UID={root}; PASSWORD={L4rd_erix};")
crsr = cnxn.cursor()

insert_str = 'select * from Persons'
print('insert_str')
crsr.execute(insert_str)
cnxn.commit()
out = crsr.fetchall()

customers = Table('Persons')

q = Query.into(customers).insert(1, 'Jane')

crsr.execute(str(q))
cnxn.commit()
out = crsr.fetchall()

print('end')
