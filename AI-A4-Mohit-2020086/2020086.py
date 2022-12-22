#!/usr/bin/env python
# coding: utf-8

# In[59]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt


# In[60]:


# Read Data Frame 
df = pd.read_csv("roo_data.csv")


# In[61]:


# Renamming courses 
df.rename(columns = {'Percentage in Mathematics':'Percentage in Linear Algebra'}, inplace = True)
df.rename(columns = {'percentage in Algorithms':'Percentage in Data Structures & Algorithms'}, inplace = True)
df.rename(columns = {'Percentage in Communication skills':'Percentage in Introduction To The Study Of Literature'}, inplace = True)
df.rename(columns = {'Percentage in Electronics Subjects':'Percentage in Photonics: Fundamentals & Applications'}, inplace = True)
df.rename(columns = {'Percentage in Programming Concepts':'Percentage in Advanced Programming'}, inplace = True)


# In[62]:


print("Info: \n")
df.info()                         


# In[63]:


# Print Dataframe
df.head()


# # Preprocessing the Dataframe

# In[64]:


# Plot heatmap for correlations 
import seaborn as sns
plt.figure(figsize=(15,15))
sns.heatmap(df.corr(), annot=True, cmap=plt.cm.Reds)   # heatmap to show the correaltion between columns 
plt.show()


# In[65]:


# list all the coulmns
list(df.columns)


# In[66]:


# Drop columns based on correlations and requirement 
columns_to_drop = [ 'Hours working per day',
                 'can work long time before system?',
                 'self-learning capability?',
                 'talenttests taken?',
                 'olympiads',
                 'reading and writing skills',
                 'memory capability score',
                 'Type of company want to settle in?',
                 'Taken inputs from seniors or elders',
                 'interested in games',
                 'Interested Type of Books',
                 'Salary Range Expected',
                 'In a Realtionship?',
                 'Gentle or Tuff behaviour?',
                 'hard/smart worker',
                 'worked in teams ever?',
                 'Introvert']
                
df = df.drop(columns_to_drop, axis = 1)
df.shape


# In[67]:


# See the unique values in Job Role column
df['Suggested Job Role'].unique()


# In[68]:


# club together simillar values 
replace_data_dev = ['Database Developer', 'Database Administrator', 'Database Manager', 'Data Architect']
df = df.replace(to_replace = replace_data_dev, value = 'Data Scientist')
replace_des = ['UX Designer', 'Applications Developer', 'Design & UX', 'Mobile Applications Developer', 'Quality Assurance Associate']
df = df.replace(to_replace = replace_des, value = 'UI/UX designer')
replace_eco = ['E-Commerce Analyst', 'Business Intelligence Analyst', 'Business Systems Analyst']
df = df.replace(to_replace = replace_eco, value = 'Economist')
replace_soft_dev = ['Software Systems Engineer', 'Software Developer', 'Software Engineer', 'Web Developer', 'Project Manager']
df = df.replace(to_replace = replace_soft_dev, value = 'Software Developer')
replace_crm = ['CRM Technical Developer', 'CRM Business Analyst', 'Software Quality Assurance (QA) / Testing', 'Portal Administrator', 'Programmer Analyst']
df = df.replace(to_replace = replace_crm, value = 'CRM')
replace_seq = ['Systems Security Administrator','Information Security Analyst', 'Systems Analyst', 'Solutions Architect']
df = df.replace(to_replace = replace_seq, value = 'Systems Security Management')
replace_tech = ['Technical Support',  'Technical Services/Help Desk/Tech Support', 'Technical Engineer', 'Information Technology Manager', 'Information Technology Auditor']
df = df.replace(to_replace = replace_tech, value = 'Technology Support')
replace_net = ['Network Security Administrator', 'Network Security Engineer', 'Network Engineer']
df = df.replace(to_replace = replace_net, value = 'Network Engineer')


# In[69]:


