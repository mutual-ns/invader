import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    #宇宙船を管理するクラス

    def __init__(self, ai_game):
        super().__init__()
        #宇宙船を初期化し、開始時の位置を特定する

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.screen_rect = ai_game.screen.get_rect() #画面のrect属性にアクセス

        #宇宙船の画像を読み込み、サイズを取得する
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect() #画像のrect属性にアクセス

        self.rect.midbottom = self.screen_rect.midbottom #画像のmidbottm=画面のmidbottom

        #宇宙船の水平位置の浮動小数点数を格納する
        self.x=float(self.rect.x)

        #移動フラグ
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        #移動フラグによって宇宙船の位置を更新する
        #宇宙船のxの値を更新する
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left>=0 :
            self.x -= self.settings.ship_speed

        #self.xからrectオブジェクトの位置を更新する
        self.rect.x = self.x  #整数部分だけが格納される 


    def blitme(self):
        #宇宙船を現在の位置に描画する
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        #宇宙船を中央に配置する
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)



