import matplotlib.pyplot as plt
import csv
Names=[]
Values=[]
with open ('bp report.csv','r')as csvfile:
    lines=csv.reader(csvfile,delimiter=',')
    for row in lines:
        Names.append(row[0])
        Values.append(int(row[1]))
plt.scatter(Names,Values,color='g',s=100)
plt.xticks(rotation=25)
plt.xlabel('NAMES')
plt.ylabel('VALUES')
plt.title('Patients blood pressure report',fontsize=20)
plt.show()
 
