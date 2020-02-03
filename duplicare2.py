# duplicates
from array import *
term=array('i',[])
a=array('i',[])
term.insert(0,10)
term.insert(1,10)
term.insert(2,20)
term.insert(3,30)
num=int(input("enter the number"))
for i in range(0,len(term)):
    for j in range(1,len(term)):
        if term[i]==term[j]:
            if term[i]/num:
                a.append(term[i])
    print(term[i])
for each in range(0,len(a)):
        print(a)
