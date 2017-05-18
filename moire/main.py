from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock


class MainEngine(Widget):

    def update(self, dt):
        pass


class GUI(App):

    def __init__(self, **kwargs):
        if 'runnable' in kwargs:
            self.runnable = kwargs['runnable']
            del kwargs['runnable']
        super(GUI, self).__init__(**kwargs)
    
    def build(self):
        engine = MainEngine()
        Clock.schedule_interval(MainEngine.update, 1.0 / 25.0)
        return engine
