import random
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000
MOVEMENT_SPEED = 3
BULLET_SPEED = 10
SCREEN_TITLE = "Pheonix Reborn"

class MenuView(arcade.View):

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("MENU", SCREEN_WIDTH/2, SCREEN_HEIGHT - 70, arcade.color.GREEN, font_size = 50, anchor_x = "center")
        arcade.draw_text("Naciśnij aby rozpocząć", SCREEN_WIDTH/2, 75, arcade.color.GREEN, font_size = 20, anchor_x = "center")
        

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instructions_view = MyGame()
        self.window.show_view(instructions_view)


class Player(arcade.Sprite):

    def update(self):

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT/3:
            self.top = SCREEN_HEIGHT/3

class MyGame(arcade.View):

    def __init__(self):

        super().__init__()

        self.ship_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.score = 0

        self.ship_sprite = arcade.Sprite("images/ship.png")
        self.ship_sprite.center_x = 400
        self.ship_sprite.center_y = 50
        self.ship_list.append(self.ship_sprite)

        for x in range(-100, SCREEN_WIDTH-100, 4):
            wall = arcade.Sprite("images/wall.png")
            wall.angle = 90
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)

        for y in range(-100, SCREEN_HEIGHT-100, 5):
            wall = arcade.Sprite("images/wall.png")
            wall.center_x = 0
            wall.center_y = y
            self.wall_list.append(wall)
        
        for x in range(-100, SCREEN_WIDTH-100, 4):
            wall = arcade.Sprite("images/wall.png")
            wall.angle = 90
            wall.center_x = x
            wall.center_y = SCREEN_HEIGHT/3
            self.wall_list.append(wall)

        for y in range(-100, SCREEN_HEIGHT-100, 5):
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
        self.bullet_list.draw()
        self.wall_list.draw()

        output = "SCORE"
        arcade.draw_text(output, 0, 945, arcade.color.GREEN, font_size = 50)

    def on_update(self, delta_time):

        self.ship_list.update()
        self.bullet_list.update()
        self.physics_engine.update()

        for bullet in self.bullet_list:
            
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

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
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()
    
if __name__ == "__main__":
    main()