import pygame
class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100
    def draw_cursor(self):
        self.game.draw_text("*", 40, self.cursor_rect.x, self.cursor_rect.y)
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()
class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h - 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 30
        self.detailsx, self.detailsy = self.mid_w, self.mid_h + 60
        self.infosx, self.infosy = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('3D MAZE GAME', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 - 20)
            self.game.draw_text("EASY", 20, self.startx, self.starty)
            self.game.draw_text("MEDIUM", 20, self.optionsx, self.optionsy)
            self.game.draw_text("HARD", 20, self.creditsx, self.creditsy)
            self.game.draw_text("DETAILS", 20, self.detailsx, self.detailsy)
            self.game.draw_text("CREDITS", 20, self.infosx, self.infosy)
            self.draw_cursor()
            self.blit_screen()
    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.detailsx + self.offset, self.detailsy)
                self.state = 'Details'
            elif self.state == 'Details':
                self.cursor_rect.midtop = (self.infosx + self.offset, self.infosy)
                self.state = 'Infos'
            elif self.state == 'Infos':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.infosx + self.offset, self.infosy)
                self.state = 'Infos'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Details':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Infos':
                self.cursor_rect.midtop = (self.detailsx + self.offset, self.detailsy)
                self.state = 'Details'
    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                import easy
            elif self.state == 'Options':
                import medium
            elif self.state == 'Credits':
                import hard
            elif self.state == 'Details':
                self.game.curr_menu = self.game.details
            elif self.state == 'Infos':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class DetailsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('GAME DETAILS',20,self.game.DISPLAY_W/2,self.game.DISPLAY_H/2-50)
            self.game.draw_text('This game will demonstrate how collision detection works in panda and provide a simple implementation of its use', 8, self.game.DISPLAY_W / 2, self.game.DISPLAY_H/2 - 20)
            self.game.draw_text('Collisions are used extensively in modern games for a variety of purposes. At the most basic level', 8, self.game.DISPLAY_W / 2, self.game.DISPLAY_H/2 - 10)
            self.game.draw_text('collision detection allows for two objects to bump into each other and react', 8, self.game.DISPLAY_W / 2, self.game.DISPLAY_H/2 )
            self.game.draw_text('This can be used to keep the objects from passing through each other but is not limited to that purpose', 8, self.game.DISPLAY_W / 2, self.game.DISPLAY_H/2+10 )
            self.game.draw_text('In this tutorial, collision detection be used to simulate the game of Labyrinth and will keep the ball', 8, self.game.DISPLAY_W / 2, self.game.DISPLAY_H/2+20 )
            self.game.draw_text('within the bounds of the board It will also be used to detect if the ball is over a hole', 8, self.game.DISPLAY_W / 2, self.game.DISPLAY_H/2+30 )
            self.blit_screen()

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('MADE BY INTERNS AT CONTRIVER:', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H/3 - 20)
            self.game.draw_text('AHMED SHOIEB AQHTAR', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 20)
            self.game.draw_text('DARSHINIRAJ C B', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 60)
            self.game.draw_text('POOJA R', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 100)
            self.game.draw_text('DILEEP KUMAR S B', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 140)
            self.blit_screen()