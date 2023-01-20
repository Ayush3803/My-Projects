from tabulate import tabulate
table=[['Name','Age'],['Aman',23],['Neha',25],['Lata',27]]
print(tabulate({"Name":['Aman','Lata','Neha'],'Age':[23,25,28]},headers='keys'))
print('\n')
print(tabulate({"Name":['Aman','Lata','Neha'],'Age':[23,25,28]},headers='keys',showindex=True))
