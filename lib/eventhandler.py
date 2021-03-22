# event handler for sf ubws
import time, json, os
import pygame

#initiate font
pygame.font.init()
fontsize = 16
terminalFont = pygame.font.SysFont('Ubuntu Monospace.ttf', fontsize)
BGCOLOR = (0,0,55)

with open(os.path.join(os.getcwd(),"data/appinfo.json"), "r") as jsonfile:
	appinfo = json.load(jsonfile)


def MainEventHandler(events):
	for event in events:
		ControlHandler(pygame.key.get_pressed())
		if event.type == pygame.QUIT:
			return False

def ControlHandler(event):
	pass
