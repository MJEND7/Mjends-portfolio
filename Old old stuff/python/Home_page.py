from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.button import MDFloatingActionButton, MDFlatButton, MDIconButton
from kivy.lang import Builder


navigation_helper = """
Screen:

    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        right_action_items: [["dots-vertical", lambda x: app.callback_1()], ["clock", lambda x: app.callback_2()]]
                        title: "Navigation Drawer"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            MDRectangleFlatIconButton:
                pos_hint: {"center_x": 1.0, "center_y": 0.97}
                icon: "home"
                elevation_normal: 18
                text: "Back To Home"
        
"""


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen


DemoApp().run()