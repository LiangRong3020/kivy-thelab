from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.graphics.vertex_instructions import Line
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.metrics import dp


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

class canvasExample1(Widget):
    pass

class canvasExample2(Widget):
    pass

class canvasExample3(Widget):
    pass

class canvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count_= 0
        with self.canvas:
            Line(points= (100, 100, 400, 500), width= 2)
            Color(0, 1, 0)
            Line(circle= (400, 200, 80), width= 2)

            Line(rectangle=(700, 200, 150, 100), width=2)
            self.rect= Rectangle(pos=(700, 500), size=(150, 100))

    def on_press_a_click(self):
        x, y= self.rect.pos
        w, h= self.rect.size
        inc = dp(10)
        x =  x + inc if x + inc+ w <= self.width else self.width-w

        self.rect.pos= (x, y)

        # self.label_text= str(self.count_)

class canvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size= dp(50)
        self.vx = 3
        self.vy = 4
        with self.canvas:
            self.ball = Ellipse(pos= self.center, size= (self.ball_size, self.ball_size))

        Clock.schedule_interval(self.update, 1/60)

    def on_size(self, *args):
        # print('width: ', self.width, ' height: ', self.height)
        self.ball.pos= (self.center_x- self.ball_size/2, self.center_y- self.ball_size/2)

    def update(self, dt):

        x, y= self.ball.pos

        x += self.vx
        y += self.vy

        if y + self.ball_size >= self.height:
            y= self.height-self.ball_size
            self.vy *= -1
        elif y <= 0:
            y = 0
            self.vy *= -1


        if x + self.ball_size >= self.width:
            x = self.width - self.ball_size
            self.vx *= -1
        elif x <= 0:
            x = 0
            self.vx *= -1


        self.ball.pos= (x, y)

class TheAppLab(App):
    pass



TheAppLab().run()