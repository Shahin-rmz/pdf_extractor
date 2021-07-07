#!/usr/bin/env python
# coding: utf-8

# In[3]:


from os.path import basename
import fitz
from bs4 import BeautifulSoup
from PIL import Image
import io
import pandas as pd
import os
from natsort import natsorted


# In[4]:


htmltxt = ''
htmlfile2 = open ('htmlfile2.html', 'w+')
doc = fitz.open('govahi.pdf')
for page in doc:
    txt = page.get_text('xhtml') 
    htmltxt = htmltxt + txt
f = htmlfile2.write(htmltxt)
htmlfile2.close()


# In[5]:


file = open('htmlfile.html', 'r')
soup = BeautifulSoup(file.read(),'html.parser')
l = []
for item in soup.select('p[style *= "left:118pt"]'):
    (l.append(item.get_text()))


# In[6]:


df = pd.DataFrame(l)
df.to_csv('names.csv',index = False)


# In[7]:


df2 = pd.read_csv('names_configured2.csv')
df2.columns = ['obj_name']


# In[8]:


fpath = '/home/shahin/3-ComputerProj/projects/pdf_extractor/images_test/'
for file, i in zip(natsorted(os.listdir(fpath)),df2.obj_name.iloc) :
    ext = os.path.splitext(file)[-1].lower()
    if ext == '.png':
        dest = i+'.png'
        source = fpath + file
        dest = fpath + dest
        os.rename(src=source,dst=dest)
    elif ext =='.jpeg':
        dest = i+'.jpeg'
        source = fpath + file
        dest = fpath + dest
        os.rename(source, dest)


# In[ ]:




