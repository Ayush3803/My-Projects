from prettytable import from_csv
with open("datatable.csv","r")as fp:
    x=from_csv(fp)
print(x)    
