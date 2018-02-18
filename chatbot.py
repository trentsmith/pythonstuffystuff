import sqlite3
import datetime
conn=sqlite3.connect('robot1.db')
c = conn.cursor()
p=0
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS randomq(questions TEXT,job TEXT, age TEXT,input TEXT)')
def data():
    x=raw_input('HELLO MY NAME IS NOISEBOT what do you want to talk about???')
    mainloop(x)
def remove(x):
    #decodes the unicode
    x = x[2:]
    x = x[:-1]
    return x
def mainloop(x):
    p=0
    #add a closing statement
    z = raw_input('what is your job??')
    a = raw_input('what is your age??')
    while(p!=1):
        try:
            remove(x)
            c.execute('SELECT questions FROM randomq where job = '+z+'AND age = '+a+'AND input= '+x)
            print(c.fetchall())
            x=raw_input()
        except:
            print("what should I say???")
            y = raw_input()
            print('what is your response')
            x=raw_input()
            c.execute('INSERT INTO randomq(job,age,questions,input)VALUES(?,?,?,?)',(z,a,y,x))
create_table()
data()