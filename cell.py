import pygame

#This class represents a single cell in the Sudoku board. There are 81 Cells in a Board.
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.original_value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self, selected=False):
        cell_size = 60
        x = self.col * cell_size
        y = self.row * cell_size

        if selected: #Thick red Border if selected
            pygame.draw.rect(self.screen, (255,0,0), (x,y,cell_size, cell_size), 3)
        else: #Thin black border if not selected
            pygame.draw.rect(self.screen, (0, 0, 0), (x, y, cell_size, cell_size), 1)
            
        big_font = pygame.font.SysFont("arial", 32)
        little_font = pygame.font.SysFont("arial", 16)
        
        if self.value != 0: #Display value if available
            value_display = big_font.render(str(self.value), True, (0,0,0))
            self.screen.blit(value_display, (x+20, y+15)) #Middle of cell
        elif self.sketched_value != 0: #Display sketched value if available
            sketched_value_display = little_font.render(str(self.sketched_value), True, (128,128,128))
            self.screen.blit(sketched_value_display, (x+5, y+5)) #Top left of cell
