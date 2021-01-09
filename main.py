import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class MyApp(App):

    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    MyApp().run()

# All logic is done in this file, and all UI design done in my.kv
