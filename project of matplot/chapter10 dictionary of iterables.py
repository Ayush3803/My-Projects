from tabulate import tabulate
table={'First name':['John','Mary','Jennifer'],'Last name':['Smith','Jane','Doe'],'Age':[39,28,25]}
print(tabulate(table,headers='keys'))
print("\n")
print(tabulate(table,headers='keys',tablefmt='fancy_grid'))
