import random, arcade, os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000
MOVEMENT_SPEED = 3
BIRD_SPEED = 1
BULLET_SPEED = 10
SCREEN_TITLE = "Pheonix Reborn"

class Menu(arcade.View):

    def on_show(self):

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):

        arcade.start_render()
        arcade.draw_text("Menu", SCREEN_WIDTH/2, SCREEN_HEIGHT - 70, arcade.color.GREEN, font_size = 50, anchor_x = "center")
        arcade.draw_text("Press to start", SCREEN_WIDTH/2, 75, arcade.color.GREEN, font_size = 20, anchor_x = "center")
        
    def on_mouse_press(self, _x, _y, _button, _modifiers):

        self.window.show_view(Menu1())

class Menu1(arcade.View):

    def on_show(self):

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):

        arcade.start_render()
        arcade.draw_text("LEVEL 1", SCREEN_WIDTH/2, SCREEN_HEIGHT - 70, arcade.color.GREEN, font_size = 50, anchor_x = "center")
        arcade.draw_text("Press to start", SCREEN_WIDTH/2, 75, arcade.color.GREEN, font_size = 20, anchor_x = "center")
        
    def on_mouse_press(self, _x, _y, _button, _modifiers):

        self.window.show_view(Level1())

class Menu2(arcade.View):

    def on_show(self):

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):

        arcade.start_render()
        arcade.draw_text("LEVEL 2", SCREEN_WIDTH/2, SCREEN_HEIGHT - 70, arcade.color.GREEN, font_size = 50, anchor_x = "center")
        arcade.draw_text("YOUR ALREADY SCORED: "+str(score), SCREEN_WIDTH/2, SCREEN_HEIGHT - 250, arcade.color.GREEN, font_size = 50, anchor_x = "center")
        arcade.draw_text("Press to start", SCREEN_WIDTH/2, 75, arcade.color.GREEN, font_size = 20, anchor_x = "center")
        
    def on_mouse_press(self, _x, _y, _button, _modifiers):

        self.window.show_view(Level2())

class Menu3(arcade.View):

    def on_show(self):

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):

        arcade.start_render()
        arcade.draw_text("LEVEL 3", SCREEN_WIDTH/2, SCREEN_HEIGHT - 70, arcade.color.GREEN, font_size = 50, anchor_x = "center")
        arcade.draw_text("YOUR ALREADY SCORED: "+str(score), SCREEN_WIDTH/2, SCREEN_HEIGHT - 250, arcade.color.GREEN, font_size = 50, anchor_x = "center")
        arcade.draw_text("Press to start", SCREEN_WIDTH/2, 75, arcade.color.GREEN, font_size = 20, anchor_x = "center")
        
    def on_mouse_press(self, _x, _y, _button, _modifiers):

        self.window.show_view(Level3())

class GameOver(arcade.View):

    def on_show(self):

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):

        arcade.start_render()
        arcade.draw_text("CONGRATULATIONS", SCREEN_WIDTH/2, SCREEN_HEIGHT - 100, arcade.color.GREEN, font_size = 75, anchor_x = "center")
        arcade.draw_text("YOU COMPLETE GAME", SCREEN_WIDTH/2, SCREEN_HEIGHT - 175, arcade.color.GREEN, font_size = 50, anchor_x = "center")
        arcade.draw_text("YOUR SCORE: "+str(score), SCREEN_WIDTH/2, SCREEN_HEIGHT - 250, arcade.color.GREEN, font_size = 50, anchor_x = "center")
        arcade.draw_text("Press to go to menu", SCREEN_WIDTH/2, 75, arcade.color.GREEN, font_size = 20, anchor_x = "center")
        
    def on_mouse_press(self, _x, _y, _button, _modifiers):

        self.window.show_view(Menu())

class Level1(arcade.View):

    def __init__(self):

        super().__init__()

        self.ship_list = arcade.SpriteList()
        self.bird_list = arcade.SpriteList()
        self.bird_bullet_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.score = 0
        self.total_time = 0.0
        self.counter = 0
        self.lives = 3
        self.bird_deaths = 0

        self.ship_sprite = arcade.Sprite("images/ship.png")
        self.ship_sprite.center_x = 400
        self.ship_sprite.center_y = 50
        self.ship_list.append(self.ship_sprite)

        for x in range(50, SCREEN_WIDTH, 100):
            self.bird_sprite = arcade.Sprite("images/bird.png")
            self.bird_sprite.center_x = x
            self.bird_sprite.center_y = 800
            self.bird_list.append(self.bird_sprite)
        
        for x in range(100, SCREEN_WIDTH, 100):
            self.bird_sprite = arcade.Sprite("images/bird.png")
            self.bird_sprite.center_x = x
            self.bird_sprite.center_y = 750
            self.bird_list.append(self.bird_sprite)
        
        for x in range(150, SCREEN_WIDTH - 100, 100):
            self.bird_sprite = arcade.Sprite("images/bird.png")
            self.bird_sprite.center_x = x
            self.bird_sprite.center_y = 700
            self.bird_list.append(self.bird_sprite)

        for x in range(200, SCREEN_WIDTH - 100, 100):
            self.bird_sprite = arcade.Sprite("images/bird.png")
            self.bird_sprite.center_x = x
            self.bird_sprite.center_y = 650
            self.bird_list.append(self.bird_sprite)

        for x in range(-100, SCREEN_WIDTH, 200):
            wall = arcade.Sprite("images/wall.png")
            wall.angle = 90
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)

        for y in range(-100, SCREEN_HEIGHT, 200):
            wall = arcade.Sprite("images/wall.png")
            wall.center_x = 0
            wall.center_y = y
            self.wall_list.append(wall)
        
        for x in range(-100, SCREEN_WIDTH, 200):
            wall = arcade.Sprite("images/wall.png")
            wall.angle = 90
            wall.center_x = x
            wall.center_y = SCREEN_HEIGHT/3
            self.wall_list.append(wall)

        for y in range(-100, SCREEN_HEIGHT, 200):
            wall = arcade.Sprite("images/wall.png")
            wall.center_x = SCREEN_WIDTH
            wall.center_y = y
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.ship_sprite, self.wall_list)
    
    def on_show(self):

        arcade.set_background_color(arcade.color.BLACK)
        self.window.set_mouse_visible(False)

    def on_draw(self):

        arcade.start_render()

        self.ship_list.draw()
        self.bird_list.draw()
        self.bird_bullet_list.draw()
        self.bullet_list.draw()
        self.wall_list.draw()

        arcade.draw_text("SCORE:"+str(self.score), 0, 945, arcade.color.GREEN, font_size = 50)
        arcade.draw_text("LIVES:"+str(self.lives), 600, 945, arcade.color.GREEN, font_size = 50)

    def on_update(self, delta_time):

        self.ship_list.update()
        self.bullet_list.update()
        self.bird_list.update()
        self.bird_bullet_list.update()
        self.physics_engine.update()

        self.total_time += delta_time

        for self.bird_sprite in self.bird_list:

            self.bird_sprite.change_x = BIRD_SPEED
            if self.total_time > 0.25 + self.counter:
                self.bird_sprite.change_x = -BIRD_SPEED
            if self.total_time > 0.75 + self.counter:
                self.bird_sprite.change_x = BIRD_SPEED
                self.counter += 1

            if random.randrange(int(5 / delta_time)) == 0:
                bird_bullet = arcade.Sprite("images/bullet.png")
                bird_bullet.change_y = -BULLET_SPEED
                bird_bullet.center_x = self.bird_sprite.center_x
                bird_bullet.top = self.bird_sprite.bottom
                self.bird_bullet_list.append(bird_bullet)

        for bullet in self.bullet_list:
            
            hit_list = arcade.check_for_collision_with_list(bullet, self.bird_list)

            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
            
            for bird in hit_list:
                bird.remove_from_sprite_lists()
                self.score += 10
                self.bird_deaths += 1
                if self.bird_deaths == 26:
                    global lives, score
                    lives = self.lives
                    score = self.score
                    self.window.show_view(Menu2())

            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()
                self.score -= 1
        
        for bird_bullet in self.bird_bullet_list:
            
            hit_list = arcade.check_for_collision_with_list(bird_bullet, self.ship_list)

            if len(hit_list) > 0:
                bird_bullet.remove_from_sprite_lists()
            
            for ship in hit_list:
                self.lives -= 1
                if self.lives == 0:
                    ship.remove_from_sprite_lists()
                    self.window.show_view(Menu1())

            if bird_bullet.bottom > SCREEN_HEIGHT:
                bird_bullet.remove_from_sprite_lists()

    def on_key_press(self, key, modifiers):

        if key == arcade.key.SPACE:
            bullet = arcade.Sprite("images/bullet.png")
            bullet.change_y = BULLET_SPEED
            bullet.center_x = self.ship_sprite.center_x
            bullet.bottom = self.ship_sprite.top
            self.bullet_list.append(bullet)

        if key == arcade.key.UP:
            self.ship_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ship_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ship_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.ship_sprite.change_x = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.ship_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ship_sprite.change_x = 0

class Level2(arcade.View):

    def __init__(self):

        super().__init__()

        self.ship_list = arcade.SpriteList()
        self.bird_list = arcade.SpriteList()
        self.bird_bullet_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.score = score
        self.total_time = 0.0
        self.counter1 = 0
        self.counter2 = 0
        self.lives = lives
        self.bird_deaths = 0

        self.ship_sprite = arcade.Sprite("images/ship.png")
        self.ship_sprite.center_x = 400
        self.ship_sprite.center_y = 50
        self.ship_list.append(self.ship_sprite)

        for x in range(100, SCREEN_WIDTH, 150):
            self.bird_sprite = arcade.Sprite("images/bigbird.png", 1.5)
            self.bird_sprite.center_x = x
            self.bird_sprite.center_y = 800
            self.bird_list.append(self.bird_sprite)
        
        for x in range(175, SCREEN_WIDTH - 100, 150):
            self.bird_sprite = arcade.Sprite("images/bigbird.png", 1.5)
            self.bird_sprite.center_x = x
            self.bird_sprite.center_y = 750
            self.bird_list.append(self.bird_sprite)
        
        for x in range(250, SCREEN_WIDTH - 200, 150):
            self.bird_sprite = arcade.Sprite("images/bigbird.png", 1.5)
            self.bird_sprite.center_x = x
            self.bird_sprite.center_y = 700
            self.bird_list.append(self.bird_sprite)

        for x in range(325, SCREEN_WIDTH - 300, 150):
            self.bird_sprite = arcade.Sprite("images/bigbird.png", 1.5)
            self.bird_sprite.center_x = x
            self.bird_sprite.center_y = 650
            self.bird_list.append(self.bird_sprite)

        for x in range(-100, SCREEN_WIDTH, 200):
            wall = arcade.Sprite("images/wall.png")
            wall.angle = 90
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)

        for y in range(-100, SCREEN_HEIGHT, 200):
            wall = arcade.Sprite("images/wall.png")
            wall.center_x = 0
            wall.center_y = y
            self.wall_list.append(wall)
        
        for x in range(-100, SCREEN_WIDTH, 200):
            wall = arcade.Sprite("images/wall.png")
            wall.angle = 90
            wall.center_x = x
            wall.center_y = SCREEN_HEIGHT/3
            self.wall_list.append(wall)

        for y in range(-100, SCREEN_HEIGHT, 200):
            wall = arcade.Sprite("images/wall.png")
            wall.center_x = SCREEN_WIDTH
            wall.center_y = y
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.ship_sprite, self.wall_list)
    
    def on_show(self):

        arcade.set_background_color(arcade.color.BLACK)
        self.window.set_mouse_visible(False)

    def on_draw(self):

        arcade.start_render()

        self.ship_list.draw()
        self.bird_list.draw()
        self.bird_bullet_list.draw()
        self.bullet_list.draw()
        self.wall_list.draw()

        arcade.draw_text("SCORE:"+str(self.score), 0, 945, arcade.color.GREEN, font_size = 50)
        arcade.draw_text("LIVES:"+str(self.lives), 600, 945, arcade.color.GREEN, font_size = 50)

    def on_update(self, delta_time):

        self.ship_list.update()
        self.bullet_list.update()
        self.bird_list.update()
        self.bird_bullet_list.update()
        self.physics_engine.update()

        self.total_time += delta_time

        for self.bird_sprite in self.bird_list:

            self.bird_sprite.change_x = BIRD_SPEED
            if self.total_time > 0.25 + self.counter1:
                self.bird_sprite.change_x = -BIRD_SPEED
            if self.total_time > 0.75 + self.counter1:
                self.bird_sprite.change_x = BIRD_SPEED
                self.counter1 += 1
            
            self.bird_sprite.change_y = BIRD_SPEED
            if self.total_time > 0.25 + self.counter2:
                self.bird_sprite.change_y = -BIRD_SPEED
            if self.total_time > 4.25 + self.counter2:
                self.bird_sprite.change_y = BIRD_SPEED
                self.counter2 += 8

            if random.randrange(int(1 / delta_time)) == 0:
                bird_bullet = arcade.Sprite("images/bullet.png")
                bird_bullet.change_y = -BULLET_SPEED
                bird_bullet.center_x = self.bird_sprite.center_x
                bird_bullet.top = self.bird_sprite.bottom
                self.bird_bullet_list.append(bird_bullet)


        for bullet in self.bullet_list:
            
            hit_list = arcade.check_for_collision_with_list(bullet, self.bird_list)

            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
            
            for bird in hit_list:
                bird.remove_from_sprite_lists()
                self.score += 20
                self.bird_deaths += 1
                if self.bird_deaths == 14:
                    global lives, score
                    lives = self.lives
                    score = self.score
                    self.window.show_view(Menu3())

            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()
                self.score -= 1
        
        for bird_bullet in self.bird_bullet_list:
            
            hit_list = arcade.check_for_collision_with_list(bird_bullet, self.ship_list)

            if len(hit_list) > 0:
                bird_bullet.remove_from_sprite_lists()
            
            for ship in hit_list:
                self.lives -= 1
                if self.lives == 0:
                    ship.remove_from_sprite_lists()
                    self.window.show_view(Menu1())

            if bird_bullet.bottom > SCREEN_HEIGHT:
                bird_bullet.remove_from_sprite_lists()

    def on_key_press(self, key, modifiers):

        if key == arcade.key.SPACE:
            bullet = arcade.Sprite("images/bullet.png")
            bullet.change_y = BULLET_SPEED
            bullet.center_x = self.ship_sprite.center_x
            bullet.bottom = self.ship_sprite.top
            self.bullet_list.append(bullet)

        if key == arcade.key.UP:
            self.ship_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ship_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ship_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.ship_sprite.change_x = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.ship_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ship_sprite.change_x = 0

class Level3(arcade.View):

    def __init__(self):

        super().__init__()

        self.ship_list = arcade.SpriteList()
        self.boss_list = arcade.SpriteList()
        self.bird_list = arcade.SpriteList()
        self.bird_bullet_list = arcade.SpriteList()
        self.brick_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.score = 0
        self.total_time = 0.0
        self.counter = 0
        self.lives = 3
        self.bird_deaths = 0

        self.ship_sprite = arcade.Sprite("images/ship.png")
        self.ship_sprite.center_x = 400
        self.ship_sprite.center_y = 50
        self.ship_list.append(self.ship_sprite)

        for x in range(50, SCREEN_WIDTH, 100):
            self.bird_sprite = arcade.Sprite("images/bird.png")
            self.bird_sprite.center_x = x
            self.bird_sprite.center_y = 800
            self.bird_list.append(self.bird_sprite)
        
        for x in range(100, SCREEN_WIDTH, 100):
            self.bird_sprite = arcade.Sprite("images/bird.png")
            self.bird_sprite.center_x = x
            self.bird_sprite.center_y = 750
            self.bird_list.append(self.bird_sprite)

        for x in range(200, SCREEN_WIDTH - 200, 25):
            self.brick_sprite = arcade.Sprite("images/roof.png")
            self.brick_sprite.center_x = x
            self.brick_sprite.center_y = 700
            self.brick_list.append(self.brick_sprite)

        for x in range(175, SCREEN_WIDTH - 175, 25):
            self.brick_sprite = arcade.Sprite("images/roof.png")
            self.brick_sprite.center_x = x
            self.brick_sprite.center_y = 680
            self.brick_list.append(self.brick_sprite)

        for x in range(150, SCREEN_WIDTH - 425, 25):
            self.brick_sprite = arcade.Sprite("images/roof.png")
            self.brick_sprite.center_x = x
            self.brick_sprite.center_y = 660
            self.brick_list.append(self.brick_sprite)
        
        for x in range(SCREEN_WIDTH - 350, SCREEN_WIDTH - 150, 25):
            self.brick_sprite = arcade.Sprite("images/roof.png")
            self.brick_sprite.center_x = x
            self.brick_sprite.center_y = 660
            self.brick_list.append(self.brick_sprite)

        for x in range(125, SCREEN_WIDTH - 425, 25):
            self.brick_sprite = arcade.Sprite("images/roof.png")
            self.brick_sprite.center_x = x
            self.brick_sprite.center_y = 640
            self.brick_list.append(self.brick_sprite)
        
        for x in range(SCREEN_WIDTH - 350, SCREEN_WIDTH - 125, 25):
            self.brick_sprite = arcade.Sprite("images/roof.png")
            self.brick_sprite.center_x = x
            self.brick_sprite.center_y = 640
            self.brick_list.append(self.brick_sprite)

        for x in range(100, SCREEN_WIDTH - 425, 25):
            self.brick_sprite = arcade.Sprite("images/roof.png")
            self.brick_sprite.center_x = x
            self.brick_sprite.center_y = 620
            self.brick_list.append(self.brick_sprite)
        
        for x in range(SCREEN_WIDTH - 350, SCREEN_WIDTH - 100, 25):
            self.brick_sprite = arcade.Sprite("images/roof.png")
            self.brick_sprite.center_x = x
            self.brick_sprite.center_y = 620
            self.brick_list.append(self.brick_sprite)

        for x in range(75, SCREEN_WIDTH - 75, 25):
            self.brick_sprite = arcade.Sprite("images/platform.png")
            self.brick_sprite.center_x = x
            self.brick_sprite.center_y = 600
            self.brick_list.append(self.brick_sprite)

        for x in range(100, SCREEN_WIDTH - 100, 25):
            self.brick_sprite = arcade.Sprite("images/brick.png")
            self.brick_sprite.center_x = x
            self.brick_sprite.center_y = 580
            self.brick_list.append(self.brick_sprite)
        
        for x in range(125, SCREEN_WIDTH - 125, 25):
            self.brick_sprite = arcade.Sprite("images/brick.png")
            self.brick_sprite.center_x = x
            self.brick_sprite.center_y = 560
            self.brick_list.append(self.brick_sprite)
        
        for x in range(150, SCREEN_WIDTH - 150, 25):
            self.brick_sprite = arcade.Sprite("images/brick.png")
            self.brick_sprite.center_x = x
            self.brick_sprite.center_y = 540
            self.brick_list.append(self.brick_sprite)

        for x in range(175, SCREEN_WIDTH - 175, 25):
            self.brick_sprite = arcade.Sprite("images/brick.png")
            self.brick_sprite.center_x = x
            self.brick_sprite.center_y = 520
            self.brick_list.append(self.brick_sprite)
        
        for x in range(200, SCREEN_WIDTH - 200, 25):
            self.brick_sprite = arcade.Sprite("images/brick.png")
            self.brick_sprite.center_x = x
            self.brick_sprite.center_y = 500
            self.brick_list.append(self.brick_sprite)

        for x in range(225, SCREEN_WIDTH - 225, 25):
            self.brick_sprite = arcade.Sprite("images/brick.png")
            self.brick_sprite.center_x = x
            self.brick_sprite.center_y = 480
            self.brick_list.append(self.brick_sprite)
        
        for x in range(250, SCREEN_WIDTH - 250, 25):
            self.brick_sprite = arcade.Sprite("images/brick.png")
            self.brick_sprite.center_x = x
            self.brick_sprite.center_y = 460
            self.brick_list.append(self.brick_sprite)

        for x in range(-100, SCREEN_WIDTH, 200):
            wall = arcade.Sprite("images/wall.png")
            wall.angle = 90
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)

        for y in range(-100, SCREEN_HEIGHT, 200):
            wall = arcade.Sprite("images/wall.png")
            wall.center_x = 0
            wall.center_y = y
            self.wall_list.append(wall)
        
        for x in range(-100, SCREEN_WIDTH, 200):
            wall = arcade.Sprite("images/wall.png")
            wall.angle = 90
            wall.center_x = x
            wall.center_y = SCREEN_HEIGHT/3
            self.wall_list.append(wall)

        for y in range(-100, SCREEN_HEIGHT, 200):
            wall = arcade.Sprite("images/wall.png")
            wall.center_x = SCREEN_WIDTH
            wall.center_y = y
            self.wall_list.append(wall)
        
        self.boss_sprite = arcade.Sprite("images/boss.png")
        self.boss_sprite.center_x = 400
        self.boss_sprite.center_y = 636
        self.boss_list.append(self.boss_sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(self.ship_sprite, self.wall_list)
    
    def on_show(self):

        arcade.set_background_color(arcade.color.BLACK)
        self.window.set_mouse_visible(False)

    def on_draw(self):

        arcade.start_render()

        self.ship_list.draw()
        self.boss_list.draw()
        self.bird_list.draw()
        self.bird_bullet_list.draw()
        self.bullet_list.draw()
        self.wall_list.draw()
        self.brick_list.draw()

        arcade.draw_text("SCORE:"+str(self.score), 0, 945, arcade.color.GREEN, font_size = 50)
        arcade.draw_text("LIVES:"+str(self.lives), 600, 945, arcade.color.GREEN, font_size = 50)

    def on_update(self, delta_time):

        self.ship_list.update()
        self.boss_list.update()
        self.bullet_list.update()
        self.bird_list.update()
        self.bird_bullet_list.update()
        self.physics_engine.update()
        self.brick_list.update()

        self.total_time += delta_time

        for self.brick_sprite in self.brick_list:

            self.brick_sprite.change_y = - 0.1 * BIRD_SPEED
        
        for self.boss_sprite in self.boss_list:

            self.boss_sprite.change_y = - 0.1 * BIRD_SPEED

        for self.bird_sprite in self.bird_list:

            self.bird_sprite.change_x = BIRD_SPEED
            if self.total_time > 0.25 + self.counter:
                self.bird_sprite.change_x = -BIRD_SPEED
            if self.total_time > 0.75 + self.counter:
                self.bird_sprite.change_x = BIRD_SPEED
                self.counter += 1

            if random.randrange(int(5 / delta_time)) == 0:
                bird_bullet = arcade.Sprite("images/bullet.png")
                bird_bullet.change_y = -BULLET_SPEED
                bird_bullet.center_x = self.bird_sprite.center_x
                bird_bullet.top = self.bird_sprite.bottom
                self.bird_bullet_list.append(bird_bullet)

        for bullet in self.bullet_list:
            
            hit_list1 = arcade.check_for_collision_with_list(bullet, self.brick_list)
            hit_list2 = arcade.check_for_collision_with_list(bullet, self.bird_list)
            hit_list3 = arcade.check_for_collision_with_list(bullet, self.boss_list)

            if len(hit_list1) > 0:
                bullet.remove_from_sprite_lists()

            if len(hit_list2) > 0:
                bullet.remove_from_sprite_lists()

            if len(hit_list3) > 0:
                bullet.remove_from_sprite_lists()

            for brick in hit_list1:
                brick.remove_from_sprite_lists()
                self.score += 5
            
            for bird in hit_list2:
                bird.remove_from_sprite_lists()
                self.score += 10
            
            for boss in hit_list3:
                boss.remove_from_sprite_lists()
                self.score += 100
                self.window.show_view(GameOver())

            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()
                self.score -= 1
        
        for bird_bullet in self.bird_bullet_list:
            
            hit_list = arcade.check_for_collision_with_list(bird_bullet, self.ship_list)

            if len(hit_list) > 0:
                bird_bullet.remove_from_sprite_lists()
            
            for ship in hit_list:
                self.lives -= 1
                if self.lives == 0:
                    ship.remove_from_sprite_lists()
                    self.window.show_view(Menu1())

            if bird_bullet.bottom > SCREEN_HEIGHT:
                bird_bullet.remove_from_sprite_lists()

    def on_key_press(self, key, modifiers):

        if key == arcade.key.SPACE:
            bullet = arcade.Sprite("images/bullet.png")
            bullet.change_y = BULLET_SPEED
            bullet.center_x = self.ship_sprite.center_x
            bullet.bottom = self.ship_sprite.top
            self.bullet_list.append(bullet)

        if key == arcade.key.UP:
            self.ship_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ship_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ship_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.ship_sprite.change_x = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.ship_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ship_sprite.change_x = 0

def main():
    
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.show_view(Menu())
    arcade.run()
    
if __name__ == "__main__":
    main()