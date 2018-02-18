# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 16:15:44 2017

@author: Bruce Wayne
"""
print("what is the phrase??")
subjects = []
x=raw_input()
x = x.replace(",","")
x = x.replace(".","")
x=x.split(" ")
i = 0 
m=0
while i <len(x):
    if str(x[i]).find("the")!=-1:
        subjects.append(x[i+1])
        print("found i is :"+str(subjects[m]))
        m=m+1
    if str(x[i]).find("is")!=-1:
        x.remove("is")
    i=i+1
print (subjects)
def verb_Finder():
    return 1