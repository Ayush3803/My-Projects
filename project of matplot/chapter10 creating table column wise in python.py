from prettytable import PrettyTable
columns=['Students name','Class','Section','Precentage']
mytable=PrettyTable()
mytable.add_column(columns[0],['Leanord','Penny','Howard','Bernadette','Sheldon','Raj','Amy'])
mytable.add_column(columns[1],['X','X','X','X','X','X','X'])
mytable.add_column(columns[2],['B','C','A','D','A','B','B'])
mytable.add_column(columns[3],['91.2%','63.5%','90.235','92.27%','98.2%','88.15','95.0%'])
print(mytable)