#!/usr/bin/env python
# coding: utf-8

# In[22]:


import cv2

img_source = "1612952485.jpeg" #Need Change Name of file

img = cv2.imread(img_source)

cv2.imshow('OMG',img)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:


import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img_source = "1612952485.jpeg" #Need Change Name of file

img = cv2.imread(img_source)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
)

for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('OMG',img)
cv2.waitKey()
cv2.destroyAllWindows()

#Not_work_in_png_or_jpeg_ect
#Not_work_in_too_big_or_small_size
#Could_not_work_in_some_situation

