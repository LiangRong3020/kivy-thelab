from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty


class WidgetsExample(GridLayout):

    count_= 0
    label_text= StringProperty(str(count_))
    def click_button(self):
        self.count_ += 1
        self.label_text= str(self.count_)
        # print('you pressed')

class GridLayoutExample(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols= 2
        for i in range(50):
            b= Button(text= str(i), size_hint_y=None, width=100)
            self.add_widget(b)

class BoxLayoutExample(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation= "vertical"

        for i in range(50):
            b= Button(text= str(i), size_hint= (1, 1), height= "100dp")
            self.add_widget(b)

class MainWidget(Widget):
    def build(self):
        pass



class TheAppLab(App):
    pass



TheAppLab().run()