from prettytable import PrettyTable
x=PrettyTable()
x.field_names=['City name','Area','Population','Annual rainfall']
x.add_row(['Adelaide',1295,1158259,600.5])
x.add_row(['Brisbane',5905,1857594,1146.4])
x.add_row(['Darwin',112,120900,1714.7])
x.add_row(['Hobart',1357,205556,619.5])
x.add_row(['Sydney',2058,4336374,1214.8])
x.add_row(['Melbourne',1566,3806092,646.9])
x.add_row(['Perth',5386,1554769,869.4])
print("table sorted by population:")
x.sortby="Population"
print(x)
print()
print("Table sorted by city in descending order:")
x.sortby="City name"
x.reversesort=True
print(x)
print("Table sorted by Population:")
x.sortby="Population"
print(x)
print("Table sorted by city in ascending order:")
x.sortby="City name"
x.reversesort=False
print(x)

