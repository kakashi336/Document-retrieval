#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer


# In[7]:


documentA = 'the man went out for a walk'
documentB="the man went out but he never came back coz he dead motherfucerrrr"


# In[8]:


BowA=documentA.split()
BowB=documentB.split()
uniqueWords=set(BowA).union(set(BowB))


# In[9]:


numOfWordsA=dict.fromkeys(uniqueWords,0)
numOfWordsB=dict.fromkeys(uniqueWords,0)

for words in BowA:
    numOfWordsA[words]+=1
for w in BowB:    
    numOfWordsB[w]+=1


# In[10]:


def computeTF(WordDict,BoW):
    tfDict={}
    for words,count in WordDict.items():
        tfDict[words]=count/len(BoW)
    return tfDict
tfA = computeTF(numOfWordsA,BowA)
tfB = computeTF(numOfWordsB,BowB)


# In[11]:


def computeIDF(docs):
    idfDict=dict.fromkeys(docs[0],0)
    import math
    N=len(docs)
  #  print(docs,N)
    for documents in docs:
        for word,val in documents.items():
            if val>0:
                idfDict[word]+=1
  #  print(idfDict)
    for word,val in idfDict.items():
        idfDict[word]=math.log(N/float(val))
    print(idfDict)
    return idfDict

idfs = computeIDF([numOfWordsA, numOfWordsB])


# In[ ]:





# In[12]:


def computeTFIDF(TF,IDF):
    tfidf={}
    for words,val in TF.items():
        tfidf[words]=val*IDF[words]
    print(tfidf)
    return tfidf
a=computeTFIDF(tfA,idfs)
b=computeTFIDF(tfB,idfs)


# In[ ]:





# In[ ]:




