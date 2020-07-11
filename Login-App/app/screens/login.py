from app.modules import *

DATABASES = {
    # user     # password
    'mohamed':'12345678',

}

class Login(MDFloatLayout):

    def check_data(self):
        username = self.ids.username
        password = self.ids.password
        try :
            if DATABASES[username.text] == password.text:
                return True
            else:
                return False
        except KeyError: return False

    def welcome(self):
        if self.check_data():
            toast('welcome '+self.ids.username.text)
