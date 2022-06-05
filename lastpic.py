

import os
import sys


try:
	n = sys.argv[1]
except:
	n = "1"
try:
	m = sys.argv[2]
except:
	m = False

if m == "e" or m == "email":
	print("email")

if n == "1":
	a = os.popen("ls -t $HOME/Pictures | head -1")
else:
	a = os.popen("ls -t $HOME/Pictures | head -" + n + " | tail -1")

l = a.read()
#.split(".png")

#g = "xdg-open /home/james/Pictures/'" + l[0] + ".png'"
g = "xdg-open $HOME/Pictures/'" + l.rstrip() + "'"
qq = l.rstrip().split(" ")
qqq = "\ ".join(qq)
print("xdg-open $HOME/Pictures/" + qqq)

os.system(g + " && sleep 0.7 && xdotool getwindowfocus windowsize 400 400 windowmove 1350 650 mousemove --sync 1397 683 && sleep 0.1 && xdotool click 3 click 3 && sleep 0.1 && xdotool mousemove --sync 1417 783 click 1")

# ~ emailer()
	
