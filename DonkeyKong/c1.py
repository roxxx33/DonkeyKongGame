import m2
import m3
import time
import os,sys,random
from threading import Thread

class Person:
	def __init__(self,pos_x,pos_y):
		self.pos_x=pos_x
		self.pos_y=pos_y
	def move_left(self,c,prev):
		l=list(m3.l[self.pos_x])
		l[self.pos_y]=prev
		prev=l[self.pos_y-1]
		l[self.pos_y-1]=c
		m3.l[self.pos_x]="".join(l)
		self.pos_y-=1
		if c == 'D' or c == 'O':
			return prev
	def move_right(self,c,prev):
		l=list(m3.l[self.pos_x])
		l[self.pos_y]=prev
		prev=l[self.pos_y+1]
		l[self.pos_y+1]=c
		m3.l[self.pos_x]="".join(l)
		self.pos_y+=1
		if c == 'D' or c =='O':
			return prev
	def checkWall(self):
		return 'checking for dead end'
	def getPostion(self):
		return self.pos_x+":"+self.pos_y
	def get_x(self):
		return self.pos_x
	def get_y(self):
		return self.pos_y

class Common:
	def move_down(self,prev,c):
		l1=list(m3.l[self.pos_x+1])
		l2=list(m3.l[self.pos_x])
		l2[self.pos_y]=prev
		prev=l1[self.pos_y]
		l1[self.pos_y]=c
		m3.l[self.pos_x+1]="".join(l1)
		m3.l[self.pos_x]="".join(l2)
		self.pos_x+=1
		if c == 'O':
			return prev

class Player(Person,Common):
	def __init__(self,lives,score,pos_x,pos_y,coins):
		self.__lives=lives
		self.__score=score
		self.pos_x=pos_x
		self.pos_y=pos_y
		self.__coins=coins
	def move_up(self,prev):
		l1=list(m3.l[self.pos_x-1])
		l2=list(m3.l[self.pos_x])
		l1[self.pos_y]='P' 
		l2[self.pos_y]=prev
		m3.l[self.pos_x-1]="".join(l1)
		m3.l[self.pos_x]="".join(l2)
		self.pos_x-=1
	def jump(self,direction,prev):
		if direction == "left":
			flag=0
	       		l1=[]
	 		l1.append(m3.l[self.pos_x][self.pos_y-3])
 			l1.append(m3.l[self.pos_x-1][self.pos_y-3])	 
			l1.append(m3.l[self.pos_x-1][self.pos_y-2])
			l1.append(m3.l[self.pos_x-2][self.pos_y-2])
			l1.append(m3.l[self.pos_x-1][self.pos_y-2])
			l1.append(m3.l[self.pos_x-1][self.pos_y-1])
		        l1.append(m3.l[self.pos_x][self.pos_y-1])
			l1.append(prev)
			if m3.l[self.pos_x+1][self.pos_y-4] == 'X' or m3.l[self.pos_x+1][self.pos_y-4] == 'H': 
				flag = 1
			self.move_left('P',l1.pop())
			self.move_up(l1.pop())
			time.sleep(0.5)
			self.move_left('P',l1.pop())
			self.move_up(l1.pop())
			time.sleep(0.5)
			self.move_down(l1.pop(),'P')
			self.move_left('P',l1.pop())
			time.sleep(0.5)
			self.move_down(l1.pop(),'P')
			self.move_left('P',l1.pop())
			if flag == 0:
				l1=[]
				l1=list(m3.l[self.pos_x])
				l1[self.pos_y] = ' '
				m3.l[self.pos_x] = "".join(l1)
				if m3.l[self.pos_x+4][self.pos_y] == 'C':
					self.collectCollision()
				l1=list(m3.l[self.pos_x+4])
				l1[self.pos_y] = 'P'
				m3.l[self.pos_x+4]="".join(l1)
				self.pos_x+=4
		else:
			flag=0
			l1=[]
			l1.append(m3.l[self.pos_x][self.pos_y+3])
			l1.append(m3.l[self.pos_x-1][self.pos_y+3])
			l1.append(m3.l[self.pos_x-1][self.pos_y+2])
			l1.append(m3.l[self.pos_x-2][self.pos_y+2])
			l1.append(m3.l[self.pos_x-1][self.pos_y+2])
			l1.append(m3.l[self.pos_x-1][self.pos_y+1])
		        l1.append(m3.l[self.pos_x][self.pos_y+1])
			l1.append(prev)
			if m3.l[self.pos_x+1][self.pos_y+4] == 'X' or m3.l[self.pos_x+1][self.pos_y+4] == 'H': 
				flag = 1
			self.move_right('P',l1.pop())
			self.move_up(l1.pop())
			time.sleep(0.5)
			self.move_right('P',l1.pop())
			self.move_up(l1.pop())
			time.sleep(0.5)
			self.move_down(l1.pop(),'P')
			self.move_right('P',l1.pop())
			time.sleep(0.5)
			self.move_down(l1.pop(),'P')
			self.move_right('P',l1.pop())

			if flag == 0:
				l1=[]
				l1=list(m3.l[self.pos_x])
				l1[self.pos_y] = ' '
				m3.l[self.pos_x] = "".join(l1)
				if m3.l[self.pos_x+4][self.pos_y] == 'C':
					self.collectCollision()
				l1=list(m3.l[self.pos_x+4])
				l1[self.pos_y] = 'P'
				m3.l[self.pos_x+4] = "".join(l1)
				self.pos_x+=4
				
	def get_coins(self):
		return self.__coins
	def get_score(self):
		return self.__score
	def get_lives(self):
		return self.__lives
	def collectCoin(self):
		self.__coins+=1
		self.__score+=5
							
	def checkCollision(self):
		if self.__lives>0:
			if m3.l[self.pos_x][self.pos_y-1] == 'O' or m3.l[self.pos_x][self.pos_y+1] == 'O' or m3.l[self.pos_x-1][self.pos_y] == 'O' or m3.l[self.pos_x+1][self.pos_y] == 'O':
				self.__lives=self.__lives-1
				return 1
		else:
			return 2		
		
	def checkWall(self,direction):
		if direction == "left":
			if m3.l[self.pos_x][self.pos_y-1]=='X':
				return 1
		elif m3.l[self.pos_x][self.pos_y+1]=='X':
				return 1
		else:
				return 0

