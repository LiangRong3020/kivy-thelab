from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty


class WidgetsExample(GridLayout):

    count_= 0
    label_text= StringProperty(str(count_))
    widget_state= BooleanProperty(False)

    # slder
    slider_state = BooleanProperty(False)
    slider_text = StringProperty(str(50))

    # text input
    text_input_string= StringProperty()

    def click_button(self):
        if self.widget_state:
            self.count_ += 1
            self.label_text= str(self.count_)
        # print('you pressed')

    def on_toggle_button_state(self, widget):

        if widget.state == 'normal':
            self.widget_state = False
            widget.text = 'OFF'
        else:
            self.widget_state = True
            widget.text = 'ON'

    # def on_switch_active(self, widget):
    #     if widget.active:
    #         self.slider_state = True
    #     else:
    #         self.slider_state = False

    # def on_slider_value(self, widget):
    #     self.slider_text= str(round(widget.value, 2))

    def on_text_validate(self, widget):
        self.text_input_string= widget.text

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