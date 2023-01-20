from tabulate import tabulate
table=[["Roll number","Student name","Marks"],
       [1,"Sasha",34],
       [2,"Richard",36],
       [3,"Judy",20],
       [4,"Lori",39],
       [5,"Maggie",40]]
table1=tabulate(table)
table2=tabulate(table,headers='firstrow')
print(table1)
print('\n')
print(table2)
print('\n')
print(tabulate(table,headers='firstrow',tablefmt='html'))
        
