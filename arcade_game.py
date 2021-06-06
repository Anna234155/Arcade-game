import arcade
from arcade.gui import UIManager
import arcade.gui


class MyGame(arcade.View):
    def __init__(self):
        super().__init__()

        self.ui_manager = UIManager()


    def on_show_view(self):
        self.setup()
        arcade.set_background_color(arcade.color.BLACK)


    def setup(self):
        self.ui_manager.purge_ui_elements()

        y_slot = self.window.height // 4
        left_column_x = self.window.width // 4
        right_column_x = 3 * self.window.width // 4

        button_normal = arcade.load_texture(':resources:gui_basic_assets/red_button_normal.png')
        hovered_texture = arcade.load_texture(':resources:gui_basic_assets/red_button_hover.png')
        pressed_texture = arcade.load_texture(':resources:gui_basic_assets/red_button_press.png')

        start_button = arcade.gui.UIImageButton(
            center_x=self.window.width // 2,
            center_y=y_slot * 3,
            normal_texture=button_normal,
            hover_texture=hovered_texture,
            press_texture=pressed_texture,
            text='START'
        )
        self.ui_manager.add_ui_element(start_button)


        how_button = arcade.gui.UIImageButton(
            center_x=left_column_x,
            center_y=y_slot * 2,
            normal_texture=button_normal,
            hover_texture=hovered_texture,
            press_texture=pressed_texture,
            text='How to play?'
        )
        self.ui_manager.add_ui_element(how_button)


        abt_button = arcade.gui.UIImageButton(
            center_x=left_column_x,
            center_y=y_slot * 1,
            normal_texture=button_normal,
            hover_texture=hovered_texture,
            press_texture=pressed_texture,
            text='About the author'
        )
        self.ui_manager.add_ui_element(abt_button)

        close_button = arcade.gui.UIImageButton(
            center_x=right_column_x,
            center_y=y_slot * 1,
            normal_texture=button_normal,
            hover_texture=hovered_texture,
            press_texture=pressed_texture,
            text='Close'
        )

        self.ui_manager.add_ui_element(close_button)


        result_button = arcade.gui.UIImageButton(
            center_x=right_column_x,
            center_y=y_slot * 2,
            normal_texture=button_normal,
            hover_texture=hovered_texture,
            press_texture=pressed_texture,
            text='The best results'
        )
        self.ui_manager.add_ui_element(result_button)



if __name__ == '__main__':
    window = arcade.Window(title='ARCADE_GUI')
    view = MyGame()
    window.show_view(view)
    arcade.run()
