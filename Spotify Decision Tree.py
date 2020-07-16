#!/usr/bin/env python
# coding: utf-8

# In[71]:


import pandas as pd
import numpy as np

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split

from matplotlib import pyplot as plt
import seaborn as sns

# import graphviz
# import pydotplus
import io
from scipy import misc

# get_ipython().run_line_magic('matplotlib', 'inline')


# In[72]:


data = pd.read_csv("/Users/atharvak/Desktop/Projects/RunningManPlaylist/data.csv")


# In[73]:


data.describe()


# In[74]:


data


# In[75]:


data.columns


# In[66]:


train, test = train_test_split(data, test_size=0.15)


# In[67]:


train


# In[76]:


c = DecisionTreeClassifier()


# In[77]:


features = ["tempo","danceability","time signature","valence", "energy"]


# In[79]:


X_train = train[features]
y_train = train["target"]

X_test = test[features]
y_test = test["target"]


# In[80]:


dt = c.fit(X_train, y_train)


# In[81]:


y_pred = c.predict(X_test)


# In[82]:


print(y_pred)


# In[83]:


print(y_test)


# In[ ]:




