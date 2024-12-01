import pygame
from board import Board

pygame.init()

button_color = (107, 2, 56)

def draw_button(screen, x, y, text, color):
    button_font = pygame.font.SysFont("arial", 32)
    button_text = button_font.render(text, True, (255,255,255))
    pygame.draw.rect(screen, color, (x,y,200,50))
    screen.blit(button_text, (x + (200 - button_text.get_width()) // 2, y + (50 - button_text.get_height()) // 2))

def main():
    try:
        screen = pygame.display.set_mode((540, 540)) #540x540 Screen
        pygame.display.set_caption("Sudoku")
        clock = pygame.time.Clock()
        running = True

        difficulty = None
        board = None
        selected = None

        #Game loop for menu
        while running and not board:
            screen.fill((255, 255, 255))  #White background
            #Easy, Medium, Hard Buttons
            draw_button(screen, 170, 150, "Easy", button_color)
            draw_button(screen, 170, 250, "Medium", button_color)
            draw_button(screen, 170, 350, "Hard", button_color)

            for event in pygame.event.get(): #Event listener
                if event.type == pygame.QUIT: #Quit button
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickX, clickY = event.pos
                    if 270 <= clickX <= 470:
                        if 150 <= clickY <= 200:
                            difficulty = "easy"
                        elif 250 <= clickY <= 300:
                            difficulty = "medium"
                        elif 350 <= clickY <= 400:
                            difficulty = "hard"

                        if difficulty:
                            board = Board(540, 540, screen, difficulty)
                            running = False

        pygame.display.flip()
        clock.tick(60)

        #Game loop for Sudoku
        while running and board:
            screen.fill((255,255,255)) #White background

            for event in pygame.event.get(): #Event listener
                if event.type == pygame.QUIT: #Quit button
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN: #Select cell
                    x, y = event.pos
                    row, col = board.click(x,y)
                    if row and col:
                        board.select(row, col)

                if event.type == pygame.KEYDOWN and selected: #Input value
                    if event.key == pygame.K_1:
                        board.place_number(1)
                    elif event.key == pygame.K_2:
                        board.place_number(2)
                    elif event.key == pygame.K_3:
                        board.place_number(3)
                    elif event.key == pygame.K_4:
                        board.place_number(4)
                    elif event.key == pygame.K_5:
                        board.place_number(5)
                    elif event.key == pygame.K_6:
                        board.place_number(6)
                    elif event.key == pygame.K_7:
                        board.place_number(7)
                    elif event.key == pygame.K_8:
                        board.place_number(8)
                    elif event.key == pygame.K_9:
                        board.place_number(9)
                    elif event.key == pygame.K_BACKSPACE:  # Clear the cell
                        board.clear()

            board.draw()

            if row and col:
                board.cells[row][col].draw(selected=True)

            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
