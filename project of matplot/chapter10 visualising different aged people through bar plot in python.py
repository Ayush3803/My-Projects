import matplotlib.pyplot as plt
import csv
x=[]
y=[]
with open ('different people ages.csv','r')as csvfile:
    plots=csv.reader(csvfile,delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(int(row[2]))
plt.bar(x,y,color='g',width=0.72,label="AGE")
plt.xlabel('NAMES')
plt.ylabel('AGES')
plt.title('Age of different people')
plt.legend()
plt.show()
