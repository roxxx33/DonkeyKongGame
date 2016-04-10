import c1
import m2
import m3

p = c1.Player(2,5,24,45,20)
d = c1.Donkey(4,40)

layout = m3.l

class Test_Player:

	def test_move_left(self):
		pos_x = c1.Player.get_x(p)
		pos_y = c1.Player.get_y(p)
		if layout[pos_x + 1][pos_y - 1] == 'X' or layout[pos_x + 1][pos_y - 1] == 'H':
	       		if layout[pos_x][pos_y - 1] == ' ' or layout[pos_x][pos_y - 1] == 'H' or layout[pos_x][pos_y -1] == 'C':
				prev = layout[pos_x][pos_y]
				prev = c1.Player.move_left(p,'P',prev)
				new_pos_x = c1.Player.get_x(p)
				new_pos_y = c1.Player.get_y(p)
 				assert new_pos_x == pos_x
				assert new_pos_y == pos_y - 1
			else:
				assert new_pos_x == pos_x
				assert new_pos_y == pos_y
		else:

			prev = layout[pos_x][pos_y]
			prev = c1.Player.move_left(p,'P',prev)
			new_pos_x = c1.Player.get_x(p)
			new_pos_y = c1.Player.get_y(p)
			assert new_pos_x == pos_x + 4
			assert new_pos_y == pos_y - 1

	def test_move_right(self):
		pos_x = c1.Player.get_x(p)
		pos_y = c1.Player.get_y(p)
		if layout[pos_x + 1][pos_y + 1] == 'X' or layout[pos_x + 1][pos_y + 1] == 'H':
	       		if layout[pos_x][pos_y + 1] == ' ' or layout[pos_x][pos_y + 1] == 'H' or layout[pos_x][pos_y + 1] == 'C':
				prev = layout[pos_x][pos_y]
				prev = c1.Player.move_right(p,'P',prev)
				new_pos_x = c1.Player.get_x(p)
				new_pos_y = c1.Player.get_y(p)
				assert new_pos_x == pos_x
				assert new_pos_y == pos_y + 1
			else:
				assert new_pos_x == pos_x
				assert new_pos_y == pos_y
		else:

			prev = layout[pos_x][pos_y]
			prev = c1.Player.move_right(p,'P',prev)
			new_pos_x = c1.Player.get_x(p)
			new_pos_y = c1.Player.get_y(p)
			assert new_pos_x == pos_x + 4
			assert new_pos_y == pos_y + 1

	def test_move_up(self):
		pos_x = c1.Player.get_x(p)
		pos_y = c1.Player.get_y(p)
		if layout[pos_x + 1][pos_y] == 'H' or (layout[pos_x + 1][pos_y] == ' ' and ( layout[pos_x][pos_y - 1] == 'H' or layout[pos_x][pos_y - 1] == 'X' or layout[pos_x][pos_y + 1] == 'H' or layout[pos_x][pos_y + 1] == 'X' )):

				prev = layout[pos_x][pos_y]
				prev = c1.Player.move_up(p,prev)
				new_pos_x = c1.Player.get_x(p)
				new_pos_y = c1.Player.get_y(p)
				assert new_pos_x == pos_x - 1
				assert new_pos_y == pos_y
		else:
			assert new_pos_x == pos_x
			assert new_pos_y == pos_y


	def test_move_down(self):
		pos_x = c1.Player.get_x(p)
		pos_y = c1.Player.get_y(p)
		if layout[pos_x + 1][pos_y] == 'H' or (layout[pos_x + 1][pos_y] == ' ' and layout[pos_x + 2][pos_y] == 'H'):
				prev = layout[pos_x][pos_y]
				prev = c1.Player.move_down(p,'P',prev)
				new_pos_x = c1.Player.get_x(p)
				new_pos_y = c1.Player.get_y(p)
				assert new_pos_x == pos_x + 1
				assert new_pos_y == pos_y
		else:
			assert new_pos_x == pos_x
			assert new_pos_y == pos_y

	def test_jump(self,direction):
		pos_x = c1.Player.get_x(p)
		pos_y = c1.Player.get_y(p)
		if direction == "left":
			if pos_y - 4 <= 0:
				assert new_pos_x == pos_x
				assert new_pos_y == pos_y
			elif layout[pos_x+1][pos_y - 4] == ' ':
				prev = layout[pos_x][pos_y]
				c1.Player.jump(p,direction,prev)
				new_pos_x = c1.Player.get_x(p)
				new_pos_y = c1.player.get_y(p)
				assert new_pos_x == pos_x + 4
				assert new_pos_y == pos_y - 4
			else:
				prev = layout[pos_x][pos_y]
				c1.Player.jump(p,direction,prev)
				new_pos_x = c1.Player.get_x(p)
				new_pos_y = c1.player.get_y(p)
				assert new_pos_x == pos_x
				assert new_pos_y == pos_y - 4

		else:
			if pos_y + 4 >= 79:
				assert new_pos_x == pos_x
				assert new_pos_y == pos_y
			elif layout[pos_x+1][pos_y + 4] == ' ':
				prev = layout[pos_x][pos_y]
				c1.Player.jump(p,direction,prev)
				new_pos_x = c1.Player.get_x(p)
				new_pos_y = c1.player.get_y(p)
				assert new_pos_x == pos_x + 4
				assert new_pos_y == pos_y + 4
			else:
				prev = layout[pos_x][pos_y]
				c1.Player.jump(p,direction,prev)
				new_pos_x = c1.Player.get_x(p)
				new_pos_y = c1.player.get_y(p)
				assert new_pos_x == pos_x
				assert new_pos_y == pos_y + 4

	def test_collectCoin(self):
		coins = Player.get_coins(p)
		score = Player.get_score(p)
		c1.Player.collectCoin(p)
		new_coins = Player.get_coins(p)
		new_score = Player.get_score(p)
		assert new_coins == coins + 1
		assert new_score == score + 5

	def test_checkWall(self,direction):
		pos_x = c1.Player.get_x(p)
		pos_y = c1.Player.get_y(p)
		x = c1.Player.checkWall(p)
		if direction == "left" and layout[pos_x][pos_y - 1] == 'X':
			assert x == 1
		elif direction == "right" and layout[pos_x][pos_y + 1] == 'X':
			assert x == 1
		else:
			assert x == 0

	def test_checkCollision(self):
		pos_x = c1.Player.get_x(p)
		pos_y = c1.Player.get_y(p)
		lives = c1.Player.get_lives(p)
		x = c1.Player.checkCollision(p)
		new_lives = c1.Player.get_lives(p)
		if lives > 0:
			if layout[pos_x][pos_y + 1] == 'O' or layout[pos_x][pos_y - 1] == 'O' or layout[pos_x - 1][pos_y] == 'O':
				assert x == 1
				assert new_lives == lives - 1
			else:
				assert x == 0
				assert new_lives == lives
		else:
			assert x == 2

