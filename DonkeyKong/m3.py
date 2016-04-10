import m2
import random
l=[]
def f():
   l=m2.f()
   l1=list(l[28])
   l1[1]='P'
   l[28]="".join(l1)
   i=0
   while i<20:
	x=random.randint(4,28)
	y=random.randint(1,60)
	if (l[x][y]==' ' and (l[x+1][y]=='X' or (l[x+1][y]=='H' and l[x-1][y]==' '))):
		l1=list(l[x])
		l1[y]='C'
		l[x]="".join(l1)
	else:
		i=i-1
	i=i+1
   return l
