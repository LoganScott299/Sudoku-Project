from cell import Cell
from sudoku_generator import SudokuGenerator
import pygame

#This class represents an entire Sudoku board. A Board object has 81 Cell objects
class Board:
    def __init__(self, width, height, screen, removed_cells):
        self.width = width
        self.height = height
        self.screen = screen
        self.removed_cells = removed_cells
        self.selected_cell = None

        self.sudoku_generator = SudokuGenerator(9, removed_cells)
        self.sudoku_generator.fill_values()
        self.completed_board = self.sudoku_generator.get_board() #Board before cells are removed
        self.sudoku_generator.remove_cells()
        player_board = self.sudoku_generator.get_board() #Board after cells are removed

        self.cells = [] #9x9 grid of cells.
        for row in range(9):
            row_cells = []
            for col in range(9):
                cell = Cell(player_board[row][col], row, col, screen) #Use player_board to make cells
                row_cells.append(cell)
            self.cells.append(row_cells)

    def draw(self): #Draw each of the cells in the 9x9 grid
        for row in range(9):
            for col in range(9):
                self.cells[row][col].draw()

        if self.selected_cell: #Don't run this if no cell is selected
            row, col = self.selected_cell.row, self.selected_cell.col
            for i in range(9):
                self.cells[i][col].draw(same_row_or_col=True) #Redraw cells in the same column as selected cell
            for j in range(9):
                self.cells[row][j].draw(same_row_or_col=True) #Redraw cells in the same row as selected cell
            self.selected_cell.draw(selected=True) #Redraw the selected cell

        for x in [3, 6]: #Only need box divider lines at the 3rd and 6th positions
            pygame.draw.line(self.screen, (0, 0, 0), (x * self.width // 9, 0), (x * self.width // 9, self.height), 5)  #Vertical lines
            pygame.draw.line(self.screen, (0, 0, 0), (0, x * self.height // 9), (self.width, x * self.height // 9), 5)  #Horizontal lines

    def select(self, row, col):
        self.selected_cords = row, col
        self.selected_cell = self.cells[row][col]

    def click(self, x, y):
        row = y // (self.height // 9)
        col = x // (self.width // 9)

        if row >= 0 and row < 9: #Check if the click is in the board's boundaries
            if col >= 0 and col < 9:
                return row, col #Return the row and col of the click
        return None #Return None if the click is outside the board

    def clear(self): #Reset the cell to 0
        if self.selected_cell.original_value == 0:
            self.selected_cell.set_cell_value(0)
            self.selected_cell.set_sketched_value(0)

    def sketch(self, value): #Set sketch value
        if self.selected_cell.original_value == 0:
            self.selected_cell.set_sketched_value(value)

    def place_number(self): #Set actual value
        sketched_value = self.selected_cell.sketched_value
        if self.selected_cell.original_value == 0:
            self.selected_cell.set_cell_value(sketched_value)

    def reset_to_original(self): #Reset board to original state
        for row in self.cells:
            for cell in row:
                cell.value = cell.original_value
                cell.sketched_value = 0

    def is_full(self): #Check if the board is completed
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
                player_value = self.cells[row][col].value
                if player_value != 0:
                    if player_value != self.completed_board[row][col]: #Check player_board against completed_board
                        return False
        return True