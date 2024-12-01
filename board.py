from cell import Cell

#This class represents an entire Sudoku board. A Board object has 81 Cell objects
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        self.cells = [] #9x9 grid of cells.
        for row in range(9):
            row_cells = []
            for col in range(9):
                cell = Cell(0, row, col, screen)
                row_cells.append(cell)
            self.cells.append(row_cells)

    def draw(self): #Draw each of the cells in the 9x9 grid
        for row in range(9):
            for col in range(9):
                self.cells[row][col].draw()

        for x in [3,6,9]: #Draw thick lines to separate the 3x3 boxes
            pygame.draw.line(self.screen, (0,0,0), (x * self.width // 9, 0), (x * self.width // 9, self.height), 3)
            pygame.draw.line(self.screen, (0, 0, 0), (x * self.height // 9, 0), (self.height, x * self.width // 9), 3)

    def select(self, row, col): #
        self.selected_cell = self.cells[row][col]

    def click(self, x, y):
        row = y // (self.height // 9)
        col = x // (self.width // 9)

        if row >= 0 and row < 9: #Check if the click is in the board's boundaries
            if col >= 0 and col < 9:
                return row, col
        return None #Return None if the click is outside the board
