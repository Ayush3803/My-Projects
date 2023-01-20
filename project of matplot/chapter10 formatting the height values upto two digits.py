from tabulate import tabulate
table=tabulate({'Name':['Aman','Lata','Neha'],'Age':[23,25,28],'Height':[153.4567,151.2362,180.2564]},headers='keys',floatfmt='2f')
print(table)
