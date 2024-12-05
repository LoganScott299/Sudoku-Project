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

        removed_cells = None
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
                    if 170 <= clickX <= 370:
                        if 150 <= clickY <= 200:
                            removed_cells = 30 #Easy
                        elif 250 <= clickY <= 300:
                            removed_cells = 40 #Medium
                        elif 350 <= clickY <= 400:
                            removed_cells = 50 #Hard

                        if removed_cells:
                            board = Board(540, 540, screen, removed_cells)
                            running = False
            pygame.display.flip()
            clock.tick(60)

        running = True
        #Game loop for Sudoku
        while running and board:
            screen.fill((255,255,255)) #White background

            for event in pygame.event.get(): #Event listener
                if event.type == pygame.QUIT: #Quit button
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN: #Select cell
                    x, y = event.pos
                    selected = board.click(x,y)
                    if selected:
                        board.select(*selected)

                if event.type == pygame.KEYDOWN and selected: #Input value
                    if event.key == pygame.K_1:
                        board.sketch(1)
                    elif event.key == pygame.K_2:
                        board.sketch(2)
                    elif event.key == pygame.K_3:
                        board.sketch(3)
                    elif event.key == pygame.K_4:
                        board.sketch(4)
                    elif event.key == pygame.K_5:
                        board.sketch(5)
                    elif event.key == pygame.K_6:
                        board.sketch(6)
                    elif event.key == pygame.K_7:
                        board.sketch(7)
                    elif event.key == pygame.K_8:
                        board.sketch(8)
                    elif event.key == pygame.K_9:
                        board.sketch(9)
                    elif event.key == pygame.K_BACKSPACE:  #Clear the cell
                        board.clear()
                    elif event.key == pygame.K_RETURN: #Submit guess
                        board.place_number()

            board.draw()

            if selected:
                row,col = selected
                board.cells[row][col].draw(selected=True)
            
            pygame.display.flip()
            clock.tick(25)

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
