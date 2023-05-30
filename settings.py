class Settings:
    #エイリアン侵略の全設定を格納するクラス

    def __init__(self):
        #ゲームの初期設定
        #画面に関する設定
        
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color =(230,230,230)

        #宇宙船の設定
        #self.ship_speed = 1.0
        self.ship_limit = 3 #宇宙船の残基

        #弾の設定
        #self.bullet_speed = 0.2
        self.bullet_width = 1000
        self.bullet_height = 20
        self.bullet_color = (60,60,60)
        self.bullet_time = 500 #連射の間隔の調整  

        #エイリアンの設定
        #self.alien_speed = 0.1
        self.alien_speed_debug = 10 #a keyを押している間加速するスピードの値
        self.fleet_drop_speed = 5
        #self.fleet_direction = 1

        #ゲームスピードの変化
        self.ship_speedup_scale = 1.1
        self.bullet_speedup_scale = 1.1
        self.alien_speedup_scale = 1.1

        self.score_scale = 1.5

        self.alien_points = 50

        self.alien_speed_hard = 0.2
        self.alien_speed_easy = 0.07

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #ゲーム中の設定値の初期化
        self.ship_speed = 1.0
        self.bullet_speed = 0.2
        self.alien_speed = 0.1
        self.fleet_direction = 1

    def increase_speed(self):
        #速度の設定値を増やす
        self.ship_speed *= self.ship_speedup_scale
        self.bullet_speed *= self.bullet_speedup_scale
        self.alien_speed *= self.alien_speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

            




        