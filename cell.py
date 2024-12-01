import pygame

#This class represents a single cell in the Sudoku board. There are 81 Cells in a Board.
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self, selected=False):
        cell_size = 20 
        x = self.col * cell_size
        y = self.row * cell_size

        if selected: #Thick red Border if selected
            pygame.draw.rect(self.screen, (255,0,0), (x,y,cell_size, cell_size), 3)
        else: #Thin black border if not selected
            pygame.draw.rect(self.screen, (0, 0, 0), (x, y, cell_size, cell_size), 1)
        font = pygame.font.SysFont("arial", 32)
        if self.value != 0: #Display value if available
            value_text = font.render(str(self.value), True, (0,0,0))
            self.screen.blit(value_text, x+10, y+10) #Middle of cell
        elif self.sketched_value != 0: #Display sketched value if available
            sketched_value_text = font.render(str(self.sketched_value), True, (0,0,0))
            self.screen.blit(sketched_value_text, x, y) #Top left of cell