print("Unique values : ", end='')
print(df['Suggested Job Role'].unique())
print(df['Suggested Job Role'].value_counts())


# In[70]:


df = df.replace(to_replace = 'Data Scientist', value = 0)
df = df.replace(to_replace = 'UI/UX designer', value = 1)
df = df.replace(to_replace = 'Economist', value = 2)
df = df.replace(to_replace = 'Software Developer', value = 3)
df = df.replace(to_replace = 'CRM', value = 4)
df = df.replace(to_replace = 'Systems Security Management', value = 5)
df = df.replace(to_replace = 'Technology Support', value = 6)
df = df.replace(to_replace = 'Network Engineer', value = 7)


# In[71]:


list(df.columns)


# In[72]:


#catergorizing the values of percentage columns and rating columns

percentage_col = ['Acedamic percentage in Operating Systems',
                    'Percentage in Data Structures & Algorithms',
                    'Percentage in Advanced Programming',
                    'Percentage in Software Engineering',
                    'Percentage in Computer Networks',
                    'Percentage in Photonics: Fundamentals & Applications',
                    'Percentage in Computer Architecture',
                    'Percentage in Linear Algebra',
                    'Percentage in Introduction To The Study Of Literature']

df1_without_class = df.copy(deep=True)

for i in percentage_col:
    for j in range(0, df.shape[0]):
        if(df[i][j] <= 33):
            df[i][j] = 'F'
        elif(df[i][j] <= 70):
            df[i][j] = 'C'
        elif(df[i][j] <= 80):
            df[i][j] = 'B'
        elif(df[i][j] <= 100):
            df[i][j] = 'A'
            
            
rating_col = ['Logical quotient rating', 'coding skills rating', 'public speaking points']
for i in rating_col:
    for j in range(0, df.shape[0]):
        if(df[i][j] <= 3):
            df[i][j] = 'F'
        elif(df[i][j] <= 6):
            df[i][j] = 'C'
        elif(df[i][j] <= 8):
            df[i][j] = 'B'
        elif(df[i][j] <= 10):
            df[i][j] = 'A'


# In[73]:


# label encoding the features 
from sklearn import preprocessing
feature_label_encoder = preprocessing.LabelEncoder()

features = ['Acedamic percentage in Operating Systems',
                    'Percentage in Data Structures & Algorithms',
                    'Percentage in Advanced Programming',
                    'Percentage in Software Engineering',
                    'Percentage in Computer Networks',
                    'Percentage in Photonics: Fundamentals & Applications',
                    'Percentage in Computer Architecture',
                    'Percentage in Linear Algebra',
                    'Percentage in Introduction To The Study Of Literature',
                    'Logical quotient rating', 
                    'coding skills rating', 
                    'public speaking points',
                    'Extra-courses did',
                    'workshops',
                    'certifications',
                    'hackathons',
                    'Interested subjects',
                    'interested career area ',
                    'Job/Higher Studies?',
                    'Salary/work',
                    'Management or Technical']

for i in features:
    df[i] = feature_label_encoder.fit_transform(df[i])


# In[74]:


for i in list(df.columns):
    print(i)
    print(df[i].value_counts())
    print("-------------------------------------------")


# In[75]:


print("Info: \n")
df.info()   


# # Experimenting With the values

# Experimenting with the column values to find best combination of features -  
# Result: The change in the accuracy was marginal. The NN itself choose the features by setting the values of the weights to zero. 

# In[76]:


print("dataframe shape : ",df.shape)
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

train_x, test_x, train_y, test_y = train_test_split(df.drop('Suggested Job Role', axis = 1), df['Suggested Job Role'], test_size = 0.3, shuffle = True)

model = MLPClassifier(activation='tanh', solver = 'sgd',max_iter = 250, hidden_layer_sizes = (256, 128, 64, 32), early_stopping = False, validation_fraction=0.001)
model.fit(train_x.values, train_y.values.ravel())
pred_y = model.predict(test_x.values)

print("Accuracy Score = ", accuracy_score(test_y.values, pred_y))


# In[ ]:


columns_to_drop = ['Logical quotient rating', 'hackathons', 'coding skills rating', 'public speaking points', 
            'certifications', 'workshops', 'Job/Higher Studies?', 'Management or Technical', 'Salary/work']

df_1 = df.drop(columns_to_drop, axis = 1)
print("dataframe shape : ",df_1.shape)

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

train_x, test_x, train_y, test_y = train_test_split(df_1.drop('Suggested Job Role', axis = 1), df_1['Suggested Job Role'], test_size = 0.3, shuffle = True)

model = MLPClassifier(activation='tanh', solver = 'sgd',max_iter = 250, hidden_layer_sizes = (256, 128, 64, 32), early_stopping = False, validation_fraction=0.001)
model.fit(train_x.values, train_y.values.ravel())
pred_y = model.predict(test_x.values)

print("Accuracy Score = ", accuracy_score(test_y.values, pred_y))


# Experimenting with the values of the columns -  
# Result: The change in the accuracy was marginal. The NN itself choose the features by setting the values of the weights to zero. 

# In[ ]:


from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

train_x, test_x, train_y, test_y = train_test_split(df.drop('Suggested Job Role', axis = 1), df['Suggested Job Role'], test_size = 0.3, shuffle = True)

model = MLPClassifier(activation='tanh', solver = 'sgd',max_iter = 250, hidden_layer_sizes = (256, 128, 64, 32), early_stopping = False, validation_fraction=0.001)
model.fit(train_x.values, train_y.values.ravel())
pred_y = model.predict(test_x.values)
print('Label Encoded')
print("Accuracy Score = ", accuracy_score(test_y.values, pred_y))


# In[ ]:


# from sklearn.model_selection import train_test_split
# from sklearn.neural_network import MLPClassifier
# from sklearn.metrics import accuracy_score

# train_x, test_x, train_y, test_y = train_test_split(df1_without_class.drop('Suggested Job Role', axis = 1), df1_without_class['Suggested Job Role'], test_size = 0.3, shuffle = True)

# model = MLPClassifier(activation='tanh', solver = 'sgd',max_iter = 250, hidden_layer_sizes = (256, 128, 64, 32), early_stopping = False, validation_fraction=0.001)
# model.fit(train_x.values, train_y.values.ravel())
# pred_y = model.predict(test_x.values)

# print('Without Label Encoding')
# print("Accuracy Score = ", accuracy_score(test_y.values, pred_y))


# Performed Grid search to find the best combinations of the parameters 

# In[ ]:


from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import log_loss
from sklearn.model_selection import GridSearchCV

# Using 80:20 split 
train_x, test_x, train_y, test_y = train_test_split(df.drop('Suggested Job Role', axis = 1), df['Suggested Job Role'], test_size = 0.2, shuffle = True)
model1 = MLPClassifier()


pram = {
    'activation' : ['logistic', 'relu', 'tanh', 'identity'],
    'solver' : ['sgd','adam'],
    'hidden_layer_sizes' : [(256, 128, 64, 32, 16),(256, 128, 64, 32),(200, 150, 100, 50),(500, 400, 300, 200)],
    'learning_rate_init' : [0.1, 0.01, 0.001],
    'max_iter' : [100, 250, 500, 750, 1000]
}

grid_m = GridSearchCV(model1, pram, n_jobs= -1, cv = 3)
grid_m.fit(train_x, train_y)

y_pred = grid_m.predict(test_x)

print("Best Estimator: ",grid_m.best_estimator_)
print("Best Score : ", grid_m.best_score_)
print("Best parameters : ",grid_m.best_params_)

y_pred_train = grid_m.predict(train_x)
y_pred_test = grid_m.predict(test_x)
acc_train = accuracy_score(train_y,y_pred_train)
acc_test = accuracy_score(test_y,y_pred_test)

