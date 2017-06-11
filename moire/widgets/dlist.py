from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class DescriptiveList(GridLayout):

    def __init__(self, fields, item_width, item_height=25, **kwargs):
        kwargs['pos_hint'] = {'x': 0, 'y': 0}
        kwargs['cols'] = 2
        kwargs['row_force_default'] = True
        kwargs['row_default_height'] = item_height
        super(DescriptiveList, self).__init__(**kwargs)
        self.values = {}
        for field in fields:
            label = Label(text=field + ": ",
                          text_size=(item_width * 0.3, 0), halign='right')
            self.add_widget(label)
            value = Label(text_size=(item_width * 0.7, 0), halign='left')
            self.add_widget(value)
            self.values[field.lower()] = value

    def __setitem__(self, key, value):
        self.values[key].text = str(value)
