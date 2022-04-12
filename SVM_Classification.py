#!/usr/bin/env python
# coding: utf-8

# In[31]:


f = open("closed_door.txt")
Lines = f.readlines()
y_closed = []
x_closed_intermediate = []
x_closed = []

for line in Lines:
    line.strip()
    y_closed.append(int(line.split()[0]))
    x_closed_intermediate.append(line.split()[1:])
    
for x_list in x_closed_intermediate:
    x_temp = []
    for x in x_list:
        x_temp.append(float(x.split(":")[1]))
    x_closed.append(x_temp)
    
#print(x_closed)


# In[32]:


f = open("open_door.txt")
Lines = f.readlines()
y_open = []
x_open_intermediate = []
x_open = []

for line in Lines:
    line.strip()
    y_open.append(int(line.split()[0]))
    x_open_intermediate.append(line.split()[1:])
    
for x_list in x_open_intermediate:
    x_temp = []
    for x in x_list:
        x_temp.append(float(x.split(":")[1]))
    x_open.append(x_temp)
    
#print(x_open)


# In[33]:


x = x_open + x_closed
y = y_open + y_closed


# In[34]:


from sklearn.decomposition import PCA
import pandas as pd

pca = PCA()
x_pca = pca.fit_transform(x)
x_pca = pd.DataFrame(x_pca)
#x_pca.head()
explained_variance = pca.explained_variance_ratio_
explained_variance


# In[15]:


x_pca['target']=y
x_pca.columns = ['PC1','PC2','PC3','PC4','PC5','PC6','target']
x_pca.head()


# In[16]:


import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1') 
ax.set_ylabel('Principal Component 2') 
ax.set_title('2 component PCA') 
targets = [1, -1]
colors = ['r', 'g']
for target, color in zip(targets,colors):
    indicesToKeep = x_pca['target'] == target
    ax.scatter(x_pca.loc[indicesToKeep, 'PC1']
               , x_pca.loc[indicesToKeep, 'PC2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()


# In[37]:


import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from sklearn import svm
import pylab as pl
import numpy as np
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = train_test_split(x, y,
                                   test_size=0.5, stratify=y,
                                   random_state=32)

scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
pca = PCA(n_components=2).fit(X_train_scaled)
X_train_scaled_pca = pca.transform(X_train_scaled)
print("Shape of scaled PCA features ",np.shape(X_train_scaled_pca))

scaler = StandardScaler()
scaler.fit(X_test)
X_test_scaled = scaler.transform(X_test)
pca = PCA(n_components=2).fit(X_test_scaled)
X_test_scaled_pca = pca.transform(X_test_scaled)
print("Shape of scaled PCA features ",np.shape(X_test_scaled_pca))

#svc_model = SVC(kernel = 'linear')
svc_model = SVC(kernel='rbf',C=1.0,gamma=0.12)
svc_model.fit(X_train_scaled_pca,y_train)
result = svc_model.predict(X_test_scaled_pca)
print(svc_model.score(X_test_scaled_pca,y_test))


# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import GridSearchCV

C_range = np.logspace(-2, 10, 5)
gamma_range = np.logspace(-9, 3, 5)
param_grid = dict(gamma=gamma_range, C=C_range)
cv = StratifiedShuffleSplit(n_splits=5, test_size=0.2, random_state=42)
grid = GridSearchCV(SVC(), param_grid=param_grid, cv=cv)
grid.fit(X_train_scaled_pca, y_train)

print(
    "The best parameters are %s with a score of %0.2f"
    % (grid.best_params_, grid.best_score_)
)


# In[ ]:




