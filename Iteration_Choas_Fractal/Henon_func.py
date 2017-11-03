import matplotlib.pyplot as plt

a=0.3
b=0.6
num_iteration=100
x=[]
y=[]
x_initi=0.3
y_initi=0.3
x.append(x_initi)
y.append(y_initi)
for i in range(0,num_iteration):
    x.append(y[i])
    y.append(b*x[i]+a*y[i]-y[i])
    i=i+1
print(x,'\n',y)
plt.plot(x,y,'*')
plt.show()