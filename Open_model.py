#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 18:21:13 2018

@author: aaron
"""
from gensim.models import Word2Vec
import pandas as pd

def most_similar(w2v_model, words, topn=5):
    similar_df = pd.DataFrame()
    for word in words:
        try:
            similar_words = pd.DataFrame(w2v_model.wv.most_similar(word, topn=topn), 
                                         columns=[word, 'value'])
            similar_df = pd.concat([similar_df, similar_words], axis=1)
        except:
            print(word, "not found in Word2Vec model!")
    return similar_df

if __name__ == "__main__":
    
    model_name = 'data4.model'
    path = '/Users/aaron/Desktop/DataMining/med/chai/'
   
    full = path + model_name 
    model = Word2Vec.load(full)
    print(most_similar(model,['466']))
    print(model.wv['466'])
    print(model.wv['751'])
       