class Donkey(Person):
	def __init__(self,pos_x,pos_y):
		self.pos_x=pos_x
		self.pos_y=pos_y
	def checkWall(self,di):
		if m3.l[self.pos_x][self.pos_y-1]=='X' or m3.l[self.pos_x+1][self.pos_y-1] == ' ':
				return "right"
		elif m3.l[self.pos_x][self.pos_y+1]=='X' or m3.l[self.pos_x+1][self.pos_y+1] == ' ':
				return "left"
		else:
			lis = ["right","left"]
			return (lis[random.randint(0,1)])

class Board:
	def __init__(self,level):
		self.__level=level
	def layout(self,p):
		for i in m3.l:
			print i
		score = p.get_score()
		coins = p.get_coins()
		lives = p.get_lives()
		print "LEVEL = "+str(self.__level)
		print "SCORE = "+str(score)
		print "COINS COLLECTED = "+str(coins)
		print "LIVES = "+str(lives)
	def get_level(self):
		return self.__level

class Fireball(Person,Common):
	count=-1
	def __init__(self,pos_x,pos_y):
		self.pos_x=pos_x
		self.pos_y=pos_y
	def checkWall(self,direction):
		print "haha"
		if self.pos_y-1=='X':
			if self.pos_x == 28 and self.pos_y == 1:
				return "terminate"
			elif m3.l[self.pos_x+1][self.pos_y] == 'H' or m3.l[self.pos_x-1][self.pos_y] == 'H':
				return "down"
			else:
				return "right"
		
		elif self.pos_y+1=='X':
			if m3.l[self.pos_x+1][self.pos_y] == 'H' or m3.l[self.pos_x-1][self.pos_y] == 'H':
				return "down"
			else:
				return "left"
		else:
			self.dire(direction)

	def dire(self,direction):
		print direction
		if (m3.l[self.pos_x-1][self.pos_y] == ' ' and m3.l[self.pos_x-2][self.pos_y] == 'H') or m3.l[self.pos_x-1][self.pos_y] == 'H':
			if m3.l[self.pos_x+1][self.pos_y] == 'X':
				l=['left','right']
				x=random.randint(0,1)
				return l[x]
			elif m3.l[self.pos_x+1][self.pos_y] == 'H':
				return "down" 

		elif m3.l[self.pos_x+1][self.pos_y] == ' ': 
			return "down"
		
		elif(m3.l[self.pos_x+1][self.pos_y] == 'X' and direction == "down"):
			l=['left','right']
			x=random.randint(0,1)
			return l[x]
		else:
			return direction
		print "mama"

