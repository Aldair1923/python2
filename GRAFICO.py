import matplotlib.pyplot as plt
year = [2012, 2013, 2014,2015,2016,2017,2018,2019,2020,2021,2022] 
edad = [14,15,16,17,18,19,20,21,22,23,24]
height = [162,163,164,165,166,167,168,169,170,171,172]
weight = [55,57,59,60,62,63,65,67,68,70,72]
'''
plt.figure(figsize=(10,5))
plt.plot(year, height,color='red', marker='*', linewidth=4, markersize=11);
plt.legend(['relacion edad altura'])
plt.title('altura de aldair del 2012 - 2022')
plt.xlabel('año', fontsize=15, color= 'brown')
plt.xlabel('altura', fontsize=15, color= 'green')
#plt.margin(x=, y=0)
plt.show()
'''

plt.figure(figsize=(10,5))
plt.plot(edad,weight,color='red', marker='*', linewidth=4, markersize=11);
plt.legend(['relacion edad peso'])
plt.title('peso de aldair del 2012 - 2022')
plt.xlabel('edad', fontsize=15, color= 'brown')
plt.xlabel('peso', fontsize=15, color= 'green')
#plt.margin(x=, y=0)
plt.show()