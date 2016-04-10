import random
board_width=80
board_height=30
def f():
	global board_width,board_height
	cage_min_width=7
	cage_max_width=15
	floor_min_width=50
	floor_max_width=70
	ladder_start=0
	broken_ladder_start=0
	broken_ladder_count=0
	cage_width=random.randint(cage_min_width,cage_max_width)
	cage_start=random.randint(1,board_width-1-cage_width)
	princess_pos=random.randint(cage_start+1,cage_start+cage_width-2)
	if cage_start+cage_width-1 < 50 :
		direction = "left"
	else:
		direction = "right"
	 
	l=[]
	for i in range(0,board_height):
		subl=[]
		if i == 0 or i == board_height-1:
			j=0
			while j<80:
				subl.append('X')
				j=j+1
		elif i == 1:
			j=0
			while j<80:
				if j == 0 or j == cage_start or j == cage_start+cage_width-1 or j == board_width-1:
					elem='X'
				elif j == princess_pos:
					elem='Q'
				else:
					elem=' '
				subl.append(elem)
				j=j+1
		elif i == 2:
			j=0
			ladder_start=random.randint(cage_start+1,cage_start+cage_width-2)
			while j<board_width:
				if j == 0 or j == board_width-1:
					elem='X'
				elif j >= cage_start and j<= cage_start+cage_width-1:
					elem='X'
				else:	
					elem=' '
				subl.append(elem)
				j=j+1
		elif (i-5)%4 == 0:
			floor_width=random.randint(floor_min_width,floor_max_width)
			if direction == "left":
				floor_start = 1
				direction = "right"
			else:
				floor_start = board_width-floor_width-1
				direction = "left"
			j=0
			while j<board_width:
				if j == 0 or j == board_width-1 or (j>=floor_start and j<=floor_start+floor_width+1):
					elem='X'
				else:
					elem=' '
				subl.append(elem)
				j=j+1
		else:
			j=0
			while j<board_width:
				if j == 0 or j == board_width-1:
					elem='X'
				else:
			 		elem=' '
				subl.append(elem)
				j=j+1

		subl="".join(subl)
		l.append(subl)

	i=0
	for j in l:
		j=list(j)
		if i == 2:
			ladder_start=random.randint(cage_start+1,cage_start+cage_width-2)	
			j[ladder_start]='H'
		elif (i-5)%4 == 0 and i!=board_height-1 and i!=1:
			x=0
			y=0
			if i+4 != board_height-1:
				for a in range(1,board_width-2):
					if l[i][a] == ' ' and l[i][a+1] == 'X' and a!=board_width-2:
						x = a+1
					elif l[i][a-1] == 'X' and l[i][a] == ' ' and a!=1:
						y = a-1
					elif l[i+4][a-1] == 'X' and l[i+4][a] == ' ' and a!=1:
						y = a-1 
					elif l[i+4][a] == ' ' and l[i+4][a+1] == 'X' and a!=board_width-2:
						x = a+1
			else:
		  		for a in range(1,board_width-2):
					if l[i][a] == ' ' and l[i][a+1] == 'X' and a!=board_width-2:
						x = a+1
						y = board_width-2
					elif l[i][a-1] == 'X' and l[i][a] == ' ' and a!=1:
						y = a-1
						x = 1
			ladder_start=random.randint(x,y)
			broken_ladder_start=ladder_start
			broken_ladder_count=1
			while ladder_start == broken_ladder_start:
				broken_ladder_start=random.randint(x,y)
			j[ladder_start]='H'
			j[broken_ladder_start]='H'
		elif i > 2 and i!=board_height-1:
			k=0
			if i>5:
				broken_ladder_count+=1
			while k<board_width:
				if k == ladder_start:
					j[ladder_start] = 'H'
				elif k == broken_ladder_start and broken_ladder_count != 3 and i>5:
					j[broken_ladder_start] = 'H'
				k=k+1
		j="".join(j)
		l[i]=j
		i=i+1
	return l		
