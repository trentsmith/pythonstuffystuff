# -*- coding: utf-8 -*-
"""
Created on Wed Aug 09 21:46:39 2017

@author: Bruce Wayne
"""

import cv2
import numpy as np
img_bgr = cv2.imread("")
img_gray = cv2.cvtColor(img_bgr,cv2_BGR2GRAY)
template = cv2.imread("")
w,h=template.shape[::-1]
res =cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
loc=np.where(res>=threshold)
#for pt in zip(*loc[::-1]):
#    cv2.rectangle(img_bgr,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)
cv2.imshow("hello",img_bgr)