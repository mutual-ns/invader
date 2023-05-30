import pygame.font

class Button:
    def __init__(self, ai_game, msg1 ,msg2, msg3):
        #ボタンの属性の初期化
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #ボタンの大きさと属性の設定
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        #ボタンのrectオブジェクトを生成し、画面の中央に配置する
        self.rect = pygame.Rect(0, 0, self.width ,self.height)
        self.rect.center = self.screen_rect.center

        self.rect2 = pygame.Rect(0, 0, self.width ,self.height)
        self.rect2.center = self.screen_rect.center
        self.rect2.top = self.screen_rect.top +150

        self.rect3 = pygame.Rect(0, 0, self.width ,self.height)
        self.rect3.center = self.screen_rect.center
        self.rect3.bottom = self.screen_rect.bottom -150

        self.rect4 = pygame.Rect(0, 0, self.width+50 ,self.height+50)
        self.rect5 = pygame.Rect(0, 0, self.width+30 ,self.height+30)
        self.rect4.center = self.screen_rect.center
        self.rect5.center = self.screen_rect.center

        self.rect6 = pygame.Rect(0, 0, self.width+50 ,self.height+50)
        self.rect7 = pygame.Rect(0, 0, self.width+30 ,self.height+30)
        self.rect6.center = self.rect2.center
        self.rect7.center = self.rect2.center

        self.rect8 = pygame.Rect(0, 0, self.width+50 ,self.height+50)
        self.rect9 = pygame.Rect(0, 0, self.width+30 ,self.height+30)
        self.rect8.center = self.rect3.center
        self.rect9.center = self.rect3.center

        #ボタンのメッセージは一度だけ準備する必要がある
        self._prep_msg(msg1)
        self._prep_msg_2(msg2)
        self._prep_msg_3(msg3)
        
    def _prep_msg(self, msg):
        #msgを画像に変換しボタンの中央に配置する
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def _prep_msg_2(self, msg):
        #msgを画像に変換しボタンの中央に配置する
        self.msg_image_2 = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect_2 = self.msg_image.get_rect()
        self.msg_image_rect_2.center = self.rect.center 
        self.msg_image_rect_2.center = self.rect2.center

    def _prep_msg_3(self, msg):
        #msgを画像に変換しボタンの中央に配置する
        self.msg_image_3 = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect_3 = self.msg_image.get_rect()
        self.msg_image_rect_3.center = self.rect.center
        self.msg_image_rect_3.center = self.rect3.center

    def draw_button(self):
        if self.stats.difficulty == 1:
            self.screen.fill(self.button_color, self.rect4)
            self.screen.fill(self.settings.bg_color, self.rect5)
            self.screen.fill(self.button_color, self.rect)
            self.screen.blit(self.msg_image, self.msg_image_rect)
            self.screen.fill(self.button_color, self.rect2)
            self.screen.blit(self.msg_image_2, self.msg_image_rect_2)
            self.screen.fill(self.button_color, self.rect3)
            self.screen.blit(self.msg_image_3, self.msg_image_rect_3)
        if self.stats.difficulty == 2:
            self.screen.fill(self.button_color, self.rect6)
            self.screen.fill(self.settings.bg_color, self.rect7)
            self.screen.fill(self.button_color, self.rect)
            self.screen.blit(self.msg_image, self.msg_image_rect)
            self.screen.fill(self.button_color, self.rect2)
            self.screen.blit(self.msg_image_2, self.msg_image_rect_2)
            self.screen.fill(self.button_color, self.rect3)
            self.screen.blit(self.msg_image_3, self.msg_image_rect_3)
        if self.stats.difficulty == 0:
            self.screen.fill(self.button_color, self.rect8)
            self.screen.fill(self.settings.bg_color, self.rect9)
            self.screen.fill(self.button_color, self.rect)
            self.screen.blit(self.msg_image, self.msg_image_rect)
            self.screen.fill(self.button_color, self.rect2)
            self.screen.blit(self.msg_image_2, self.msg_image_rect_2)
            self.screen.fill(self.button_color, self.rect3)
            self.screen.blit(self.msg_image_3, self.msg_image_rect_3)