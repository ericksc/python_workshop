import csv
from pypika import Query, Table, Field


from turbodbc import connect
connection_string = "DRIVER={MySQL}; " \
                    "SERVER={127.0.0.1};" \
                    "DATABASE={exampledb}; " \
                    "UID={root}; PASSWORD={L4rd_erix};"

connection = connect(connection_string=connection_string)
cursor = connection.cursor()

cursor.execute("INSERT INTO Persons VALUES (42, 'alex')")
connection.commit()

query_to_run = 'select * from Persons'
cursor.execute(query_to_run)
table = cursor.fetchallarrow()
df = table.to_pandas()


print('Application end')
