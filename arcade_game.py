import arcade


import arcade.gui
from arcade.gui import UIManager


class MyFlatButton(arcade.gui.UIFlatButton):

    def on_click(self):
        """ Called when user lets off button """
        print(f"")

class MyFlatResultButton(arcade.gui.UIFlatButton):

    def on_click(self):
        """ Called when user lets off button """
        best_result_view = BestResultView()
        window.show_view(best_result_view)


class BestResultView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        arcade.start_render()

        WIDTH = 800
        HEIGHT = 600

        arcade.draw_text("The Best Results Screen", WIDTH/2, HEIGHT/2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

        arcade.draw_text("Click to go back", WIDTH/2, HEIGHT/2-75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        my_view = MyView()
        self.window.show_view(my_view)


class MyFlatAbtButton(arcade.gui.UIFlatButton):

    def on_click(self):
        """ Called when user lets off button """
        about_me_view = AboutMeView()
        window.show_view(about_me_view)


class AboutMeView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        arcade.start_render()

        WIDTH = 800
        HEIGHT = 600

        arcade.draw_text("About Me Screen", WIDTH/2, HEIGHT/2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

        arcade.draw_text("Click to go back", WIDTH/2, HEIGHT/2-75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        my_view = MyView()
        self.window.show_view(my_view)


class MyFlatHowButton(arcade.gui.UIFlatButton):

    def on_click(self):
        """ Called when user lets off button """
        instructions_view = InstructionView()
        window.show_view(instructions_view)

class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        arcade.start_render()

        WIDTH = 800
        HEIGHT = 600

        arcade.draw_text("Instructions Screen", WIDTH/2, HEIGHT/2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

        arcade.draw_text("Click to go back", WIDTH/2, HEIGHT/2-75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        my_view = MyView()
        self.window.show_view(my_view)

class MyFlatCloseButton(arcade.gui.UIFlatButton):

    def on_click(self):
        """ Called when user lets off button """
        window.close()


class MyView(arcade.View):
    """
    Main view. Really the only view in this example. """
    def __init__(self):
        super().__init__()

        self.ui_manager = UIManager()

    def on_draw(self):
        """ Draw this view. GUI elements are automatically drawn. """
        arcade.start_render()

    def on_show_view(self):
        """ Called once when view is activated. """
        self.setup()
        arcade.set_background_color(arcade.color.GRAPE)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def setup(self):
        """ Set up this view. """
        self.ui_manager.purge_ui_elements()

        y_slot = self.window.height // 4
        left_column_x = self.window.width // 4
        right_column_x = 3 * self.window.width // 4

        start_button = MyFlatButton(
            'Start',
            center_x=self.window.width // 2,
            center_y=y_slot * 3,
            width=250,
            # height=20
        )
        self.ui_manager.add_ui_element(start_button)

        result_button = MyFlatResultButton(
            'Best results',
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
            width=250,
            # height=20
        )
        self.ui_manager.add_ui_element(how_button)


        author_button = MyFlatHowButton(
            'How to play?',
            center_x=right_column_x,
            center_y=y_slot * 2,
            width=250,
            # height=20
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

if __name__ == '__main__':
    window = arcade.Window(title='ARCADE_GUI')
    view = MyView()
    window.show_view(view)
    arcade.run()
