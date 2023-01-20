from tabulate import tabulate
mydata=[["Nikhil","Delhi"],["Ravi","Kanpur"],["Manish","Ahmedabad"],["Prince","Bangalore"]]
head=["Name","City"]
print(tabulate(mydata,headers=head,tablefmt="grid"))
