import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1, 0, 0, 1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]


class LayoutDemo(App):

    def build(self):
        layout = BoxLayout(padding=10, orientation="vertical")
        colors = [red, green, blue, purple]

        for i in range(3):
            h_layout = BoxLayout(padding=20)
            for i in range(5):
                btn = Button(text=f"Button {i+1}",
                             background_color=random.choice(colors))
                h_layout.add_widget(btn)
            layout.add_widget(h_layout)
        return layout


if __name__ == "__main__":
    app = LayoutDemo()
    app.run()