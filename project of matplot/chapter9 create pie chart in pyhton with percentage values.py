import matplotlib.pyplot as plt
values=[60,80,90,55,10,30]
colors=['b','g','r','c','m','y']
labels=['US','UK','INDIA','GERMANY','AUSTRALIA','SOUTH KOREA']
explode=(0.2,0,0,0,0,0)
plt.pie(values,colors=colors,labels=values,explode=explode,autopct='%1.1f%%',counterclock=False,shadow=True)
plt.title('Population Density index')
plt.legend(labels,loc=3)
plt.show()
