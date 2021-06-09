import arcade

class SpriteWithHealth(arcade.Sprite):
    """Create sprites with health points"""

    def __init__(self, image, scale, max_health):
        super().__init__(image, scale)

        self.max_health = max_health
        self.current_health = max_health

    def draw_health_number(self):
        """Draw the health points"""

        health_string = f"{self.current_health}/{self.max_health}"
        arcade.draw_text(health_string,
                         start_x=self.center_x -10,
                         start_y=self.center_y -25,
                         font_size=12,
                         color=arcade.color.WHITE)

        health_width = 25 * (self.current_health / self.max_health)

        arcade.draw_rectangle_filled(center_x=self.center_x - 0.5 * (25 - health_width),
                                     center_y=self.center_y - 10,
                                     width=health_width,
                                     height=3,
                                     color=arcade.color.GREEN)
    def draw_health_bar(self):
        """Draw the health bar"""

        if self.current_health < self.max_health:
            arcade.draw_rectangle_filled(center_x=self.center_x,
                                         center_y=self.center_y -10,
                                         width=25,
                                         height=3,
                                         color=arcade.color.RED)

        health_width = 25 * (self.current_health / self.max_health)

        arcade.draw_rectangle_filled(center_x=self.center_x - 0.5 * (25 - health_width),
                                     center_y=self.center_y - 10,
                                     width=health_width,
                                     height=3,
                                     color=arcade.color.GREEN)


class PlayerSprite(arcade.Sprite):
    """Create player with health points"""

    def __init__(self, image, scale, max_health):
        super().__init__(image, scale)


        self.max_health = max_health
        self.current_health = max_health

    def draw_health_number(self):
        """Draw the health points"""

        health_string = f"{self.current_health}/{self.max_health}"
        arcade.draw_text(health_string,
                         start_x=727.5,
                         start_y=50,
                         font_size=25,
                         color=arcade.color.WHITE)


    def draw_health_bar(self):
        """Draw the health bar"""


        if self.current_health < self.max_health:
            arcade.draw_rectangle_filled(center_x=750,
                                         center_y=self.center_y -10,
                                         width=60,
                                         height=10,
                                         color=arcade.color.RED)

        health_width = 60 * (self.current_health / self.max_health)

        arcade.draw_rectangle_filled(center_x=750 - 0.5 * (60 - health_width),
                                     center_y=self.center_y - 10,
                                     width=health_width,
                                     height=10,
                                     color=arcade.color.GREEN)