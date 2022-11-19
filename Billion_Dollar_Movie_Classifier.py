# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 14:12:01 2022

@author: Shobhan Mitra
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# importing data and cleaning NAN value
df1 = pd.read_csv("E:/DaFif/Devpost/AWS Data Exchange for APIs Challenge/data extraction/Billion_data.csv")
df1.Production_Budget_million.fillna(df1.Production_Budget_million.mean(),inplace=True)
print(df1['Production_Budget_million'])


df2 = pd.read_csv("E:/DaFif/Devpost/AWS Data Exchange for APIs Challenge/data extraction/BillionLess_data.csv")
df2.Production_Budget_million.fillna(df2.Production_Budget_million.mean(),inplace=True)
print(df2['Production_Budget_million'])

#concatenating two data set
pdList=[df1, df2]
merged_data=pd.concat(pdList)

print(merged_data)

merged_data.to_csv("E:/DaFif/Devpost/AWS Data Exchange for APIs Challenge/data extraction/merged_data1.csv", index=False)


#importing merged data after auditing

movie_data= pd.read_csv("E:/DaFif/Devpost/AWS Data Exchange for APIs Challenge/data extraction/merged_data5.csv")

#splitting data into train & test

movie_data_train=movie_data.loc[:80,:]
movie_data_test=movie_data.loc[81:,:]


#Also sorting the train data classwise

pos_billion=movie_data_train[movie_data_train['Billion_Dollar_Club']=='pos']
neg_billion=movie_data_train[movie_data_train['Billion_Dollar_Club']=='neg']

#Train the model{Binary classifier,normal,(Bays theory)multivariate,(Multivariate parameter),qudratic discriminator by putting decision threshold 0.5 on posterior probability}.

#Bays theory, post_pos= Likelihood_pos * Prior_Pos/Likelihood_pos* Prior_pos + Likelihood_neg* Prior_neg

#Multivariate, f(x)= 1/(2pip/2 * det sig1/2) e-1/2(x-mu)T * sig**-1(x-mu); we need two parameter mean=mu and cov=sigma

from scipy.stats import multivariate_normal

mu_pos = pos_billion.mean()
mu_neg = neg_billion.mean()

sig_pos = pos_billion.cov()
sig_neg = neg_billion.cov()

#multivariate_normal_pos = multivariate_normal(mu_pos,sig_pos)
#multivariate_normal_neg = multivariate_normal(mu_neg,sig_neg)



movie_data.corr()

multivariate_normal_pos = multivariate_normal(mu_pos,sig_pos)

multivariate_normal_neg = multivariate_normal(mu_neg,sig_neg)

movie_data_train_withoutlebel= movie_data_train.drop(['Billion_Dollar_Club'],axis=1)

prior_pos=len(pos_billion)/(len(pos_billion)+len(neg_billion))
prior_neg=len(neg_billion)/(len(pos_billion)+len(neg_billion))


likelihood_pos=multivariate_normal_pos.pdf(movie_data_train_withoutlebel)
likelihood_neg=multivariate_normal_neg.pdf(movie_data_train_withoutlebel)
post_pos=likelihood_pos*prior_pos/(likelihood_pos*prior_pos+likelihood_neg*prior_neg)
post_neg=likelihood_neg*prior_neg/(likelihood_neg*prior_neg+likelihood_pos*prior_pos)
#If below condition satisfied then it will be true otherwise false. Thats  whyy control thresholed kept as 0.5.
pred= post_pos>post_neg
pred

###Converting label as TRUE/FALSE from pos/neg to compare the string length for accuracy measurement purpose at next stage
##(since the pred outcome is bullian as TRUE/FALSE as we saw at previous stage)
labels = movie_data_train['Billion_Dollar_Club']
labels

labels[labels=='pos'] = True
labels[labels=='neg'] =False

labels

#Training Error

#if lebels & Predict have same string then = sum their numbers. *** index of both pred & lebels is True.But *** pred is true Lebel is false. 
#Then divide by total number of that string in Pred. This will give accuracy.


(sum((labels == pred))/len(pred))*100

#Testing

movie_data_test_withoutlebel= movie_data_test.drop(['Billion_Dollar_Club'],axis=1)
likelihood_pos=multivariate_normal_pos.pdf(movie_data_test_withoutlebel)
likelihood_neg=multivariate_normal_neg.pdf(movie_data_test_withoutlebel)
post_pos=likelihood_pos*prior_pos/(likelihood_pos*prior_pos+likelihood_neg*prior_neg)
post_neg=likelihood_neg*prior_neg/(likelihood_neg*prior_neg+likelihood_pos*prior_pos)

pred= post_pos>post_neg
pred

#Testing Error
labels = movie_data_test['Billion_Dollar_Club']
labels[labels=='pos'] = True
labels[labels=='neg'] = False


(sum((labels == pred))/len(pred))*100

#####TESTING :- WILL A MOVIE EARN BILLION DOLLAR OR NOT


% movie data
%            [Rating, Production_Budget_million] 
movie_data=[1,20]

likelihood_pos=multivariate_normal_pos.pdf(movie_data)
likelihood_neg=multivariate_normal_neg.pdf(movie_data)
post_pos=likelihood_pos*prior_pos/(likelihood_pos*prior_pos+likelihood_neg*prior_neg)
post_neg=likelihood_neg*prior_neg/(likelihood_neg*prior_neg+likelihood_pos*prior_pos)

pred= post_pos>post_neg
pred



