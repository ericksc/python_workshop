from querybuilder.query import Query

query = Query().from_table('account')
query.select()
# [{"id": 1, "name": "Person 1"}, {"id": 2, "name": "Person 2"}]
query.get_sql()
# "SELECT account.* FROM account"
print('end')