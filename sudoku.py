import pygame
from board import Board

pygame.init()

button_color = (107, 2, 56)

sudoku_background = pygame.image.load('sudoku.jpg')

def draw_title(screen, x, y, text, title_color, outline_color):
    button_font = pygame.font.SysFont("comicsans", 64)
    button_text = button_font.render(text, True, title_color)
    button_outline_font = pygame.font.SysFont("comicsans", 65)
    button_outline_text = button_outline_font.render(text, True, outline_color)
    screen.blit(button_outline_text, (x + (200 - button_outline_text.get_width()) // 2, y + (50 - button_outline_text.get_height()) // 2))
    screen.blit(button_text, (x + (200 - button_text.get_width()) // 2, y + (50 - button_text.get_height()) // 2))

def draw_button(screen, x, y, text, color):
    button_font = pygame.font.SysFont("arial", 32)
    button_text = button_font.render(text, True, (255,255,255))
    pygame.draw.rect(screen, color, (x,y,200,50),border_radius = 15)
    screen.blit(button_text, (x + (200 - button_text.get_width()) // 2, y + (50 - button_text.get_height()) // 2))

def draw_small_button(screen, x, y, text, color):
    button_font = pygame.font.SysFont("arial", 22)
    button_text = button_font.render(text, True, (255,255,255))
    pygame.draw.rect(screen, color, (x,y,80,40), border_radius = 15)
    screen.blit(button_text, (x + 10, y + 6))

def main():
    try:
        screen = pygame.display.set_mode((540, 600)) #540x600 Screen
        pygame.display.set_caption("Sudoku")
        clock = pygame.time.Clock()
        running = True

        removed_cells = None
        board = None
        selected = None

        #Game loop for menu
        while running and not board:
            screen.blit(sudoku_background, (0,0)) #Sudoku background
            
            #Title
            draw_title(screen, 170, 70, "Play Sudoku", button_color, (0,0,0))
            
            #Easy, Medium, Hard Buttons
            draw_button(screen, 170, 170, "Easy", button_color)
            draw_button(screen, 170, 270, "Medium", button_color)
            draw_button(screen, 170, 370, "Hard", button_color)

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
                    if 550 <= y <= 590:
                        if 50 <= x <= 130:
                            board.reset_to_original()
                        elif 230 <= x <= 310:
                            main()
                        elif 410 <= x <= 490:
                            exit()
                    else:
                        selected = board.click(x,y)
                        if selected:
                            board.select(*selected)

                if event.type == pygame.KEYDOWN and selected:
                    if event.key == pygame.K_UP:
                        grid_list = list(selected)
                        if grid_list[0] != 0:
                            selected = (grid_list[0] - 1, grid_list[1])
                        if selected:
                            board.select(*selected)
                    if event.key == pygame.K_DOWN:
                        grid_list = list(selected)
                        if grid_list[0] != 8:
                            selected = (grid_list[0] + 1, grid_list[1])
                        if selected:
                            board.select(*selected)
                    if event.key == pygame.K_RIGHT:
                        grid_list = list(selected)
                        if grid_list[1] != 8:
                            selected = (grid_list[0], grid_list[1] + 1)
                        if selected:
                            board.select(*selected)
                    if event.key == pygame.K_LEFT:
                        grid_list = list(selected)
                        if grid_list[1] != 0:
                            selected = (grid_list[0], grid_list[1] - 1)
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
                if board.is_full():
                    if board.check_board():
                        while running:
                            screen.blit(sudoku_background, (0,0)) #Sudoku background
                            draw_button(screen, 170, 150, "Game Won!", button_color)
                            draw_small_button(screen, 230, 300, "   Exit", button_color)
                            pygame.display.flip()
                            for event in pygame.event.get():  # Event listener
                                if event.type == pygame.QUIT:  # Quit button
                                    running = False
                                if event.type == pygame.MOUSEBUTTONDOWN:  # Select cell
                                    x, y = event.pos
                                    if 300 <= y <= 340:
                                        if 230 <= x <= 310:
                                            exit()
                    if not board.check_board():
                        while running:
                            screen.fill((255, 255, 255))
                            draw_button(screen, 170, 150, "Game Over :(", button_color)
                            draw_small_button(screen, 230, 300, "Restart", button_color)
                            pygame.display.flip()
                            for event in pygame.event.get():  # Event listener
                                if event.type == pygame.QUIT:  # Quit button
                                    running = False
                                if event.type == pygame.MOUSEBUTTONDOWN:  # Select cell
                                    x, y = event.pos
                                    if 300 <= y <= 340:
                                        if 230 <= x <= 310:
                                            main()

            board.draw()
            #Reset, Restart, Exit Buttons
            draw_small_button(screen, 50, 550, " Reset", button_color)
            draw_small_button(screen, 230, 550, "Restart", button_color)
            draw_small_button(screen, 410, 550, "   Exit", button_color)

            pygame.display.flip()
            clock.tick(25)

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
