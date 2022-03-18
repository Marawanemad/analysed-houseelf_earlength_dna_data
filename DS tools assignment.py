#!/usr/bin/env python
# coding: utf-8


# In[12]:


import pandas as pd
data = pd.read_csv("C:\\Users\\leader tech\\Desktop\\houseelf_earlength_dna_data.csv")
df = pd.DataFrame(data)
df


# In[13]:


# loop to show the size of ears
length=[]
Id = []
DNAseq=[]
for i in range(len(df)) :
    Id.append(df.loc[i,"id"])
    DNAseq.append(df.loc[i,"dnaseq"])
    if(df.loc[i, "earlength"]>10):
        length.append('large')
        print(df.loc[i, "earlength"] , "large")
    else:
        length.append('small')
        print(df.loc[i, "earlength"] , "small")
    
# add length to data frame
df["length"] = length


# In[14]:


# calculate averagare 
sum_l=0 ; sum_s=0 ; l=0; s=0 ;
for i in range(len(df)) :
    if(df.loc[i, "earlength"]>10):
        sum_l = sum_l + df.loc[i, "earlength"]
        l = 1+l
    else:
        sum_s = sum_s + df.loc[i, "earlength"]
        s = s+1
print("large-eared average = ",(sum_l/l))
print("small-eared average = ",(sum_s/s))


# In[15]:


df.drop('earlength',axis=1,inplace=True)
df


# In[16]:


# turn file to csv file
df.to_csv("assignment1.csv")

