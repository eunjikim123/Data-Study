#!/usr/bin/env python
# coding: utf-8

# In[109]:


import pandas as pd

star_wars = pd.read_csv('star_wars.csv', encoding='ISO-8859-1')
star_wars.head(10)


# In[110]:


star_wars.columns


# In[111]:


star_wars['Have you seen any of the 6 films in the Star Wars franchise?'].value_counts()


# In[112]:


star_wars['Do you consider yourself to be a fan of the Star Wars film franchise?'].value_counts()


# In[113]:


yes_no = {
    "Yes":True,
    "No":False
}

star_wars['Have you seen any of the 6 films in the Star Wars franchise?'] = star_wars['Have you seen any of the 6 films in the Star Wars franchise?'].map(yes_no)
star_wars['Do you consider yourself to be a fan of the Star Wars film franchise?'] = star_wars['Do you consider yourself to be a fan of the Star Wars film franchise?'].map(yes_no)


# In[114]:


star_wars['Do you consider yourself to be a fan of the Star Wars film franchise?'].value_counts()


# In[115]:


import numpy as np
yes_no = {
    "Star Wars: Episode I  The Phantom Menace":True,
    np.nan:False
}
star_wars['Which of the following Star Wars films have you seen? Please select all that apply.'] = star_wars['Which of the following Star Wars films have you seen? Please select all that apply.'].map(yes_no)


# In[116]:


star_wars['Which of the following Star Wars films have you seen? Please select all that apply.']


# In[117]:


star_wars = star_wars.rename(columns=
                            {"Which of the following Star Wars films have you seen? Please select all that apply.": "seen_1"})


# In[118]:


star_wars['seen_1']


# In[119]:


star_wars['Unnamed: 5']


# In[121]:


# 시리즈 이름 담아두기
# 해당 시즌을 봤으면 True , 아니면 False
# 비어있는 컬럼이름 see_~ 로 변경하기

list = ['Star Wars: Episode II  Attack of the Clones','Star Wars: Episode III  Revenge of the Sith','Star Wars: Episode IV  A New Hope','Star Wars: Episode V The Empire Strikes Back','Star Wars: Episode VI Return of the Jedi']
count = 4
num = 2
for i in list:
    
    yes_no = {
    i:True,
    np.nan:False
    }
    
    name = f"Unnamed: {count}"
    star_wars[name] = star_wars[name].map(yes_no) 
    star_wars = star_wars.rename(columns=
                            {name: f"seen_{num}"})
    count +=1
    num +=1 
        
    
    
    
    
    
   


# In[122]:


star_wars.head()


# In[123]:


star_wars[star_wars.columns[9:15]] = star_wars[star_wars.columns[9:15]].astype(float)


# In[127]:


star_wars.columns[9]


# In[131]:


num = 1
for i in range(9,15):
    name = star_wars.columns[i]    
    star_wars = star_wars.rename(columns={name:f"ranking_{num}"})
    num+=1


# In[148]:


star_wars[star_wars.columns[9:15]].mean()


# In[135]:


star_wars.mean()


# In[134]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[149]:


import matplotlib.pyplot as plt
plt.bar(star_wars.columns[9:15],star_wars[star_wars.columns[9:15]].mean()) 
plt.show()


# In[156]:


star_wars.columns[3:9]


# In[157]:


plt.bar(star_wars.columns[3:9],star_wars[star_wars.columns[3:9]].sum()) 
plt.show()


# In[158]:


male = star_wars[star_wars['Gender'] == "Male"]
male


# In[164]:


plt.bar(male.columns[3:9],male[male.columns[3:9]].sum()) 
plt.show()


# In[165]:


female = star_wars[star_wars['Gender'] == "Female"]
female


# In[166]:


plt.bar(female.columns[3:9],female[female.columns[3:9]].sum()) 
plt.show()


# In[ ]:




