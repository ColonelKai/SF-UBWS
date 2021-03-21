# Text display code for SF;UBWS.
import time, json, os
import pygame

#initiate font
pygame.font.init()
fontsize = 16
terminalFont = pygame.font.SysFont('Ubuntu Monospace.ttf', fontsize)
BGCOLOR = (0,0,55)

with open(os.path.join(os.getcwd(),"data/appinfo.json"), "r") as jsonfile:
	appinfo = json.load(jsonfile)

# A function that writes shit on the screen bound between 2 coordinates from a dict, timed. mostly used in loading screens.
# Working principle:
# This will go through all the keys in a dict and will look for keys under that key, and will replace the text with each sub-key each 0.5 second apart.
# If you want more than a 0.5 second. If you dont want the text to change just put 1 and no more.
# Example JSON file:
# {
#	"1":{
#	"a":"Yay this displays",
#	"b":"It displays this now, 0.5 seconds afterwards!"
# }}
# pause, just copy paste the same text and it should work.
# PLEASE FOR THE LOVE OF GOD USE JSON TO DO THESE, ITLL BE SO MUCH MORE CLEAN AAAAAAA - past kai
def SequencedTextDisplay(TextDict, window, startloc, linelimit):
	# get all the major keys for each line
	mainkeys = list(TextDict.keys())
	# current line that we are on.
	currentLine = 1
	# the dict that will contain all of the lines - ready to be displayed.
	textsInLines = {}
	lastText = ""
	# This is the per-line loop, it iterates through every lines text
	for i in mainkeys:
		# get all the states of this particular line
		subkeys = list(TextDict[i].keys())
		# This is for every state of a line.
		for ii in subkeys:
			# calculate y coordinate of the text depending on which line it is and the font size.
			yloc = startloc[1] + (currentLine * fontsize) - 16
			# get the text to print
			currentText = TextDict[str(i)][str(ii)]
			# we will now erase the text from the previous loop.
			wipeText = terminalFont.render(lastText, True, (BGCOLOR))
			window.blit(wipeText, (yloc, startloc[1]))
			# if its at the limit of the lines we can use, we will have to shift it all, eliminating the one line at the top.
			if currentLine == linelimit:
				# shifting all of them one up, overriding the first element of it.
				for ind, elem, in enumerate(list(textsInLines.keys())):
					# if the index is 0, dont do anything as we cannot shift the 0th value to anywhere else.
					if ind != 0:
						# set the element previous to the current element to the the current element to shift all elements one back in the list. 0th element gets overriden by this
						# so that it accomodates for extra room for our new element to be placed on the screen. 
						textsInLines[ind-1] = elem
			else: # if there is still space in the text area, just continue writing.
				textsInLines[currentLine] = currentText
			# now, just write everything on the screen.
			# this is not efficient as it displays all the text on the screen every time, but its small enough to be ignored.
			for i in textsInLines:
				# create the text surface, think of it as a text sprite.
				textsurface = terminalFont.render(textsInLines[i], True, (255,255,255))
				# blit that shit onto the screen
				window.blit(textsurface, (yloc, startloc[1]))
			# save the text for overriding in the next loop to allow cleanup.
			lastText = currentText
			# the 0.5 second delay i promised!!!
			time.sleep(0.5)
		# increase the line by 1 to adjust the pixel.
		currentLine += 1




def StartupSequence(window, startloc, linelimit):
	time.sleep(2)
	with open(os.path.join(appinfo["parentdir"],"data/textdata/startup.json")) as file:
		TextDict = json.load(file)
	SequencedTextDisplay(TextDict, window, startloc, linelimit)