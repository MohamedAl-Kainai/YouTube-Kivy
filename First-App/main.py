from kivymd.app import MDApp
from kivy.lang import Builder

root_kv = '''
FloatLayout:
    MDFillRoundFlatButton:
        text:'login'
        pos_hint:{'center_x':.5,'center_y':.5}
'''
class MyApp(MDApp):
    def build(self):
        self.root = Builder.load_string(root_kv)

MyApp().run()
