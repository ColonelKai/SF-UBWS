import pygame
import sys, os

WIDTH, HEIGHT =  900, 500
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
			# user quit window
			if event.type == pygame.QUIT:
				doGameLoop = False

		WIN.fill(BGCOLOR)
	
		# Update Screen
		pygame.display.update()
	
	pygame.quit()


if __name__ == "__main__":
	main()