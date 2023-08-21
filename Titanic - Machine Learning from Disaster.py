#!/usr/bin/env python
# coding: utf-8

# # Titanic - Machine Learning from Disaster

# In[1]:


import numpy as np


# In[2]:


import pandas as pd 


# In[3]:


Data = pd.read_csv("D:\\Downloads\\train.csv")


# In[4]:


Data.head(20)


# In[5]:


Data.dtypes 


# In[6]:


Data.describe() 


# In[7]:


missing_values=Data.isnull().sum()


# In[8]:


missing_values[missing_values>0]/len(Data)*100 


# In[9]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[10]:


sns.heatmap(Data.isnull(),yticklabels=False,cbar=False )


# In[11]:


Data.drop(['PassengerId','Name','Ticket','Cabin'],axis=1,inplace=True)
Data.head()


# # Fill missing values with mode

# In[12]:


Data['Age']=Data['Age'].fillna(Data['Age'].mode()[0])
Data['Embarked']=Data['Embarked'].fillna(Data['Embarked'].mode()[0])  


# In[13]:


Data.head(10) 


# # Visualize Outliers 

# In[14]:


sns.boxplot(Data['Fare'],data=Data)


# In[15]:


Data['Fare'].hist()


# In[22]:


print('skewness value of Age: ',Data['Age'].skew())
print('skewness value of Fare: ',Data['Fare'].skew())


# In[23]:


Q1 = Data['Fare'].quantile(0.25)
Q3 = Data['Fare'].quantile(0.75)
IQR = Q3 - Q1
whisker_width = 1.5
Fare_outliers = Data[(Data['Fare'] < Q1 - whisker_width*IQR) | (Data['Fare'] > Q3 + whisker_width*IQR)]
Fare_outliers.head()


# # Capping and Flooring 

# In[25]:


Q1 = Data['Fare'].quantile(0.25)
Q3 = Data['Fare'].quantile(0.75)
IQR = Q3 - Q1
whisker_width = 1.5
lower_whisker = Q1 -(whisker_width*IQR)
upper_whisker = Q3 + ( whisker_width*IQR)
Data['Fare']=np.where(Data['Fare']>upper_whisker,upper_whisker,np.where(Data['Fare']<lower_whisker,lower_whisker,Data['Fare']))


# In[26]:


sns.boxplot(Data['Fare'], data = Data)


# In[29]:


Data.mean()


# In[30]:


Data.median() 


# In[31]:


Data.mode() 


# In[35]:


Data.std() 


# In[ ]:




