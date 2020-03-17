import sys
import pygame
import numpy as np
import random as rd
import time

def genGrid(x = 20, y = 20):
    Grid = np.zeros((x,y))
    for i in range(x):
        for j in range(y):
            Grid[i][j] = int(rd.randint(0,1))
    return Grid


def LiveNeighbours(matrix, x, y):
    Neighbours = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            Neighbours += matrix[x + i][y + j]
            #print(matrix[x + i][y + j], end=" ")
            
    Neighbours -= matrix[x][y]
    return Neighbours

def gensEngine(matrix, x = 19, y = 19):
    print(matrix)
    for x in range(1, x):
        for y in range(1, y):
            state = matrix[x][y]
            LiveNB = LiveNeighbours(matrix, x, y)
            if state == 0 and LiveNB == 3:
                matrix[x][y] = 1
            elif state == 1 and (LiveNB < 2 or LiveNB > 3):
                matrix[x][y] = 0
            else:
                matrix[x][y] = state
    return matrix

generations = gensEngine(genGrid(20,20))

# PyGame
pygame.init()
screen = pygame.display.set_mode((500, 500), 0, 32)

#Colour
gray  = [20, 20, 20]
white = [255, 255, 255]
black = [0, 0, 0]

#Display
pygame.display.set_caption("Game Of Life")
screen.fill(gray)
pygame.display.flip()


exit = False
while not exit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	i = 0
	j = 0
	pygame.display.update()
	generations = gensEngine(generations)
	for y in range(0, 500, 25):
		for x in range(0, 500, 25):
			if generations[i][j] == 1.0:
				pygame.draw.rect(screen, white, [x, y, 25, 25])
			else:
				pygame.draw.rect(screen, black, [x, y, 25, 25])
			time.sleep(0.000)
			j += 1
		i += 1
		j = 0

			
