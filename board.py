from cell import Cell
from sudoku_generator import SudokuGenerator
import pygame

#This class represents an entire Sudoku board. A Board object has 81 Cell objects
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        if difficulty == "easy":
            removed_cells = 30
        elif difficulty == "medium":
            removed_cells = 40
        elif difficulty == "hard":
            removed_cells = 50

        self.sudoku_generator = SudokuGenerator(9, removed_cells)
        self.sudoku_generator.fill_values()
        self.sudoku_generator.remove_cells()
        board = self.sudoku_generator.get_board()

        self.cells = [] #9x9 grid of cells.
        for row in range(9):
            row_cells = []
            for col in range(9):
                cell = Cell(board[row][col], row, col, screen)
                row_cells.append(cell)
            self.cells.append(row_cells)

    def draw(self): #Draw each of the cells in the 9x9 grid
        for row in range(9):
            for col in range(9):
                self.cells[row][col].draw()

        for x in [3, 6]: #These lines divide boxes and are bolded. <- Might want to make thicker 
            pygame.draw.line(self.screen, (0, 0, 0), (x * self.width // 9, 0), (x * self.width // 9, self.height), 3) #Vertical lines
            pygame.draw.line(self.screen, (0, 0, 0), (0, x * self.height // 9), (self.width, x * self.height // 9), 3) #Horizontal lines

    def select(self, row, col): 
        self.selected_cell = self.cells[row][col]

    def click(self, x, y):
        row = y // (self.height // 9)
        col = x // (self.width // 9)

        if row >= 0 and row < 9: #Check if the click is in the board's boundaries
            if col >= 0 and col < 9:
                if self.cells[row][col].value == 0:
                    return row, col
        return None #Return None if the click is outside the board

    def clear(self):
        if self.selected_cell:
            self.selected_cell.set_cell_value(0)

    def sketch(self, value):
        if self.selected_cell:
            self.selected_cell.set_sketched_value(value)

    def place_number(self, value):
        if self.selected_cell:
            self.selected_cell.set_cell_value(value)

    def reset_to_original(self): #Reset board to original state
        for row in self.cells:
            for cell in row:
                cell.value = cell.original_value

    def is_full(self): #Check if board completed
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True

    def update_board(self): #Finalize sketches
        for row in self.cells:
            for cell in row:
                cell.set_cell_value(cell.sketched_value)

    def check_board(self):
        for row in range(9):
            for col in range (9):
                value = self.cells[row][col].value
                if value != 0:
                    if not self.sudoku_generator.is_valid(row, col, value):
                        return False
        return True

