# -*- coding:utf-8 -*-
# 线性不可分数据的生成
#author:Tomator


import math
import numpy as np
import matplotlib.pyplot as plt

f=open("SVM非线性数据集.txt",'w')

arr1=np.zeros((60,2))
for i in range(60):
    x=2*math.cos(i*6)
    y=2*math.sin(i*6)
    arr1[i,0]=x
    arr1[i,1]=y
    f.write(str(x)+" "+str(y)+" "+str(-1)+"\n")


arr2=np.zeros((60,2))
for j in range(60):
    x = 4 * math.cos(j * 6)
    y = 4 * math.sin(j * 6)
    arr2[j,0]=x
    arr2[j,1]=y
    f.write(str(x) + " " + str(y) + "" + str(1) + "\n")


plt.scatter(arr1[:,0], arr1[:,1])
plt.scatter(arr2[:,0], arr2[:,1])
plt.show()
