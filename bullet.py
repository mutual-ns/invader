import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #宇宙船から発射される弾を管理するクラス

    def __init__(self, ai_game, t):
        #宇宙船の現在の位置から弾のオブジェクトを生成する
        super().__init__()  #親クラスのinitの実行
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #球のrectを（0，0）の位置に作成してから、正しい位置を設定する
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect2_1 = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect2_2 = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)

        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.width = float(self.rect.width)

        self.t=t


    def update(self):
        #画面上の弾を移動する
        #弾の浮動小数点数での位置を更新する
        self.y -= self.settings.bullet_speed+self.t
        #rectの位置を更新する
        self.rect.y = self.y
        self.x+=0.01
        self.rect.x = self.x
        self.width-=0.02
        self.rect.width = self.width
        self.t += 0.008
        

    
    def draw_bullet(self):
        #画面に弾を描画する
        pygame.draw.rect(self.screen, self.color, self.rect)
class Bullet_2(Sprite):
    #宇宙船から発射される弾を管理するクラス

    def __init__(self, ai_game, t):
        #宇宙船の現在の位置から弾のオブジェクトを生成する
        super().__init__()  #親クラスのinitの実行
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #球のrectを（0，0）の位置に作成してから、正しい位置を設定する
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect2_1 = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect2_2 = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)

        self.rect.midtop = ai_game.ship.rect.topright

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.width = float(self.rect.width)

        self.t=t


    def update(self):
        #画面上の弾を移動する
        #弾の浮動小数点数での位置を更新する
        self.y -= self.settings.bullet_speed+self.t
        #rectの位置を更新する
        self.rect.y = self.y
        self.x+=0.01
        self.rect.x = self.x
        self.width-=0.02
        self.rect.width = self.width
        self.t += 0.008
        

    
    def draw_bullet(self):
        #画面に弾を描画する
        pygame.draw.rect(self.screen, self.color, self.rect)

class Bullet_3(Sprite):
    #宇宙船から発射される弾を管理するクラス

    def __init__(self, ai_game, t):
        #宇宙船の現在の位置から弾のオブジェクトを生成する
        super().__init__()  #親クラスのinitの実行
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #球のrectを（0，0）の位置に作成してから、正しい位置を設定する
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect2_1 = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect2_2 = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)

        self.rect.midtop = ai_game.ship.rect.topleft

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.width = float(self.rect.width)

        self.t=t


    def update(self):
        #画面上の弾を移動する
        #弾の浮動小数点数での位置を更新する
        self.y -= self.settings.bullet_speed+self.t
        #rectの位置を更新する
        self.rect.y = self.y
        self.x+=0.01
        self.rect.x = self.x
        self.width-=0.02
        self.rect.width = self.width
        self.t += 0.008
        

    
    def draw_bullet(self):
        #画面に弾を描画する
        pygame.draw.rect(self.screen, self.color, self.rect)



