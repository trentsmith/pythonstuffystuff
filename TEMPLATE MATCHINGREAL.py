import numpy as np
import cv2
import matplotlib.pyplot as plt
import Tkinter as tk
import sqlite3
conn = sqlite3.connect('pictures.db')
c = conn.cursor()
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS picture(name TEXT, pic BLOB)')
def data_entry():
    name = raw_input('what is name of pic? /n')
    pic = raw_input('what is the location???/n')
    c.execute('INSERT INTO picture(name,pic)VALUES(?,?)',(name,pic))
    conn.commit()
def pic_finder():
        x= raw_input('what is the image you want to look for???')
        for row in c.execute('Select pic FROM picture WHERE name = ?',(x)):
            variable = row[0]
            break
        else:
            variable = 0
create_table()
cap = cv2.VideoCapture(0)
r=250
h=90
c=400
w=125  # simply hardcoded the values
#pic_finder()
track_window = (c,r,w,h)
x = 50
y = 40
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    template = cv2.imread(sql)#SQL ENTRY
    w,h=template.shape[::-1]
    res =cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
    loc=np.where(res>=threshold)
    i =0
    while i < len(frame):
        j=0
        while j<len(frame[i]):
            #insert the template matching in opencv
            j=j+1
        i=i+1
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        c.close()
        break
    if (cv2.waitKey(1) & 0xFF == ord('a')):
        x = x-10
    if (cv2.waitKey(1) & 0xFF == ord('s')):
        y = y-10
    if (cv2.waitKey(1) & 0xFF == ord('d')):
        x = x+10
    if (cv2.waitKey(1) & 0xFF == ord('w')):
        y = y+10
    if (cv2.waitKey(1) & 0xFF == ord('1')):
        x= raw_input('what is the image you want to look for???')
        c.execute('Select * FROM picture WHERE name = ?',(x))
        print(c.fetchall())
    if (cv2.waitKey(1) & 0xFF == ord('2')):
        data_entry()
    if (cv2.waitKey(1) & 0xFF == ord('3')):
        c.close()
        break
    if (cv2.waitKey(1) & 0xFF == ord('4')):
        pic_finder()
    cv2.imshow('frame',res)
cap.release()
cv2.destroyAllWindows()