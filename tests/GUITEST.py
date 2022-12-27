import kivy
import random
 
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
 

blue = '#d9f5ff'
grey = '#595959'


class HBoxLayoutExample(App):
    def build(self):
        

        layout = BoxLayout(padding=10)

        lenta = Button(text="Lenta",
                             background_color=grey)
        layout.add_widget(lenta)

        for i in range(4):
            btn = Button(text="Button #%s" % (i+1),
                         background_color=blue
                         )
 
            layout.add_widget(btn)
         
        return layout
 
if __name__ == "__main__":
    app = HBoxLayoutExample()
    app.run()