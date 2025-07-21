#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_csv('data.csv')
print(df)


# In[2]:


df.to_csv('output.csv')
df


# In[4]:


df['Name']
#df[['Name','Age']]


# In[5]:


df[df['Age']>25]


# In[2]:


import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.plot(x,y)
plt.title("Line-chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()


# In[4]:


categories=['A','B','C']
values=[10,20,15]
plt.bar(categories,values)
plt.title("Bar Chart")
plt.show()


# In[5]:


x=[1,2,3,4,5]
y=[2,4,1,8,7]
plt.scatter(x,y,color="red")
plt.title("Scatter plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# In[ ]:




