# finding duplicates in the list and replace it with the 10
from array import*
term=array('i',[])
term.insert(0,10)
term.insert(1,20)
term.insert(2,10)
term.insert(3,30)
for i in range(1,len(term)):
    for j in range(2,len(term)):
        if term[i]==term[j]:
            term[i]+=10
    print(term[i])