def main(level,lives,score,coins):
	global p,r,b,d
	m3.l = m3.f()
	b = Board(level)
	p = Player(lives,score,m2.board_height-2,1,coins)

	if m3.l[5][1] == ' ':
		y = m2.board_width-2
	else:
		y = 1	
	d=Donkey(4,y)
	r = 1

main(1,3,0,0)

direct=[]
pre=[]
templ=[]
f=[]

def f0():
	l=[]
	global pre,templ,f,direct
	global r,d,p,b
	while r:
		d_x=d.get_x()
		d_y=d.get_y()
		x=random.randint(0,2)
		if x == 0:
			Fireball.count+=1
			templ.append(Fireball.count)
			if m3.l[d_x][d_y-1] == 'X':
				pre.append(m3.l[d_x][d_y+1])
				direct.append("right")
				l1=list(m3.l[d_x])
				l1[d_y+1]='O'
				m3.l[d_x]="".join(l1)
				f.append(Fireball(d_x,d_y+1))
			elif m3.l[d_x][d_y+1] == 'X':
				pre.append(m3.l[d_x][d_y-1])
				direct.append("left")
				l1=list(m3.l[d_x])
				l1[d_y-1]='O'
				m3.l[d_x]="".join(l1)
				f.append(Fireball(d_x,d_y-1))
			else:
				y=random.randint(0,1)
				if y == 0:
					pre.append(m3.l[d_x][d_y-1])
					direct.append("left")
					l1=list(m3.l[d_x])
					l1[d_y-1]='O'
					m3.l[d_x]="".join(l1)
					f.append(Fireball(d_x,d_y-1))
				else:
					pre.append(m3.l[d_x][d_y+1])
					direct.append("right")
					l1=list(m3.l[d_x])
					l1[d_y+1]='O'
					m3.l[d_x]="".join(l1)
					f.append(Fireball(d_x,d_y+1))
		print direct[0]
		print "yahoo"

		for i in templ:
#			print direct[i]+"before"
			direct[i]=f[i].checkWall(direct[i])
#			print direct[i]
			if direct[i] == "left":
				pre[i]=f[i].move_left('O',pre[i])
			elif direct[i] == "right":
				pre[i]=f[i].move_right('O',pre[i])
			elif direct[i] == "down":
				pre[i]=f[i].move_down(pre[i],'O')
			elif direct[i] == "terminate":
				l=list(m3.l[28])
				l[1]=pre[i]
				m3.l[28]="".join(l)
				templ.remove(i)
		os.system('clear')
		b.layout(p)
		time.sleep(0.3)

def f1():			
	global p,b,d,r
	pr=' '
	di=''
	while r:
		d_x=d.get_x()
		d_y=d.get_y()	
		
		di = d.checkWall(di)
		if di == "right":
			pr=d.move_right('D',pr)
		else:
			pr=d.move_left('D',pr)
		os.system('clear')
		b.layout(p)
		time.sleep(0.3)
br_st=0
def f2():
	global p,r,b,br_st
	choice='t' 
	while choice!='q':
		flag=0
		os.system('clear')
		b.layout(p)
		level=b.get_level()
		posx=p.get_x()
		posy=p.get_y()
		lives=p.get_lives()
		score=p.get_score()
		coins=p.get_coins()
		if posx == 1:
			b=Board(level+1)
			if level < 3:
				main(level+1,lives,score,coins)
			else:
				choice = 'q'
			continue	 
		if br_st == 1:
			br_st = 0
			prev = ' '
			flag = 1
		elif m3.l[posx-1][posy] == 'H' or(m3.l[posx][posy-1] == 'X' and m3.l[posx][posy+1] == 'X') or (m3.l[posx][posy-1] == 'H' and m3.l[posx][posy+1] == 'X') or (m3.l[posx][posy-1] == 'X' and m3.l[posx][posy+1] == 'H') or (m3.l[posx][posy-1] == 'X' and m3.l[posx][posy+1] == ' ' and posy!=1) or (m3.l[posx][posy-1] == ' ' and m3.l[posx][posy+1] == 'X' and posy!=m2.board_width-2) or m3.l[posx-2][posy] == 'H':
			prev = 'H'
			if m3.l[posx+1][posy] == ' ':
				br_st=1
		else:
			prev = ' '

		os.system("stty cbreak -echo")
		choice=sys.stdin.read(1)
		os.system("stty -cbreak echo")	
		if choice == ' ':	
			os.system("stty cbreak -echo")
			choice1=sys.stdin.read(1)
			os.system("stty -cbreak echo")	 
		if choice == 'a':
			x=p.checkWall("left")
