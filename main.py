from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
Window.size = (350, 600)


class SplashScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class RegisterScreen(Screen):
    pass


class ForgetPasswordScreen(Screen):
    pass


class Main(MDApp):
    def build(self):
        kv = Builder.load_file("123.kv")
        screen = kv
        return screen


if __name__ == "__main__":
    Main().run()