y_prob_train = grid_m.predict_proba(train_x)
y_prob_test = grid_m.predict_proba(test_x)
loss_train = log_loss(train_y,y_prob_train)
loss_test = log_loss(test_y,y_prob_test)

print("Training accuracy : ", acc_train)
print("Testing accuracy : ", acc_test)
print("Training loss", loss_train)
print("Testing loss", loss_test)


# # 60-40 Split

# In[ ]:


# Train Test split 
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(df.drop('Suggested Job Role', axis = 1), df['Suggested Job Role'], test_size = 0.4, shuffle = True)


# In[ ]:


from sklearn.neural_network import MLPClassifier

model = MLPClassifier(activation='tanh', solver = 'sgd',max_iter = 100, hidden_layer_sizes = (64, 32, 16), early_stopping = False, validation_fraction=0.001, verbose = 1)
model.fit(train_x.values, train_y.values.ravel())
pred_y = model.predict(test_x.values)


# In[ ]:


from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

confusionmatrix_60 = confusion_matrix(test_y, pred_y)
print("Confusion matrix = \n",confusionmatrix_60)
print("-------------------------------------------")
print("Accuracy Score = ", accuracy_score(test_y, pred_y))
print("-------------------------------------------")
print("Class wise accuracy")
temp = confusionmatrix_60.diagonal()/confusionmatrix_60.sum(axis=1)
i = 0
for j in temp:
    print("Class "+str(i)+" : "+str(j))
    i = i+1
print("-------------------------------------------")
print("Classification Report")
print(classification_report(test_y, pred_y))


# # 70-30 Split

# In[ ]:


# Train Test split 
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(df.drop('Suggested Job Role', axis = 1), df['Suggested Job Role'], test_size = 0.3, shuffle = True)


# In[ ]:


from sklearn.neural_network import MLPClassifier

model = MLPClassifier(activation='tanh', solver = 'sgd',max_iter = 100, hidden_layer_sizes = (64, 32, 16), early_stopping = False, validation_fraction=0.001, verbose = 1)
model.fit(train_x.values, train_y.values.ravel())
pred_y = model.predict(test_x.values)


# In[ ]:


from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

confusionmatrix_70 = confusion_matrix(test_y, pred_y)
print("Confusion matrix = \n",confusionmatrix_70)
print("-------------------------------------------")
print("Accuracy Score = ", accuracy_score(test_y, pred_y))
print("-------------------------------------------")
print("Class wise accuracy")
temp = confusionmatrix_70.diagonal()/confusionmatrix_70.sum(axis=1)
i = 0
for j in temp:
    print("Class "+str(i)+" : "+str(j))
    i = i+1
print("-------------------------------------------")
print("Classification Report")
print(classification_report(test_y, pred_y))


# # 90-10 Split

# In[ ]:


# Train Test split 
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(df.drop('Suggested Job Role', axis = 1), df['Suggested Job Role'], test_size = 0.1, shuffle = True)


# In[ ]:


from sklearn.neural_network import MLPClassifier

model = MLPClassifier(activation='tanh', solver = 'sgd',max_iter = 100, hidden_layer_sizes = (64, 32, 16), early_stopping = False, validation_fraction=0.001, verbose = 1)
model.fit(train_x.values, train_y.values.ravel())
pred_y = model.predict(test_x.values)


# In[ ]:


from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

confusionmatrix_90 = confusion_matrix(test_y, pred_y)
print("Confusion matrix = \n",confusionmatrix_90)
print("-------------------------------------------")
print("Accuracy Score = ", accuracy_score(test_y, pred_y))
print("-------------------------------------------")

print("Class wise accuracy")
temp = confusionmatrix_90.diagonal()/confusionmatrix_90.sum(axis=1)
i = 0
for j in temp:
    print("Class "+str(i)+" : "+str(j))
    i = i+1
print("-------------------------------------------")
print("Classification Report")
print(classification_report(test_y, pred_y))


# In[ ]:




