import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    #得点の情報

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #得点表示のフォント
        self.text_color =(30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        #初期の得点画像を準備する
        self.prep_score()
        self.prep_highscore()
        self.prep_level()
        self.prep_ships()


    def prep_score(self):
        #rounded_score = round(self.stats.score, -1)
        score_str = "Score: ""{:,}".format(self.stats.score)
        #score_str =str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -20  #右端から20ピクセル
        self.score_rect.top = 20 #上から20ピクセル

    def prep_highscore(self):
        #ハイスコアの描画
        #rounded_score = round(self.stats.score, -1)
        highscore_str = "Highscore: "+"{:,}".format(self.stats.highscore)
        #score_str =str(self.stats.score)
        self.highscore_image = self.font.render(highscore_str, True, self.text_color, self.settings.bg_color)

        self.highscore_rect = self.score_image.get_rect()
        self.highscore_rect.center = self.screen_rect.center
        self.highscore_rect.top = 20

    def prep_level(self):
        level_str = "Level: " + str(self.stats.level)

        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right -20
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        #残基の表示
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


        


    def show_score(self):
        #画面に得点を描画
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highscore_image, self.highscore_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    
    def check_highscore(self):
        #ハイスコアの更新
        if self.stats.score > self.stats.highscore:
            self.stats.highscore = self.stats.score
            self.prep_highscore()