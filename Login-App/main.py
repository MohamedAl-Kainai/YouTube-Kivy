from app.modules import *
from kivymd.app import MDApp

from app.screens.login import Login

for i in os.listdir('./app/kv'):
    if i.endswith('.kv'):
        Builder.load_file('app/kv/'+i)

class LoginApp(MDApp):
    def __init__(self, *args, **kwargs):
        self.theme_cls.primary_palette = 'Teal'

        self.theme_cls.primary_dark_hue  = '800'
        self.theme_cls.primary_light_hue = '600'
        self.theme_cls.primary_hue       = '400'

        self.theme_cls.theme_style = 'Light'

        super().__init__(*args, **kwargs)

        colors = [
                    'Red', 'Pink', 'Purple',
                    'DeepPurple', 'Indigo',
                    'Blue', 'LightBlue',
                    'Cyan', 'Teal', 'Green',
                    'LightGreen', 'Lime',
                    'Yellow', 'Amber',
                    'Orange', 'DeepOrange',
                    'Brown', 'Gray', 'BlueGray'
                    ]

        menu_items = [{'icon': 'git', 'text': f'{i}'} for i in colors]
        self.color = MDDropdownMenu(
                    caller=Login().ids.ColorButton,
                    items=menu_items,
                    width_mult=4,
                    callback=self.color_callback
                )

    def color_callback(self, instance):
        self.theme_cls.primary_palette = instance.text

    def build(self):
        return Login()

if __name__=='__main__':
    LoginApp().run()
