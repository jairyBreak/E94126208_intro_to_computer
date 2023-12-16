import numpy as np
import matplotlib.pyplot as plt
a=[]
month = np.array(range(1,13))
year = np.array(range(2013,2022))
with open("oddExperiment.txt") as f:
    data = f.read()
    #print(data)
temList = data.split("\n")
del temList[0]
del temList[-1]
for i in range(len(temList)):
    a.append(temList[i].split(" "))
x = []
y = []

for j in range(len(a)):
    x.append(int(a[j][1]))
    y.append(float(a[j][0]))
x = np.array(x)
z = np.polyfit(x, y, 2)
w = np.polyfit(x, y, 1)
z2 = z[0] * x ** 2 + z[1] * x + z[2]
w2 = w[0] * x + w[1]
print(z)
mseFor2 = 0
mseFor1 = 0
for k in range(len(y)):
    mseFor2 += (y[k]-z2[k])**2
    mseFor1 += (y[k]-w2[k])**2
mseFor2 = round(mseFor2/len(y),5)
mseFor1 = round(mseFor1/len(y),5)
plt.scatter(x, y)
plt.plot(x,z2,"g",label=("fit of degree 2,LSE="+str(mseFor2)))
plt.plot(x,w2,"r",label=("fit of degree 1,LSE="+str(mseFor1)))
plt.title('Scatter Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('lab12_plus.png')
plt.show()
