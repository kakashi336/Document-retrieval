import pandas as pd
import math
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer


def computeTF(WordDict,BoW):
    tfDict={}
    for words,count in WordDict.items():
        tfDict[words]=count/len(BoW)
    return tfDict

def computeIDF(docs):
    idfDict=dict.fromkeys(docs[0],0)
    N=len(docs)
    for documents in docs:
        for word,val in documents.items():
            if val>0:
                idfDict[word]+=1
    for word,val in idfDict.items():
        idfDict[word]=math.log(N/float(val))
    print(idfDict)
    return idfDict

def computeTFIDF(TF,IDF):
    tfidf={}
    for words,val in TF.items():
        tfidf[words]=val*IDF[words]
    print(tfidf)
    return tfidf

documentA ='sample text 1'
documentB="sample text 2"

BowA=documentA.split()
BowB=documentB.split()
uniqueWords=set(BowA).union(set(BowB))

numOfWordsA=dict.fromkeys(uniqueWords,0)
numOfWordsB=dict.fromkeys(uniqueWords,0)

for words in BowA:
    numOfWordsA[words]+=1
for w in BowB:    
    numOfWordsB[w]+=1


tfA = computeTF(numOfWordsA,BowA)
tfB = computeTF(numOfWordsB,BowB)

idfs = computeIDF([numOfWordsA, numOfWordsB])

a=computeTFIDF(tfA,idfs)
b=computeTFIDF(tfB,idfs)
