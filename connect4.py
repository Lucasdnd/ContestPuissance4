import numpy as np
import pygame
import sys
import math
import tkinter as tk

#Demande le nom des joueurs :

def quitPopup():
	master.quit()
	
def launchGame(master):
	master.destroy()
	main_game()

def returnMenu(master):
    master.destroy()

name1 = ''
name2 = ''

master = tk.Tk()
master.geometry("+700+300")
tk.Label(master,
         text="Nom du joueur 1").grid(row=0)
tk.Label(master, 
         text="Non du joueur 2").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master, 
          text='Jouer', 
          command=quitPopup).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)

tk.mainloop()

name1 = e1.get()
name2 = e2.get()
master.destroy()

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
	board = np.zeros((ROW_COUNT,COLUMN_COUNT))
	return board

def drop_piece(board, row, col, piece):
	board[row][col] = piece

def is_draw(board):
	for i in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			if board[r][i] == 0:
				return False
	return True

def is_valid_location(board, col):
	return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
	for r in range(ROW_COUNT):
		if board[r][col] == 0:
			return r

def print_board(board):
	print(np.flip(board, 0))

def winning_move(board, piece):
	# Check horizontal locations for win
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	# Check vertical locations for win
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	# Check positively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	# Check negatively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(3, ROW_COUNT):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True

def draw_board(board):
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):		
			if board[r][c] == 1:
				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif board[r][c] == 2: 
				pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
	pygame.display.update()

board = create_board()
print_board(board)
game_over = False
turn = 0
score_player1 = 0
score_player2 = 0

pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

def main_game():
	board = create_board()
	print_board(board)
	game_over = False
	turn = 0

	pygame.init()

	SQUARESIZE = 100

	width = COLUMN_COUNT * SQUARESIZE
	height = (ROW_COUNT+1) * SQUARESIZE

	size = (width, height)

	RADIUS = int(SQUARESIZE/2 - 5)

	screen = pygame.display.set_mode(size)
	draw_board(board)
	pygame.display.update()

	myfont = pygame.font.SysFont("monospace", 75)

	while not game_over:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.MOUSEMOTION:
				pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
				posx = event.pos[0]
				if turn == 0:
					pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
				else: 
					pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
			pygame.display.update()

			if event.type == pygame.MOUSEBUTTONDOWN:
				pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
				#print(event.pos)
				# Ask for Player 1 Input
				if turn == 0:
					posx = event.pos[0]
					col = int(math.floor(posx/SQUARESIZE))

					if is_valid_location(board, col):
						row = get_next_open_row(board, col)
						drop_piece(board, row, col, 1)

						if winning_move(board, 1):
							global score_player1
							global name1
							score_player1 += 1
							label = myfont.render(name1 + " a gagné !", 1, RED)
							screen.blit(label, (40,10))
							game_over = True


				# # Ask for Player 2 Input
				else:				
					posx = event.pos[0]
					col = int(math.floor(posx/SQUARESIZE))

					if is_valid_location(board, col):
						row = get_next_open_row(board, col)
						drop_piece(board, row, col, 2)

						if winning_move(board, 2):
							global score_player2
							global name2
							score_player2 += 1
							label = myfont.render(name2 + " a gagné !", 1, YELLOW)
							screen.blit(label, (40,10))
							game_over = True

				# Verifie si il y a une égalité
				if is_draw(board):
					label = myfont.render("égalité!!", 1, RED)
					screen.blit(label, (40,10))
					game_over = True

				print_board(board)
				draw_board(board)

				turn += 1
				turn = turn % 2

				if game_over:
					print(score_player1)
					print(score_player2)
	
	# popup fin de partie
	master = tk.Tk()
	master.geometry("+700+300")
	# Création de nos widgets
	message = tk.Label(master, text="Score " + name1 + " : " + str(score_player1))
	message.pack()
	message = tk.Label(master, text="Score " + name2 + " : " + str(score_player2))
	message.pack()

	bouton_quitter = tk.Button(master, text="Nouvelle partie", command=lambda: launchGame(master))
	bouton_quitter.pack()
	bouton_quitter = tk.Button(master, text="Retourner au menu", command=lambda: returnMenu(master))
	bouton_quitter.pack()

	tk.mainloop()


main_game()

