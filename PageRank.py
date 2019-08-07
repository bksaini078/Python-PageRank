#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

def adjacencyMatrix(Nodes_Detail,Connec_Details):#,Connec_Details
    length_M=len(Nodes_Detail)
    #print(length_M)
    #creating Adjacency Matrix with 0 connections
    Adj_Matrix=[]
    for i in range(length_M):#Adjacency Matrix created with no connection in between
        Adj_Matrix.append([0 for j in range(length_M)])
    for l in Connec_Details:
    #    print(l)
        u= Nodes_Detail.index(l[0])#taking index of node for row
        v= Nodes_Detail.index(l[1])#taking index of node for column
        Adj_Matrix[u][v]=1 #adding the values 
 
    return Adj_Matrix

Nodes=["A","B","C","D","E"]# index of these are same as index in adjancency Matrix 
Connectn_Details= [["A","A"],["A","C"],["A","E"],["B","D"],["B","E"],["C","A"],["C","E"],["D","D"],["D","E"],["E","A"]]
adj_Matrix=adjacencyMatrix(Nodes,Connectn_Details)

print(adj_Matrix)
len(adj_Matrix)

adj_Matrix


# In[2]:


def deg_Calc(adjMatrix):# function to calculate in degree and out degree
    lengthOfMatrix=len(adjMatrix)
    outdegree=[]
    indegree=[]
   #counting out degree
    for i in range(lengthOfMatrix):
        temp=0
        for j in range(lengthOfMatrix):
            temp= adjMatrix[i][j]+temp
        outdegree.append(temp)
   
    #calculating in degree
    for i in range(lengthOfMatrix):
        temp=0
        for j in range(lengthOfMatrix):
            temp= adjMatrix[j][i]+temp
        indegree.append(temp)
        #print(indegree)
    return outdegree, indegree
            
o_Degree,in_Degree=deg_Calc(adj_Matrix) 

degree_df=pd.DataFrame(o_Degree,Nodes,columns=['Outdegree'])
degree_df['Indegree']= in_Degree
degree_df


# In[3]:


def stm_Calc(adjMatrix,alpha):#calculating stochastic matrix
    sto_PMatrix=[]
    o_Degree,in_Degree=deg_Calc(adj_Matrix) 
    lengthM=len(adj_Matrix)
    for i in range(len(adj_Matrix)):
        x=[];
        for j in range(len(adj_Matrix)):
            if o_Degree[i]==0:#if degree is zero
                x.append(1/lengthM)
            elif adj_Matrix[i][j]==0 :#if no links from i to j
                x.append(alpha/lengthM)
            else:#otherwise
                y = round((alpha/lengthM)+(1-alpha)*(1/o_Degree[i]),2)#transition probability
                x.append(y)
        sto_PMatrix.append(x)
    #print(sto_PMatrix)
    return sto_PMatrix
stochastic_PMatrix =stm_Calc(adj_Matrix,0.1)#alpha is 0.1 

degree_df['Stochastic Matrix']= stochastic_PMatrix

degree_df


# In[6]:


import numpy as np #just for matrix multiplication 
def rank_Calc(stm_P,x):#power iteration function to calculate page rank or eigen values # X is iterative variable 
    x_old=[]
    length= len(stm_P)
    for i in range(length):#creating matrix of 1
        x_old.append(1/length)
    #Power iteration 
    x_new=[]
    for i in range(x):# Normalization is not required for small matrix
        x_new= np.matmul(x_old,stm_P)
   
        x_old=x_new
    return x_new 
#page rank        
page_Rank =rank_Calc(stochastic_PMatrix,5)#we can increase the value for more accuracy

degree_df['Page Rank']= page_Rank
degree_df


# In[ ]:




