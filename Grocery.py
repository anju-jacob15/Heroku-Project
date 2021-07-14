#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from apyori import apriori
import matplotlib.pyplot as plt
from flask import Flask,request,jsonify,render_template


# In[3]:


data = pd.read_csv("basket.csv")


# In[4]:


transactions=[]  
for i in range(0, 14962):  
    transactions.append([str(data.values[i,j])  for j in range(0,3)])


# In[5]:


rules=apriori(transactions=transactions,min_support=0.00001,min_confidence = 0.1, min_lift=1, min_length=2, max_length=2)


# In[6]:


results = list(rules)
len(results)


# In[7]:


def all1():
    outputArray=[]
    for item in results: 
        pair = item[0]   
        items = [x for x in pair]  
        
        if len(items) > 1:
            output=items[0],items[1],str(item[1]),str(item[2][0][2]),str(item[2][0][3])
            outputArray.append(output)       
    return outputArray


# In[8]:


def specific(abc):
    outputArray=[]
    for item in results:  
        pair = item[0]   
        items = [x for x in pair]  
        
        if(len(items) > 1 and items[0] == abc): 
            output=items[0],items[1],str(item[1]),str(item[2][0][2]),str(item[2][0][3])
            outputArray.append(items[1])
    return outputArray     


# In[ ]:


# start flask
app = Flask(__name__)

# render default webpage
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate',methods=['POST'])
def calculate():
    
    val2=request.form['value2']
    
    
    if request.form['submit_button'] == 'View All Datasets':
        ret1=all1()
        return render_template('index.html',prediction_test1='Following is the output {}'.format(ret1))
        
    if request.form['submit_button'] == 'Submit':
        ret2=specific(val2)
        return render_template('index.html',prediction_test2='Following is the output {}'.format(ret2))

    return 
    
    
if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