class Test_Donkey:

	def test_move_left(self):
		pos_x = c1.Donkey.get_x(d)
		pos_y = c1.Donkey.get_y(d)
		if layout[pos_x + 1][pos_y - 1] == 'X' or layout[pos_x + 1][pos_y - 1] == 'H':
	       		if layout[pos_x][pos_y - 1] == ' ' or layout[pos_x][pos_y - 1] == 'H' or layout[pos_x][pos_y -1] == 'C':
				prev = layout[pos_x][pos_y]
				prev = c1.Donkey.move_left(d,'D',prev)
				new_pos_x = c1.Donkey.get_x(d)
				new_pos_y = c1.Donkey.get_y(d)
 				assert new_pos_x == pos_x
				assert new_pos_y == pos_y - 1
			else:
				assert new_pos_x == pos_x
				assert new_pos_y == pos_y

	def test_move_right(self):
		pos_x = c1.Donkey.get_x(p)
		pos_y = c1.Donkey.get_y(p)
		if layout[pos_x + 1][pos_y + 1] == 'X' or layout[pos_x + 1][pos_y + 1] == 'H':
	       		if layout[pos_x][pos_y + 1] == ' ' or layout[pos_x][pos_y + 1] == 'H' or layout[pos_x][pos_y + 1] == 'C':
				prev = layout[pos_x][pos_y]
				prev = c1.Donkey.move_right(d,'D',prev)
				new_pos_x = c1.Donkey.get_x(d)
				new_pos_y = c1.Donkey.get_y(d)
				assert new_pos_x == pos_x
				assert new_pos_y == pos_y + 1
			else:
				assert new_pos_x == pos_x
				assert new_pos_y == pos_y
		else:

			prev = layout[pos_x][pos_y]
			prev = c1.Player.move_right(d,'P',prev)
			new_pos_x = c1.Player.get_x(d)
			new_pos_y = c1.Player.get_y(d)
			assert new_pos_x == pos_x + 4
			assert new_pos_y == pos_y + 1

	def test_checkWall(self,di):
		pos_x = c1.Donkey.get_x(d)
		pos_y = c1.Donkey.get_y(d)
		x = c1.Donkey.checkWall(d,"")
		if layout[pos_x][pos_y - 1] == 'X' or layout[pos_x + 1][pos_y - 1] == ' ':
			assert x == "left"
		elif layout[pos_x][pos_y + 1] == 'X' or layout[pos_x][pos_y + 1] == ' ':
			assert x == "right"
		else:
			assert (x == "left" or x == "right")


if __name__ == "__main__":
#	for checking if no. of coins generated >= 20
	count = 0
	for i in [28,23,17,12,7]:
		for j in range(1,80):
			if layout[i][j] == 'C':
				count = count + 1
	assert count >= 20
	t = Test_Player()
	d = Test_Donkey()
	t.test_move_left()
	t.test_move_right()
	t.test_move_up()
	t.test_move_down()
	t.test_jump("left")
	t.test_jump("right")
	t.test_collectCoin()
	t.test_checkWall()
	t.test_checkCollision()
	d.test_move_left()
	d.test_move_right()
	d.test_checkWall(d,"")
