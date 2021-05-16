# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nuchYitwbp8TFXT7FTCmsPGfKIvDFDbB
"""

import random as rand
import numpy as np
from matplotlib import pyplot as plt

simu_len=100000
count=0
for i in range (simu_len):
  X_1=np.random.randint(1,7)
  X_2=np.random.randint(1,7)
  X_3=np.random.randint(1,7)
  X_4=np.random.randint(1,7)
  if(X_1+X_2+X_3+X_4==22):
     count+=1
  simu_prob=count/simu_len
  theo_prob=10/1296
print("probability by simulation = ",simu_prob)
print("theoritical probability=",theo_prob)
data1 = {'theoritical probability':theo_prob, 'simulated probability':simu_prob}
prob_type = list(data1.keys())
prob = list(data1.values())
  
fig = plt.figure(figsize = (6, 4))
 
# creating the bar plot
plt.bar(prob_type,prob, color ='green',width = 0.08)
plt.xlabel("type of probability")
plt.ylabel("probability")
plt.title("Probability of getting 22")
plt.show()