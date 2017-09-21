import csv
from pypika import Query, Table, Field


from turbodbc import connect
connection_string = "DRIVER={MySQL}; " \
                    "SERVER={127.0.0.1};" \
                    "DATABASE={exampledb}; " \
                    "UID={root}; PASSWORD={L4rd_erix};"

connection = connect(connection_string=connection_string)
cursor = connection.cursor()
query_to_run = 'select * from Persons'
cursor.execute(query_to_run)
out = cursor.fetchall()

print(str(out))
print('Application end')
