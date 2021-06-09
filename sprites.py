import arcade.gui


class BackgroundSprites(arcade.Sprite):
    """Create backgrounds stars"""
    def __init__(self, image, scale):
        super().__init__(image, scale)

class AsteroidSprites(arcade.Sprite):
    """Create meteors"""
    def __init__(self, image, scale):
        super().__init__(image, scale)

class SupernovaSprites(arcade.Sprite):
    """Create asteroids"""
    def __init__(self, image, scale):
        super().__init__(image, scale)


class StarSprites(arcade.Sprite):
    """Create stars"""
    def __init__(self, image, scale):
        super().__init__(image, scale)