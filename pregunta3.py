from random import *
l= []
y=[]
m=[]
n=0
con=0
while con<6:
    con = con +1
    n = int(input("Ingrese un numero"))
    if n>=1 and n<=10:
        m.append(n)
print(m)
a = m[0]
b= m[1]
c = m[2]
d =m[3]
e = m[4]
f= m[5]
for i in range(6):
    
    h =randint(1,10)
    l.append(h)

       
print(l)
print(y)




