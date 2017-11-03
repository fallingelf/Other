#Exercise1 for Example 1.4.1 in page 16 of 迭代 混沌 分形
import numpy as np
import matplotlib.pyplot as plt
import random
def f1(x):
    return 1-abs(2*x-1)

num_iteration=1
x=np.linspace(0,1,1001)
y=x
x0=random.random()
trajectory=[]
trajectory.append(x0)
trajectory.append(f1(x0))
i=0
while abs(trajectory[i+1]-trajectory[i]) > 0.00001:
    trajectory.append(f1(trajectory[i+1]))
    i=i+1
print(trajectory[len(trajectory)-1])
for i in range(0,num_iteration):                       #对f1迭代num_iteration次
    y=f1(y)
plt.plot(x,y)
plt.plot(x,x)
trajectory=np.array(trajectory)
plt.plot(trajectory,trajectory,'*')
plt.plot(trajectory,f1(trajectory))
plt.show()

