from tabulate import tabulate
table=[['Name','Age'],['Aman',23],['Neha',25],['Lata',27]]
print(tabulate(table,headers='firstrow'))
print('\n')
li=[2,4,6]
print(tabulate(table,headers='firstrow',showindex=li))
