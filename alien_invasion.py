import sys
import pygame
from time import sleep

from settings import Settings

from ship import Ship

from bullet import Bullet
from bullet import Bullet_2
from bullet import Bullet_3

from alien import Alien

from button import Button

from game_stats import GameStats

from scoreboard import Scoreboard


class AlienInvasion:
    #ゲームの全体の管理

    def __init__(self):
        #ゲームの初期化
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("エイリアン侵略")

        #ゲームの統計情報を格納するインスタンスの作成
        self.stats = GameStats(self)

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.bullets_2 = pygame.sprite.Group()
        self.bullets_3 = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.bullet_keep = False
        self.bullet_time = 0

        self.reset_bool = True 
        self.start_ticks = float('inf')

        #playボタン
        self.play_button = Button(self, "Normal", "Hard" , "Easy")

        #得点表示
        self.sb = Scoreboard(self)


    def run_game(self):
        #ゲームのメインループの開始
        while True:
            self._check_events()  #ゲーム終了キーなどを有効にするためにここは以下に入れない
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                if self.bullet_keep:
                    self.bullet_time += 1
                    self.bullet_time%=self.settings.bullet_time
                    self._fire_bullet()
                self._update_aliens()
            self._update_screen()
            #print(self.stats.ships_left) #デバッグ用
            
          
    def _check_events(self):
        for  event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos =pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
                    
    
    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT: 
            self.ship.moving_left =True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.bullet_keep = True
            self._fire_bullet()
        elif event.key == pygame.K_a:
            self.settings.alien_speed += self.settings.alien_speed_debug 
        elif event.key == pygame.K_p:
            self._start_game()
            self.settings.initialize_dynamic_settings()
            if self.stats.difficulty == 2:
                self.settings.alien_speed = self.settings.alien_speed_hard
            elif self.stats.difficulty == 0:
                self.settings.alien_speed = self.settings.alien_speed_easy
        elif event.key == pygame.K_r: #rでリセット
            self.stats.ships_left = 0
            self._ship_hit()
        if not self.stats.game_active:
            if event.key == pygame.K_DOWN:
                self.stats.difficulty -= 1
                self.stats.difficulty %=3
            elif event.key == pygame.K_UP:
                self.stats.difficulty += 1
                self.stats.difficulty %=3

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_SPACE:
            self.bullet_keep = False
            self.bullet_time = 0
        elif event.key == pygame.K_a:
            self.settings.alien_speed -= self.settings.alien_speed_debug 

    def _fire_bullet(self):
        #新しい弾を生成し、bulletsグループに追加する
        if self.bullet_time%self.settings.bullet_time == 0:
            if self.stats.level < 6:
                new_bullet = Bullet(self,0)
                self.bullets.add(new_bullet)
            elif self.stats.level >= 6:
                new_bullet_2 = Bullet_2(self,0)
                self.bullets_2.add(new_bullet_2)
                new_bullet_3 = Bullet_3(self,0)
                self.bullets_3.add(new_bullet_3)

    def _update_bullets(self):
        #弾の位置の更新、画面外の弾の削除
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)
            self._check_bullet_alien_collisions() 

        self.bullets_2.update()
        for bullet in self.bullets_2.copy():
            if bullet.rect.bottom <=0:
                self.bullets_2.remove(bullet)
            self._check_bullet_alien_collisions()

        self.bullets_3.update()
        for bullet in self.bullets_3.copy():
            if bullet.rect.bottom <=0:
                self.bullets_3.remove(bullet)
            self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        #弾がエイリアンに当たったか判定
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points*len(aliens)
                self.sb.prep_score()
                self.sb.check_highscore()
        collisions_2 = pygame.sprite.groupcollide(self.bullets_2, self.aliens, True, True)
        if collisions_2:
            for aliens in collisions_2.values():
                self.stats.score += self.settings.alien_points*len(aliens)
                self.sb.prep_score()
                self.sb.check_highscore()
        collisions_3 = pygame.sprite.groupcollide(self.bullets_3, self.aliens, True, True)
        if collisions_3:
            for aliens in collisions_3.values():
                self.stats.score += self.settings.alien_points*len(aliens)
                self.sb.prep_score()
                self.sb.check_highscore()

        if not self.aliens:
            self.bullets.empty()
            self.bullets_2.empty()
            self.bullets_3.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()


    def _update_aliens(self):
        #艦隊にいる全エイリアンの位置を更新する
        self._check_fleet_edges()
        self.aliens.update()
        #エイリアンと宇宙船の衝突の検出
        if self.reset_bool:
            if pygame.sprite.spritecollideany(self.ship, self.aliens):
                self.reset_bool = False
                self.start_ticks=pygame.time.get_ticks()
        if pygame.time.get_ticks() > self.start_ticks+300:  #衝突からディレイをかけて再起動
            self._ship_hit()
        
        self._check_aliens_bottom()

                
    
    def _update_screen(self):
        #ループの度に画面を再描画する
        self.screen.fill(self.settings.bg_color)
 

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        for bullet in self.bullets_2.sprites():
            bullet.draw_bullet()

        for bullet in self.bullets_3.sprites():
            bullet.draw_bullet()            

        self.aliens.draw(self.screen)
        self.ship.blitme()
        
        if not self.stats.game_active:
            self.play_button.draw_button()

        #得点の描画
        self.sb.show_score()
        

        #ゲームの最新の画面を表示する
        pygame.display.flip()

    def _create_fleet(self):
        #エイリアンの艦隊を作成する
        #1匹のエイリアンを作成する
        alien = Alien(self)
        alien_width , alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x // (2*alien_width)

        #画面に収まるエイリアンの列数を決定する
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3*alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)

        #エイリアンの艦隊を作成する
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                #エイリアンを1匹作成し列の中に配置する
                self._create_alien(alien_number, row_number, alien_width, alien_height)

    def _create_alien(self, alien_number,row_number ,alien_width, alien_height):
            alien = Alien(self)
            alien.x = alien_width + 2*alien_width*alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
            self.aliens.add(alien)

    def _check_fleet_edges(self):
        #エイリアンが画面の端に到達した際に適切な処理を行う
        for alien in  self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        #艦隊を下に移動して、横方向の移動を変更
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        #エイリアンと宇宙船の衝突
        if self.stats.ships_left > 1:
            #宇宙船の残基を減らす
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            #残ったエイリアンと弾の消去
            self.aliens.empty()
            self.bullets.empty()
            self.bullets_2.empty()
            self.bullets_3.empty()

            #新しい艦隊の生成
            self._create_fleet()
            self.ship.center_ship()

            self.reset_bool = True

            self.start_ticks = float('inf')


            #一時停止
            sleep(0.5)
        else:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.stats.game_active = False
            self.start_ticks = float('inf')
            pygame.mouse.set_visible(True) #カーソルの可視化

    def _check_aliens_bottom(self):
        #エイリアンが画面の一番下に来たか
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _check_play_button(self, mouse_pos):
        #playボタンで新規ゲームの開始
        if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
            self._start_game()
            self.settings.initialize_dynamic_settings()
            if self.stats.difficulty == 2:
                self.settings.alien_speed = self.settings.alien_speed_hard
            elif self.stats.difficulty == 0:
                self.settings.alien_speed = self.settings.alien_speed_easy

    def _start_game(self):
            "初期化"
            self.stats.reset_stats()
            self.stats.game_active = True

            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            
            self.aliens.empty()
            self. bullets.empty()
            self.bullets_2.empty()
            self.bullets_3.empty()

            self._create_fleet()
            self.ship.center_ship()


            #マウスカーソルの非表示
            pygame.mouse.set_visible(False)        





if __name__ == '__main__':
    #ゲームのインスタンスの作成、ゲームの実行
    ai = AlienInvasion()
    ai.run_game()
    