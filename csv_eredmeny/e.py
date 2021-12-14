from os import system
from func import *
system('cls')
''' Előző heti eredmények '''
hely = input("Kérek egy felhasználónevet: ")
tomb = beolvas(hely)
print(tomb[0:2])
''' Legtöbb előfordulás '''
db = 0
sorsonly = []
le_tomb = []
for x in tomb:
    for z in x[1]:
        sorsonly.append(z)
for y in range(1,100):
    t = []
    db = 0
    for x in sorsonly:
        if x==y:
            db+=1
    t.append(y)
    t.append(db)
    le_tomb.append(t)
print(sorted(le_tomb, key=lambda x: x[1], reverse=True)[0:3])
del le_tomb
''' Legkisebb összeg '''
print(sorted(tomb, key=lambda x: x[2])[0:3])
''' Hasonló számsorok '''
t = []
for x in range(1, 100):
    for y in tomb:
        temp = []
        db = 0
        for z in y[1]:
            if len(str(z))==1:
                if str(z)==str(x):
                    db+=1
            else:
                if str(z)[1]==str(x):
                    db+=1
        if db>3:
            temp.append(y[0])
            temp.append(y[1])
            temp.append(db)
        if len(temp)>0:
            t.append(temp)
print(sorted(t, key=lambda x: x[2], reverse=True))
del t
''' Sorozatok '''
t = []
for x in tomb:
    for y in range(1,25):
        db = 0
        if x[1][0]+y==x[1][1]:
            db+=1
            if x[1][1]+y==x[1][2]:
                db+=1
                if x[1][2]+y==x[1][3]:
                    db+=1
                    if x[1][3]+y==x[1][4]:
                        db+=1
        if db>2:
            print(x[1])