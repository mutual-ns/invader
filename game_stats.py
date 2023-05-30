class GameStats:
    #インベーダーゲームの統計情報の記録


    def __init__(self, ai_game):
        #統計情報の初期化
        self.settings = ai_game.settings
        self.reset_stats()
        #self.game_active = True

        #非アクティブでゲームを開始
        self.game_active = False
        self.highscore = 0
        self.difficulty = 1


    def reset_stats(self):
        #初期化
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.power = 1  #弾の強さ
        self.level = 1
