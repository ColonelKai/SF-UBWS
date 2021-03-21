import pygame
import sys, os, json

import lib.textdisplay
import lib.eventhandler

WIDTH, HEIGHT =  1200, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("UB;UBWS")

# Hardcoded FPS.
FPS = 60

#region various bullshittery
#COLORS
BGCOLOR = (0,0,55)

#IMAGES
SLOGO = pygame.image.load(os.path.join("data", "photos", "SERAPHIMLOGO.png"))
SLOGOTRANS = pygame.image.load(os.path.join("data", "photos", "SERAPHIMLOGO_TRANSPARENT.png"))
pygame.display.set_icon(SLOGOTRANS)
#endregion

# code to update appinfo.json if needed due to balls balls help me pls aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
with open(os.path.join(os.getcwd(),"data/appinfo.json"), "r") as jsonfile:
	appinfo = json.load(jsonfile)
	appinfo["parentdir"] = str(os.path.abspath(os.getcwd()))
	appinfo["hardcodedFPS"] = FPS

with open(os.path.join(os.getcwd(), "data/appinfo.json"), "w") as jsonfile:
	json.dump(appinfo, jsonfile)

# Main game loop
def main():
	clock = pygame.time.Clock()
	doGameLoop = True

	# loop
	while(doGameLoop):
		# FPS cap
		clock.tick(FPS)

		# check for events here
		for event in pygame.event.get():
			# get the pressed keys for future reference:
			keys = pygame.key.get_pressed()
			lib.eventhandler.KeyControlHander(keys, WIN)
			# user quit window
			if event.type == pygame.QUIT:
				doGameLoop = False
		

		WIN.fill(BGCOLOR)

		# lib.textdisplay.StartupSequence(WIN, (5,5), 5)
		# Update Screen
		pygame.display.update()
	# quit game after loop ends
	pygame.quit()


if __name__ == "__main__":
	main()