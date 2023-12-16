import numpy as np
import matplotlib.pyplot as plt
a=[]
month = np.array(range(1,13))
year = np.array(range(2013,2022))
with open("Temperature.txt") as f:
    data = f.read()
    #print(data)
temList = data.split("\n")


fig = plt.figure(figsize=(15,8))
fig.add_subplot(2, 2, 1)
plt.subplot(2, 2, 1)
for i in range(9):
    yearlist = temList[i+1].split(",")
    del yearlist[0]
    yearList = [float(x) for x in yearlist]
    a.append(yearList)
    #print(yearList)
    yea = 2013 + i 
    plt.plot(month,yearList , label=str(yea))

plt.title('Tainan Monthly Temperature 2013 to 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in degree C')
plt.legend()
plt.savefig('lab12_01.png')
avgList =[]
sum = 0
for l in range(12):
    avg = (a[0][l]+a[1][l]+a[2][l]+a[3][l]+a[4][l]+a[5][l]+a[6][l]+a[7][l]+a[8][l])/9
    avgList.append(avg)
    sum += avg

sum = sum/12
#plt.annotate(avgList, (month, avgList))
plt.subplot(2, 2, 2)
for k in range(len(month)):
    plt.text(month[k],avgList[k],str(round(avgList[k],2)))
plt.plot(month,avgList , '-o', label="mean of 9 years")
plt.axhline(y=sum, xmin=0.0, xmax=1.0,linestyle= '--',color = "r")
plt.text(0.5,sum,str(round(sum,2)))
plt.title('Tainan Monthly mean Temperature 2013 to 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in degree C')
plt.savefig('lab12_02.png')
plt.legend()
plt.show()


fig.savefig('lab12_03.png')