import pygame


# This class represents a single cell in the Sudoku board. There are 81 Cells in a Board.
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

    def draw(self, selected=False, same_row_or_col = False): #Draw the cell
        cell_size = 60 #The width/height of the cell
        x = self.col * cell_size
        y = self.row * cell_size

        if selected:    #If a cell is selected, it will have a dark blue background
            pygame.draw.rect(self.screen, (143,234,221), (x, y, cell_size, cell_size), 0)
        elif same_row_or_col:    #If a cell is in the same row or column as the selected cell, it will have a light blue background.
            pygame.draw.rect(self.screen, (200,255,253), (x, y, cell_size, cell_size), 0)
        else:    #Otherwise, the cell will have a white background
            pygame.draw.rect(self.screen, (255, 255, 255), (x, y, cell_size, cell_size), 0)

        pygame.draw.rect(self.screen, (0, 0, 0), (x, y, cell_size, cell_size), 1) #Draw the cell with a black border

        #These are the fonts for text inside the cells
        big_font = pygame.font.SysFont("DIN", 32)
        little_font = pygame.font.SysFont("DIN", 16)

        if self.value != 0:  #Display the cell's value if it is available
            value_display = big_font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(value_display, (x + 22, y + 22))  #The value is aligned with the middle of the cell
        elif self.sketched_value != 0:  #Display the cell's sketched value if it is available
            sketched_value_display = little_font.render(str(self.sketched_value), True, (128, 128, 128))
            self.screen.blit(sketched_value_display, (x + 5, y + 5))  #The sketched value is aligned with the top left of the cell