#			print "x = "+str(x)
			if x != 1:
				x1=p.checkCollision()
				if x1==2:
					print "GAME OVER"
					choice='q'
				elif x1==1:
					main(level+1,lives,score,coins)
				else:
					if m3.l[posx][posy-1] == 'C':
						p.collectCoin()
					if posx in [4,8,12,16,20,24,28]:
						if m3.l[posx+1][posy-1]!=' ':
							p.move_left('P',prev)
						else:
							l1=[]
							l1=list(m3.l[posx])
							l1[posy]=prev
							m3.l[posx]="".join(l1)
							l1=list(m3.l[posx+4])
							l1[posy-1]='P'
							m3.l[posx+4]="".join(l1)
							p=Player(lives,score,posx+4,posy-1,coins)
		elif choice == 'd' :
			x=p.checkWall("right")
			if x!=1:
				x1=p.checkCollision()
				if x1==2:
				  	print "GAME OVER"
					choice='q'
				elif x1==1:
					p=Player(lives,score,m2.board_height-2,1,coins)
				else:
					if m3.l[posx][posy+1] == 'C':
						p.collectCoin()
					if posx in [4,8,12,16,20,24,28]:
						if m3.l[posx+1][posy+1]!=' ':
							p.move_right('P',prev)
						else:
							l1=[]
							l1=list(m3.l[posx])
							l1[posy]=prev
							m3.l[posx]="".join(l1)
							l1=list(m3.l[posx+4])
							l1[posy+1]='P'
							m3.l[posx+4]="".join(l1)
							p=Player(lives,score,posx+4,posy+1,coins)
		elif choice == 'w':
			x1=p.checkCollision()
			if x1==2:
			   	print "GAME OVER"
				choice='q'
			elif x1==1:
				p=Player(lives,score,m2.board_height-2,1,coins)
			else:
				if m3.l[posx-1][posy] == 'C':
					p.collectCoin()
				if m3.l[posx-1][posy] == 'H' or (m3.l[posx][posy-1] == 'X' and m3.l[posx][posy+1] == 'X' and m3.l[posx+1][posy] == 'H') or (m3.l[posx][posy-1] == 'X' and m3.l[posx][posy+1] == ' ' and m3.l[posx+1][posy] == 'H') or (m3.l[posx][posy-1] == ' ' and m3.l[posx][posy+1] == 'X' and m3.l[posx+1][posy] == 'H') or (m3.l[posx][posy-1] == 'H' and m3.l[posx][posy+1] == 'X' and m3.l[posx+1][posy] == 'H') or (m3.l[posx][posy-1] == 'X' and m3.l[posx][posy+1] == 'H' and m3.l[posx+1][posy] == 'H'):
					p.move_up(prev)

		elif choice == 's':
			x1=p.checkCollision()
			if x1==2:
				print "GAME OVER"
				choice='q'
			elif x1==1:
				p=Player(lives,score,m2.board_height-2,1,coins)
			else:
				if m3.l[posx+1][posy] == 'H':
					p.move_down(prev,'P')
				elif posx<m2.board_height-2:
				 	if m3.l[posx+2][posy] == 'H':
				 		p.move_down(prev,'P')

		elif choice == ' ':
			x1=p.checkCollision()
			if x1==2:
				print "GAME OVER"
				choice='q'
			elif x1 == 1:
				p=Player(lives,score,m2.board_height-2,1,coins)
			else:
				if choice1 == 'd':
					if m3.l[posx][posy+1] != 'X' and m3.l[posx][posy+2] != 'X' and m3.l[posx][posy+3] != 'X' and m3.l[posx][posy+4] != 'X':
						p.jump("right",prev)
				elif choice1 == 'a':					
					if m3.l[posx][posy-1] != 'X' and m3.l[posx][posy-2] != 'X' and m3.l[posx][posy-3] != 'X' and m3.l[posx][posy-4] != 'X':
						p.jump("left",prev)
		
	r = 0

t0=Thread(target=f0)
t1=Thread(target=f1)
t2=Thread(target=f2)

t0.start()
t1.start()
t2.start()
