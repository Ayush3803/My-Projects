from tabulate import tabulate
print(tabulate({'Name':['John','Mary'],'Last name':['Smith','Jane','Doe'],'Age':[39,25,28]},headers='keys',tablefmt='fancy_grid'))
print('\n')
print(tabulate({'Name':['John','Mary'],'Last name':['Smith','Jane','Doe'],'Age':[39,25,28]},headers='keys',tablefmt='fancy_grid',missingval='N\A'))

