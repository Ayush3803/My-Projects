from tabulate import tabulate
table=[['First name','Last name','Age'],['John','Smith',39],['Mary','Jane',25],['Jennifer','Doe',28]]
print(tabulate(table))
print('\n')
print(tabulate(table,headers='firstrow'))
 
