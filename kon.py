#!/usr/bin/env python
import sys, random
import wx

class MainWindow(wx.Frame):
	def __init__(self, caption):
		wx.Frame.__init__(self,
			parent=None,
			title=caption,
			size=(300, 300),
			style=wx.MINIMIZE_BOX | wx.CAPTION | wx.SYSTEM_MENU | wx.CLOSE_BOX)
		self.Centre()
		self.Show(True)

app = wx.App()
MainWindow('kon')
app.MainLoop()

desired_id = 0
free_fields = []
starting_position = [' ']*8

def show_usage():
	print "Usage: " + sys.argv[0] + " [game id]"
	print "\twhere id needs to have a value between 0 and 959;"
	print "\tif id is omitted, a random game will be choosen"
	sys.exit(1)

def update_free_fields():
	global free_fields
	free_fields = [] # get an array of indices of free fields
	for i in range(0,8):
		if (starting_position[i] == ' '):
			free_fields.append(i)

if len(sys.argv) > 2: # too many arguments?
	show_usage()
elif len(sys.argv) == 2: # id has been supplied by user?
	try:
		desired_id = int(sys.argv[1]);
		if (desired_id < 0) or (desired_id > 959): # check range
			show_usage();
	except ValueError:
		show_usage()
else: # no id supplied, generate number by random
	random.seed()
	desired_id = random.randint(0, 959)

# okay, we have our desired id now, start calculating ;-)
print "Game #" + str(desired_id)

# R - Rook
# N - Knight
# B - Bishop
# Q - Queen
# K - King
# P - Pawn (not that important)

#==================== place first bishop (on bright square) ====================
#print "desired_id:", desired_id
bishop1_pos = desired_id % 4
desired_id /= 4
starting_position[1 + 2*bishop1_pos] = 'B'
#print "desired_id:", desired_id, "remainder:", bishop1_pos
#print starting_position

#==================== place second bishop (on dark square) =====================
bishop2_pos = desired_id % 4
desired_id /= 4
starting_position[0 + 2*bishop2_pos] = 'B'
#print "desired_id:", desired_id, "remainder:", bishop2_pos
#print starting_position

#================================ place queen ==================================
update_free_fields()
queen_pos = desired_id % 6
desired_id /= 6
starting_position[free_fields[queen_pos]] = 'Q'

#print "desired_id:", desired_id, "remainder:", queen_pos
#print starting_position

#================================ place knights ================================
update_free_fields()
knight_pos = desired_id
if (knight_pos == 0):
	starting_position[free_fields[0]] = 'N';
	starting_position[free_fields[1]] = 'N';
elif (knight_pos == 1):
	starting_position[free_fields[0]] = 'N';
	starting_position[free_fields[2]] = 'N';
elif (knight_pos == 2):
	starting_position[free_fields[0]] = 'N';
	starting_position[free_fields[3]] = 'N';
elif (knight_pos == 3):
	starting_position[free_fields[0]] = 'N';
	starting_position[free_fields[4]] = 'N';
elif (knight_pos == 4):
	starting_position[free_fields[1]] = 'N';
	starting_position[free_fields[2]] = 'N';
elif (knight_pos == 5):
	starting_position[free_fields[1]] = 'N';
	starting_position[free_fields[3]] = 'N';
elif (knight_pos == 6):
	starting_position[free_fields[1]] = 'N';
	starting_position[free_fields[4]] = 'N';
elif (knight_pos == 7):
	starting_position[free_fields[2]] = 'N';
	starting_position[free_fields[3]] = 'N';
elif (knight_pos == 8):
	starting_position[free_fields[2]] = 'N';
	starting_position[free_fields[4]] = 'N';
elif (knight_pos == 9):
	starting_position[free_fields[3]] = 'N';
	starting_position[free_fields[4]] = 'N';

#============================= place rooks and king ============================
update_free_fields()
starting_position[free_fields[0]] = 'R'
starting_position[free_fields[1]] = 'K'
starting_position[free_fields[2]] = 'R'

#print free_fields
print starting_position
