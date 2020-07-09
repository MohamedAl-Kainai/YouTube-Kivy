from kivymd.app import MDApp
from kivymd.toast import toast

DATABASES = {
    # user    # password
    'mohamed':'12345678',
    'ali':'123@ali',
}

class LoginApp(MDApp):
    def __init__(self, *args, **kwargs):
        self.theme_cls.primary_palette = 'Gray'
        self.theme_cls.primary_hue = '600'
        self.theme_cls.theme_style = 'Dark'
        super().__init__(*args, **kwargs)

    def login_button(self, user, password, instance):
        try:
            if DATABASES[user] == password:
                toast('Done')
        except:toast('not found!')

if __name__=='__main__':
    LoginApp().run()
