import random
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000
MOVEMENT_SPEED = 5
BULLET_SPEED = 5
SCREEN_TITLE = "Pheonix Reborn"


class Player(arcade.Sprite):

    def update(self):

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class MyGame(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.player_list = None
        self.player_sprite = None
        self.bullet_list = None

        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("images/spaceship.png")
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

    def on_draw(self):

        arcade.start_render()

        self.player_list.draw()
        self.bullet_list.draw()

        output = "SCORE"
        arcade.draw_text(output, 0, 945, arcade.color.GREEN, 50)

    def on_update(self, delta_time):

        self.player_list.update()
        self.bullet_list.update()

        for bullet in self.bullet_list:
            
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

    def on_key_press(self, key, modifiers):

        if key == arcade.key.SPACE:
            bullet = arcade.Sprite("images/bullet.png")
            bullet.change_y = BULLET_SPEED
            bullet.center_x = self.player_sprite.center_x
            bullet.bottom = self.player_sprite.top
            self.bullet_list.append(bullet)

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

def main():
    
    window = MyGame()
    window.setup()
    arcade.run()
    
if __name__ == "__main__":
    main()