#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import os
import time 
import uuid
import pandas as pd


# In[4]:


IMAGES_PATH = 'Tensorflow/workspace/images/collectedimages'


# In[8]:


labels=['HELLO','BYE','HELP','ILOVEYOU','YES','NO','OK','STOP','THANKYOU','PLAY']
number_imgs=20,


# In[9]:


for label in labels:
    get_ipython().system("mkdir {'Tensorflow\\workspace\\images\\collectedimages\\\\'+label}")
    cap=cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH, label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame )
        cv2.imshow('frame',frame)
        time.sleep(2)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()


# In[ ]:




