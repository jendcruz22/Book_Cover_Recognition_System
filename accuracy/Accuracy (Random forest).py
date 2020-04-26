from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

np.random.seed(0)

df=pd.read_csv("accm.csv")

df.head()





df['is_train']=np.random.uniform(0,1,len(df))<=.80
df.head()





train,test=df[df['is_train']==True],df[df['is_train']==False]
print('No of observations in training data:',len(train))
print('No of observations in testing data:',len(test))


# In[92]:


features=df.columns[:2]
features


# In[93]:


y=pd.factorize(train['efficient'])[0]
print(y)


# In[94]:


clf=RandomForestClassifier(n_jobs=2,random_state=0)
clf.fit(train[features],y)


# In[95]:


clf.predict(test[features])
#test[features]


# In[96]:


clf.predict_proba(test[features])[0:30]


# In[97]:


test['efficient'].head()
preds=clf.predict(test[features])


# In[98]:

#this gives the confusion matrix from this we get the accuracy

pd.crosstab(test['efficient'],preds,rownames=['Actual effiecient'],colnames=['Predicted efficient'])


# In[99]:


