import arcade
import arcade.gui
from arcade.gui import UIManager
import random
from spritehealt import SpriteWithHealth, PlayerSprite
from sprites import *


#Main menu
class MyView(arcade.View):
    """Create main menu"""
    def __init__(self):
        super().__init__()

        self.playership_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()
        self.ui_manager = UIManager()
        self.background_sound = arcade.load_sound(":resources:music/1918.mp3")
        arcade.play_sound(self.background_sound)

        for i in range(3):
            playership = StarSprites(":resources:images/space_shooter/playerShip1_green.png", 1)
            playership.center_x = random.randrange(800)
            playership.center_y = random.randrange(0, 100)
            playership.change_y = 0.5
            self.playership_list.append(playership)

        for i in range(50):
            star = StarSprites(":resources:images/items/star.png", 0.1)
            star.center_x = random.randrange(800)
            star.center_y = random.randrange(100, 600)
            self.star_list.append(star)


    def on_draw(self):

        arcade.start_render()
        self.playership_list.draw()
        self.star_list.draw()

    def on_show_view(self):

        self.setup()
        self.window.set_mouse_visible(True)
        arcade.set_background_color(arcade.color.GRAPE)

    def on_hide_view(self):

        self.ui_manager.unregister_handlers()

    def setup(self):

        self.ui_manager.purge_ui_elements()

        y_slot = self.window.height // 4
        left_column_x = self.window.width // 4
        right_column_x = 3 * self.window.width // 4

        button_normal = arcade.load_texture(':resources:gui_basic_assets/red_button_normal.png')
        hovered_texture = arcade.load_texture(':resources:gui_basic_assets/red_button_hover.png')
        pressed_texture = arcade.load_texture(':resources:gui_basic_assets/red_button_press.png')

        start_button = MyFlatButton(
            center_x=self.window.width // 2.75,
            center_y=y_slot * 3,
            normal_texture=button_normal,
            hover_texture=hovered_texture,
            press_texture=pressed_texture,
            text='EASY'
        )
        self.ui_manager.add_ui_element(start_button)

        start_hard_button = MyHardFlatButton(
            center_x= self.window.width - (self.window.width // 2.75),
            center_y=y_slot * 3,
            normal_texture=button_normal,
            hover_texture=hovered_texture,
            press_texture=pressed_texture,
            text='HARD'
        )
        self.ui_manager.add_ui_element(start_hard_button)

        result_button = MyFlatResultButton(
            'The best results',
            center_x=left_column_x,
            center_y=y_slot * 2,
            width=250,
            # height=20
        )
        self.ui_manager.add_ui_element(result_button)

        how_button = MyFlatAbtButton(
            'About me',
            center_x=left_column_x,
            center_y=y_slot * 1,
            width=250
        )
        self.ui_manager.add_ui_element(how_button)

        author_button = MyFlatHowButton(
            'How to play?',
            center_x=right_column_x,
            center_y=y_slot * 2,
            width=250
        )
        self.ui_manager.add_ui_element(author_button)

        close_button = MyFlatCloseButton(
            'Close',
            center_x=right_column_x,
            center_y=y_slot * 1,
            width=250,
            # height=20
        )
        self.ui_manager.add_ui_element(close_button)

    def on_update(self, delta_time: float):

        self.playership_list.update()

#Buttons

class MyFlatButton(arcade.gui.UIImageButton):
    """Create 'START' button(easy version)"""

    def on_click(self):
        game_view = GameView()
        window.show_view(game_view)


class MyHardFlatButton(arcade.gui.UIImageButton):
    """Create 'START' button(hard version)"""

    def on_click(self):
        game_view = HardGameView()
        window.show_view(game_view)


class MyFlatAbtButton(arcade.gui.UIFlatButton):
    """Create 'About me' button"""

    def on_click(self):
        about_me_view = AboutMeView()
        window.show_view(about_me_view)


class MyFlatCloseButton(arcade.gui.UIFlatButton):
    """Create 'Close' button"""

    def on_click(self):
        window.close()


class MyFlatHowButton(arcade.gui.UIFlatButton):
    """Create instruction button"""

    def on_click(self):
        instructions_view = InstructionView()
        window.show_view(instructions_view)


class MyFlatResultButton(arcade.gui.UIFlatButton):
    """Create result button"""

    def on_click(self):
        best_result_view = BestResultView()
        window.show_view(best_result_view)


class TryAgainButton(arcade.gui.UIFlatButton):
    """Create 'try again'' button(easy version)"""

    def on_click(self):
        menu_view = GameView()
        window.show_view(menu_view)


class TryHardAgainButton(arcade.gui.UIFlatButton):
    """Create 'try again'' button(hard version)"""

    def on_click(self):
        menu_view = HardGameView()
        window.show_view(menu_view)


class BacktoButton(arcade.gui.UIFlatButton):
    """Create 'back to menu'' button"""

    def on_click(self):
        my_view = MyView()
        window.show_view(my_view)


# GameViews #

# Easy version
class GameView(arcade.View):
    """Create the easy game"""

    def __init__(self):
        super().__init__()

        self.score = 0
        self.time_taken = 0
        self.bullet_list = arcade.SpriteList()
        self.supernova_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()
        self.background_star_list = arcade.SpriteList()


        #Create a player
        self.player_sprite = PlayerSprite(":resources:images/space_shooter/playerShip1_orange.png", 0.5, max_health=3)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        #Sounds
        self.death_sound = arcade.load_sound(":resources:sounds/hit5.wav")
        self.gun_sound = arcade.load_sound(":resources:sounds/hurt5.wav")
        self.star_sound = arcade.load_sound(":resources:sounds/explosion2.wav")
        self.end_sound = arcade.load_sound(":resources:sounds/phaseJump1.wav")


        #Create a background
        for i in range(25):
            background_star = BackgroundSprites(":resources:images/items/star.png", 0.1)
            background_star.center_x = random.randrange(800)
            background_star.center_y = random.randrange(0, 600)
            self.background_star_list.append(background_star)

        #Create meteors
        for i in range(50):
            asteroid = SpriteWithHealth(":resources:images/space_shooter/meteorGrey_big1.png", 0.25, max_health=3)
            asteroid.center_x = random.randrange(800)
            asteroid.center_y = random.randrange(150, 600)
            self.asteroid_list.append(asteroid)
            asteroid.change_x = 0.5

        # Create asteroids
        for i in range(50):
            star = StarSprites(":resources:images/pinball/bumper.png", 0.25)
            star.center_x = random.randrange(800)
            star.center_y = random.randrange(150, 600)
            star.change_x = -0.5
            self.star_list.append(star)


    def on_show(self):

        arcade.set_background_color(arcade.color.OXFORD_BLUE)
        self.window.set_mouse_visible(False)

    def on_draw(self):

        arcade.start_render()
        self.asteroid_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()
        self.star_list.draw()
        self.supernova_list.draw()
        self.background_star_list.draw()
        arcade.draw_text(f"Score:{self.score}", 10, 20, arcade.color.WHITE, 14)

        #Create health numbers and bars for asteroids
        for asteroid in self.asteroid_list:
            asteroid.draw_health_number()
            asteroid.draw_health_bar()

        # Create health number and bar for player
        for player in self.player_list:
            player.draw_health_number()
            player.draw_health_bar()


    def on_update(self, delta_time):

        self.time_taken += delta_time
        self.bullet_list.update()
        self.asteroid_list.update()
        self.supernova_list.update()
        self.star_list.update()

        #End the game after hitting the player three times
        for supernova in self.supernova_list:
            hit2_list = arcade.check_for_collision_with_list(supernova, self.player_list)

            for player in hit2_list:
                supernova.remove_from_sprite_lists()
                arcade.play_sound(self.death_sound)
                player.current_health -= 1

                if player.current_health <= 0:
                    arcade.play_sound(self.end_sound)
                    game_over_view = GameOverView()
                    game_over_view.score = self.score
                    window.show_view(game_over_view)


        #Remove bullets after impact and meteorites when they lose all health points
        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.asteroid_list)

            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            for asteroid in hit_list:
                arcade.play_sound(self.death_sound)
                asteroid.current_health -= 1
                self.score += 1

                if asteroid.current_health <= 0:
                    asteroid.remove_from_sprite_lists()
                    self.score += 1
                    arcade.play_sound(self.death_sound)
                else:
                    arcade.play_sound(self.death_sound)

        # Remove asteroids after impact
        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.star_list)

            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            for star in hit_list:
                star.remove_from_sprite_lists()
                arcade.play_sound(self.star_sound)
                self.score += 1

        #End the game after 20 seconds
        if round(self.time_taken, 2) > 20.00 :
            game_over_view = GameOverView()
            game_over_view.score = self.score
            window.show_view(game_over_view)


    def on_mouse_motion(self, x, y, _dx, _dy):

        #Only move along the x axis
        self.player_sprite.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):

        SPRITE_SCALING_LASER = 0.8
        BULLET_SPEED = 5

        arcade.play_sound(self.gun_sound)
        # Create a bullet
        bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_LASER)
        bullet.angle = 90
        bullet.change_y = BULLET_SPEED
        bullet.center_x = self.player_sprite.center_x
        bullet.bottom = self.player_sprite.top
        self.bullet_list.append(bullet)

        #Choose whether to send a bullet or not
        choice = random.choice([True, False])
        if choice:
            supernova = SupernovaSprites(":resources:images/space_shooter/laserRed01.png", 1)
            supernova.center_x = random.randrange(800)
            supernova.center_y = 600
            supernova.angle = 180
            self.supernova_list.append(supernova)
            supernova.change_y = -1




# hard version
class HardGameView(arcade.View):
    """Create the hard game"""
    
    def __init__(self):
        super().__init__()

        self.score = 0
        self.time_taken = 0
        self.bullet_list = arcade.SpriteList()
        self.supernova_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()
        self.background_star_list = arcade.SpriteList()


        #Create a player
        self.player_sprite = PlayerSprite(":resources:images/space_shooter/playerShip1_green.png", 0.5, max_health=3)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        #Sounds
        self.death_sound = arcade.load_sound(":resources:sounds/hit5.wav")
        self.gun_sound = arcade.load_sound(":resources:sounds/hurt5.wav")
        self.star_sound = arcade.load_sound(":resources:sounds/explosion2.wav")

        # Create a background
        for i in range(25):
            background_star = BackgroundSprites(":resources:images/items/star.png", 0.1)
            background_star.center_x = random.randrange(800)
            background_star.center_y = random.randrange(0, 600)
            self.background_star_list.append(background_star)

        #Create meteors
        for i in range(50):
            asteroid = SpriteWithHealth(":resources:images/space_shooter/meteorGrey_big1.png", 0.25, max_health=5)
            asteroid.center_x = random.randrange(800)
            asteroid.center_y = random.randrange(150, 600)
            self.asteroid_list.append(asteroid)
            asteroid.change_x = 0.5

        # Create asteroids
        for i in range(50):
            star = StarSprites(":resources:images/pinball/bumper.png", 0.25)
            star.center_x = random.randrange(800)
            star.center_y = random.randrange(150, 600)
            star.change_x = -0.5
            self.star_list.append(star)

    def on_show(self):

        arcade.set_background_color(arcade.color.STEEL_PINK)
        self.window.set_mouse_visible(False)

    def on_draw(self):

        arcade.start_render()
        self.asteroid_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()
        self.star_list.draw()
        self.supernova_list.draw()
        self.background_star_list.draw()
        arcade.draw_text(f"Score:{self.score}", 10, 20, arcade.color.WHITE, 14)

        # Create health numbers and bars for asteroids
        for asteroid in self.asteroid_list:
            asteroid.draw_health_number()
            asteroid.draw_health_bar()

        # Create health number and bar for player
        for player in self.player_list:
            player.draw_health_number()
            player.draw_health_bar()


    def on_update(self, delta_time):

        self.time_taken += delta_time
        self.bullet_list.update()
        self.asteroid_list.update()
        self.supernova_list.update()
        self.star_list.update()

        # End the game after hitting the player three times
        for supernova in self.supernova_list:
            hit2_list = arcade.check_for_collision_with_list(supernova, self.player_list)

            for player in hit2_list:
                supernova.remove_from_sprite_lists()
                arcade.play_sound(self.death_sound)
                player.current_health -= 1

                if player.current_health <= 0:
                    arcade.play_sound(self.death_sound)
                    game_over_view = GameOverView()
                    game_over_view.score = self.score
                    window.show_view(game_over_view)

        # Remove bullets after impact and meteorites when they lose all health points
        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.asteroid_list)

            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            for asteroid in hit_list:
                arcade.play_sound(self.death_sound)
                asteroid.current_health -= 1
                self.score += 1

                if asteroid.current_health <= 0:
                    asteroid.remove_from_sprite_lists()
                    self.score += 1
                    arcade.play_sound(self.death_sound)
                else:
                    arcade.play_sound(self.death_sound)

        # Remove asteroids after impact
        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.star_list)

            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            for star in hit_list:
                star.remove_from_sprite_lists()
                arcade.play_sound(self.star_sound)
                self.score += 1

        # End the game after 20 seconds
        if round(self.time_taken, 2) > 20.00 :
            game_over_view = HardGameOverView()
            game_over_view.score = self.score
            window.show_view(game_over_view)


    def on_mouse_motion(self, x, y, _dx, _dy):

        #Only move along the x axis
        self.player_sprite.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):

        SPRITE_SCALING_LASER = 0.8
        BULLET_SPEED = 5

        arcade.play_sound(self.gun_sound)
        # Create bullets

        bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_LASER)
        bullet.angle = 90
        bullet.change_y = BULLET_SPEED
        bullet.center_x = self.player_sprite.center_x
        bullet.bottom = self.player_sprite.top
        self.bullet_list.append(bullet)

        supernova = SupernovaSprites(":resources:images/space_shooter/laserRed01.png", 1)
        supernova.center_x = random.randrange(800)
        supernova.center_y = 600
        supernova.angle = 180
        self.supernova_list.append(supernova)
        supernova.change_y = -5

#Game over views

# Game over for easy version
class GameOverView(arcade.View):
    """Create game over view(easy version)"""

    def __init__(self):
        super().__init__()

        self.score = 0
        self.ui_manager = UIManager()

        self.playership_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()

        for i in range(3):
            playership = StarSprites(":resources:images/space_shooter/playerShip1_green.png", 1)
            playership.center_x = random.randrange(800)
            playership.center_y = random.randrange(0, 100)
            playership.change_y = 0.5
            self.playership_list.append(playership)

        for i in range(50):
            star = StarSprites(":resources:images/items/star.png", 0.1)
            star.center_x = random.randrange(800)
            star.center_y = random.randrange(100, 600)
            self.star_list.append(star)

    def setup(self):

        self.ui_manager.purge_ui_elements()
        y_slot = self.window.height // 4
        left_column_x = self.window.width // 4
        right_column_x = 3 * self.window.width // 4

        #Create 'Try Again' and 'Back to menu' buttons
        try_again_button = TryAgainButton(
            'Try again',
            center_x=left_column_x,
            center_y=y_slot * 1,
            width=250
        )
        self.ui_manager.add_ui_element(try_again_button)

        back_to_button = BacktoButton(
            'Back to menu',
            center_x=right_column_x,
            center_y=y_slot * 1,
            width=250
        )
        self.ui_manager.add_ui_element(back_to_button)

        #Enter the result into the archive
        archive = open("result.txt", 'a')
        archive.write(f"{self.score}")
        archive.write('\n')
        archive.close()

    def on_show_view(self):

        self.setup()
        self.window.set_mouse_visible(True)

    def on_hide_view(self):

        self.ui_manager.unregister_handlers()

    def on_show(self):

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):

        arcade.start_render()
        self.playership_list.draw()
        self.star_list.draw()

        WIDTH = 800
        HEIGHT = 600

        arcade.draw_text("Game over", WIDTH / 2, HEIGHT / 2,
                            arcade.color.WHITE, font_size=50, anchor_x="center")

        arcade.draw_text(f"Your score: {self.score}", WIDTH / 2, 400,
                                arcade.color.WHITE, font_size=40, anchor_x="center")

    def on_update(self, delta_time: float):
        self.playership_list.update()


# Game over view for hard version
class HardGameOverView(arcade.View):
    """Create game over view(hard version)"""

    def __init__(self):
        super().__init__()

        self.score = 0
        self.ui_manager = UIManager()
        self.playership_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()

        for i in range(3):
            playership = StarSprites(":resources:images/space_shooter/playerShip1_green.png", 1)
            playership.center_x = random.randrange(800)
            playership.center_y = random.randrange(0, 100)
            playership.change_y = 0.5
            self.playership_list.append(playership)

        for i in range(50):
            star = StarSprites(":resources:images/items/star.png", 0.1)
            star.center_x = random.randrange(800)
            star.center_y = random.randrange(100, 600)
            self.star_list.append(star)

    def setup(self):

        self.ui_manager.purge_ui_elements()
        y_slot = self.window.height // 4
        left_column_x = self.window.width // 4
        right_column_x = 3 * self.window.width // 4

        try_again_button = TryHardAgainButton(
            'Try again',
            center_x=left_column_x,
            center_y=y_slot * 1,
            width=250
        )
        self.ui_manager.add_ui_element(try_again_button)

        back_to_button = BacktoButton(
            'Back to menu',
            center_x=right_column_x,
            center_y=y_slot * 1,
            width=250
        )
        self.ui_manager.add_ui_element(back_to_button)

        #Enter the result into the archive
        archive = open("result.txt", 'a')
        archive.write(f"{self.score}")
        archive.write('\n')
        archive.close()

    def on_show_view(self):

        self.setup()
        self.window.set_mouse_visible(True)
        arcade.set_background_color(arcade.color.GRAPE)

    def on_hide_view(self):

        self.ui_manager.unregister_handlers()

    def on_show(self):

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):

        arcade.start_render()
        self.playership_list.draw()
        self.star_list.draw()

        WIDTH = 800
        HEIGHT = 600

        arcade.draw_text("Game over", WIDTH / 2, HEIGHT / 2,
                            arcade.color.WHITE, font_size=50, anchor_x="center")

        arcade.draw_text(f"Your score: {self.score}", WIDTH / 2, 400,
                                arcade.color.WHITE, font_size=40, anchor_x="center")

    def on_update(self, delta_time: float):
        self.playership_list.update()


# Result View
class BestResultView(arcade.View):
    """Create 'Best Result View' (max 6 results)"""

    def __init__(self):
        super().__init__()

        self.score = []
        self.ui_manager = UIManager()
        self.playership_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()

        for i in range(3):
            playership = StarSprites(":resources:images/space_shooter/playerShip1_green.png", 1)
            playership.center_x = random.randrange(800)
            playership.center_y = random.randrange(0, 100)
            playership.change_y = 0.5
            self.playership_list.append(playership)

        for i in range(50):
            star = StarSprites(":resources:images/items/star.png", 0.1)
            star.center_x = random.randrange(800)
            star.center_y = random.randrange(100, 600)
            self.star_list.append(star)


    def on_draw(self):

        arcade.start_render()
        self.playership_list.draw()
        self.star_list.draw()

        WIDTH = 800
        HEIGHT = 600

        arcade.draw_text("The Best Results", WIDTH / 2, 4 * HEIGHT / 6,
                            arcade.color.YELLOW, font_size=50, anchor_x="center")

        arcade.draw_text("Click to go back", WIDTH / 2, 5 * HEIGHT / 6,
                            arcade.color.WHITE, font_size=20, anchor_x="center")
        try:
            file = open("result.txt", 'r')
        except FileNotFoundError:
            arcade.draw_text("", WIDTH / 2, HEIGHT / 3,
                             arcade.color.WHITE, font_size=30, anchor_x="center")
        else:
            archive = open("result.txt", 'r')
            if archive.readable():
                score = archive.readlines()
                score.sort()
                score.reverse()

                if len(score) <= 6:
                    for i in range(len(score)):
                        arcade.draw_text(f"Score:{score[i]}", WIDTH / 2 , HEIGHT / 2 - 50*i,
                                            arcade.color.WHITE, font_size=20, anchor_x="center")
                else:
                    for i in range(6):
                        arcade.draw_text(f"Score:{score[i]}", WIDTH / 2, HEIGHT / 2 - 50 * i,
                                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_update(self, delta_time: float):

        self.playership_list.update()


    def on_hide_view(self):

        self.ui_manager.unregister_handlers()

    def on_show(self):

        arcade.set_background_color(arcade.color.BLACK)

    def on_mouse_press(self, _x, _y, _button, _modifiers):

        my_view = MyView()

        self.window.show_view(my_view)


# About me view
class AboutMeView(arcade.View):
    """Create 'About me' view"""

    def __init__(self):
        super().__init__()

        self.playership_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()

        for i in range(3):
            playership = StarSprites(":resources:images/space_shooter/playerShip1_green.png", 1)
            playership.center_x = random.randrange(800)
            playership.center_y = random.randrange(0, 100)
            playership.change_y = 0.5
            self.playership_list.append(playership)

        for i in range(50):
            star = StarSprites(":resources:images/items/star.png", 0.1)
            star.center_x = random.randrange(800)
            star.center_y = random.randrange(100, 600)
            self.star_list.append(star)

    def on_show(self):
        arcade.set_background_color(arcade.color.OXFORD_BLUE)

    def on_draw(self):

        arcade.start_render()
        self.playership_list.draw()
        self.star_list.draw()

        WIDTH = 800
        HEIGHT = 600

        arcade.draw_text("About Me Screen", WIDTH/2, HEIGHT/2 + 125,
                         arcade.color.YELLOW, font_size=50, anchor_x="center")

        arcade.draw_text("The author of the game is Anna Zadka.", WIDTH/2, HEIGHT/2,
                         arcade.color.WHITE, font_size=25, anchor_x="center")

        arcade.draw_text("The game was created for the programming class", WIDTH/2, HEIGHT/2-75,
                         arcade.color.WHITE, font_size=25, anchor_x="center")

        arcade.draw_text("in the first year of applied mathematics.", WIDTH/2, HEIGHT/2-150,
                         arcade.color.WHITE, font_size=25, anchor_x="center")

        arcade.draw_text("Click to go back", WIDTH/2, HEIGHT/2+225,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        my_view = MyView()
        self.window.show_view(my_view)

    def on_update(self, delta_time: float):
        self.playership_list.update()

# Instruction View
class InstructionView(arcade.View):
    """Create 'How to play?' view"""

    def __init__(self):
        super().__init__()

        self.playership_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()

        for i in range(3):
            playership = StarSprites(":resources:images/space_shooter/playerShip2_orange.png", 1)
            playership.center_x = random.randrange(800)
            playership.center_y = random.randrange(0, 100)
            playership.change_y = 0.5
            self.playership_list.append(playership)

        for i in range(50):
            star = StarSprites(":resources:images/items/star.png", 0.1)
            star.center_x = random.randrange(800)
            star.center_y = random.randrange(100, 600)
            self.star_list.append(star)

    def on_show(self):
            arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):

        arcade.start_render()
        self.playership_list.draw()
        self.star_list.draw()

        WIDTH = 800
        HEIGHT = 600

        arcade.draw_text("How to play?", WIDTH/2, HEIGHT/2 + 125,
                         arcade.color.WHITE, font_size=50, anchor_x="center")

        arcade.draw_text("Click to go back", WIDTH/2, HEIGHT/2+220,
                         arcade.color.YELLOW, font_size=20, anchor_x="center")

        arcade.draw_text("1. Your goal is to shoot down as many meteorites as possible", WIDTH/2, HEIGHT/2,
                             arcade.color.YELLOW, font_size=20, anchor_x="center")

        arcade.draw_text("2. You start with 3 health points", WIDTH/2, HEIGHT/2 - 75,
                             arcade.color.YELLOW, font_size=20, anchor_x="center")

        arcade.draw_text("3. You play until you lose all health points or to 20 seconds", WIDTH/2, HEIGHT/2 - 150,
                             arcade.color.YELLOW, font_size=20, anchor_x="center")


    def on_mouse_press(self, _x, _y, _button, _modifiers):

        my_view = MyView()
        self.window.show_view(my_view)

    def on_update(self, delta_time: float):

        self.playership_list.update()


if __name__ == '__main__':
    window = arcade.Window(title='ARCADE_GUI')
    window.total_score = 0
    view = MyView()
    window.show_view(view)
    arcade.run()
