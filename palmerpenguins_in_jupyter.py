#!/usr/bin/env python
# coding: utf-8

# ### penguins data in palmerpenguins

# In[ ]:





# In[1]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# In[ ]:





# In[9]:


import numpy as np
import pandas as pd


# In[ ]:





# In[19]:


# !pip install palmerpenguins


# In[7]:


from palmerpenguins import load_penguins

penguins = load_penguins()
penguins.shape


# In[10]:


# pd.options.display.max_rows = None 
pd.options.display.max_rows = 10 
penguins


# In[11]:


pengs = penguins.dropna()
pengs.shape


# In[12]:


pengs.columns


# In[13]:


pengs.columns = ['sp','is', 'bl', 'bd', 'fl', 'bm', 'sx', 'yr']
pengs.columns


# In[14]:


pengs.sp.unique()


# In[15]:


pengs.groupby(["sp","sx"]).count()
pengs.groupby(["sp","sx"])['yr'].count()


# In[16]:


pengs.groupby(["sp","sx"])['yr'].count().unstack()


# In[20]:


# !pip install plotnine


# In[21]:


from plotnine import *


# In[22]:


(

ggplot(pengs) + 
    geom_point(aes("bd","bl",color="sp")) +
    geom_smooth( aes("bd","bl",color="sp"), method="lm", se=False )
)


# In[23]:


(

ggplot(pengs) + 
    geom_point(aes("bd","bl")) +
    geom_smooth( aes("bd","bl"), method="lm", se=False )

)


# In[ ]:




