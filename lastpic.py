

import os
import sys


try:
	argument1 = sys.argv[1] #looks to see if user used an argument after the lastpic command
except:
	argument1 = "1"


if argument1 == "1":
	headResult = os.popen("ls -t $HOME/Pictures | head -1") #if no argument is used, finds file name for last file
else:
	headResult = os.popen("ls -t $HOME/Pictures | head -" + n + " | tail -1") #if a number is given as an argument, finds the file as far back as the number given

headResultUsable = headResult.read()


step1 = "xdg-open $HOME/Pictures/'" + headResultUsable.rstrip() + "'"
step2 = headResultUsable.rstrip().split(" ")
step3 = "\ ".join(step2)
print("xdg-open $HOME/Pictures/" + step3)

os.system(step1 + " && sleep 0.7 && xdotool getwindowfocus windowsize 400 400 windowmove 1350 650 mousemove --sync 1397 683 && sleep 0.1 && xdotool click 3 click 3 && sleep 0.1 && xdotool mousemove --sync 1417 783 click 1")

	
