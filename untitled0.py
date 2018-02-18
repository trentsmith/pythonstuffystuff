import numpy as np
import cv2
import matplotlib.pyplot as plt
import Tkinter as tk
import sqlite3
conn = sqlite3.connect('pictures.db')
c = conn.cursor()
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS pictures(name, pic)')
def data_entry():
    name = raw_input('what is name of pic? /n')
    pic = raw_input('what is the location???/n')
    c.execute('INSERT INTO pictures(name,pic)VALUES(?,?)',(name,pic))
    conn.commit()
create_table()
cap = cv2.VideoCapture(0)
r=250
h=90
c=400
w=125  # simply hardcoded the values
track_window = (c,r,w,h)
x = 50
y = 40
while(True):
    ret, frame = cap.read()
    roi = frame[0:100,0:100]
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    lines = cv2.HoughLines(edges,1,np.pi/180,200)
    mask = cv2.inRange(hsv, np.array((50., 50.,50.)), np.array((255.,255.,255.)))
    #cv2.circle(frame,(x,y), 63,(255,0,255), -1)
    iar = np.asarray(mask)    
    i =0
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
        c.execute('Select * FROM pictures WHERE name = ?',(x))
        print(c.fetchall())
    if (cv2.waitKey(1) & 0xFF == ord('2')):
        data_entry()
    if (cv2.waitKey(1) & 0xFF == ord('3')):
        c.close()
        break
    if (cv2.waitKey(1) & 0xFF == ord('4')):
        x = input('what is the input you want to delete??')
        c.execute('DELETE FROM pictures WHERE name = '+x)
    cv2.imshow('frame',mask)
cap.release()
cv2.destroyAllWindows()