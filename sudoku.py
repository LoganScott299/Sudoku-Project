import pygame
from board import Board

pygame.init()

button_color = "dark orange"

def draw_button(screen, x, y, text, color, border_color="dark orange", border_thickness = 5, gap_thickness = 5):
    button_font = pygame.font.SysFont("Comic Sans", 21)
    button_text = button_font.render(text, True, (255,255,255))
    pygame.draw.rect(screen, color, (x,y,100,40))
    pygame.draw.rect(screen, border_color, (x - gap_thickness - border_thickness, y - gap_thickness - border_thickness, 100 + 2 * (gap_thickness + border_thickness) , 40+2*(gap_thickness + border_thickness),
                                            ),
                     border_thickness
                     )
    pygame.draw.rect(screen, "black", (x - 5 - 1, y - 5 - 1, 100 + 2 * 5+2, 40 + 2 * 5+2,), 1)
    pygame.draw.rect(screen, "black", (x - 5 - 1 - 3, y - 5 - 1 - 3, 100 + 2 * 6 + 6, 40 + 2 * 6 + 6,), 1)
    screen.blit(button_text, (x + (105 - button_text.get_width()) // 2, y + (40 - button_text.get_height()) // 2))

def draw_small_button(screen, x, y, text, color, border_color = "dark orange", border_thickness = 5, gap_thickness = 4):
    button_font = pygame.font.SysFont("Comic Sans", 16)
    button_text = button_font.render(text, True, (255,255,255))
    pygame.draw.rect(screen, color, (x,y,90,35))
    pygame.draw.rect(screen, border_color, (x - gap_thickness - border_thickness, y - gap_thickness - border_thickness,
                                            90 + 2 * (gap_thickness + border_thickness),
                                            35 + 2 * (gap_thickness + border_thickness),
                                            ),
                     border_thickness
                     )
    pygame.draw.rect(screen, "black", (x - 4 - 1, y - 4 - 1, 90 + 2 * 4 + 2, 35 + 2 * 4 + 2,), 1)
    pygame.draw.rect(screen, "black", (x - 4 - 1 - 3, y - 4 - 1 - 3, 90 + 2 * 5 + 6, 35 + 2 * 5 + 6,), 1)
    screen.blit(button_text, (x + 11, y + 5))

def main():
    try:
        screen = pygame.display.set_mode((540, 600))
        welcome_title_font = pygame.font.Font(None, 70)
        select_title_font = pygame.font.Font(None, 50)
        game_over_title_font = pygame.font.Font(None, 70)
        game_won_title_font = pygame.font.Font(None, 70)
        #540x540 Screen
        background_image = pygame.image.load('sudoku_1.jpg')
        background_image = pygame.transform.scale(background_image, (540, 600))
        welcome_surface = welcome_title_font.render("Welcome to Sudoku", 0, "red")
        welcome_rectangle = welcome_surface.get_rect(
            center=(540 // 2, 540 // 2 - 170)
        )
        select_surface = select_title_font.render("Select Game Mode:", 0, "red")
        select_rectangle = select_surface.get_rect(
            center=(540 // 2, 540 // 2 - 50)
        )
        game_over_surface = game_over_title_font.render("Game Over :(", 0, "red")
        game_over_rectangle = game_over_surface.get_rect(
            center=(540 // 2, 540 // 2 - 160)
        )
        game_won_surface = game_won_title_font.render("Game Won!", 0, "red")
        game_won_rectangle=game_won_surface.get_rect(
            center = (540 // 2, 540 // 2 - 160)
        )
        pygame.display.set_caption("Sudoku")
        clock = pygame.time.Clock()
        running = True
        removed_cells = None
        board = None
        selected = None

        #Game loop for menu
        while running and not board:
            screen.blit(background_image, (0,0)) #Custom Background
            screen.blit(welcome_surface, welcome_rectangle)
            screen.blit(select_surface, select_rectangle)
            #Easy, Medium, Hard Buttons
            draw_button(screen, 50, 325, "EASY", button_color)
            draw_button(screen, 220, 325, "MEDIUM", button_color)
            draw_button(screen, 390, 325, "HARD", button_color)

            for event in pygame.event.get(): #Event listener
                if event.type == pygame.QUIT: #Quit button
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickX, clickY = event.pos
                    if 324 <= clickY <= 366:
                        if 49 <= clickX <= 151:
                            removed_cells = 30 #Easy
                        elif 119 <= clickX <= 321:
                            removed_cells = 40 #Medium
                        elif 289 <= clickY <= 491:
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
                    if 551 <= y <= 588:
                        if 100 <= x <= 192:
                            board.reset_to_original()
                        elif 225 <= x <= 317:
                            main()
                        elif 350 <= x <= 442:
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
                            screen.blit(background_image, (0,0))
                            screen.blit(game_won_surface, game_won_rectangle)
                            draw_small_button(screen, 230, 300, "EXIT", button_color)
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
                            screen.blit(background_image, (0, 0))
                            screen.blit(game_over_surface, game_over_rectangle)
                            draw_small_button(screen, 230, 300, "RESTART", button_color)
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
            draw_small_button(screen, 101, 552, " RESET", button_color)
            draw_small_button(screen, 226, 552, "RESTART", button_color)
            draw_small_button(screen, 351, 552, "  EXIT", button_color)

            pygame.display.flip()
            clock.tick(25)

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
