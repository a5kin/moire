from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class DescriptiveList(GridLayout):

    def __init__(self, fields, item_width, item_height=25, **kwargs):
        kwargs['pos_hint'] = {'x': 0, 'y': 0}
        kwargs['cols'] = 2
        kwargs['row_force_default'] = True
        kwargs['row_default_height'] = item_height
        kwargs['padding'] = (5, 5)
        super(DescriptiveList, self).__init__(**kwargs)
        self.values = {}
        for field in fields:
            label = Label(text=field + ":", font_name="Xolonium Bold",
                          text_size=(item_width * 0.4, 0), halign='right',
                          padding=(5, 0), font_size=item_height, max_lines=1)
            self.add_widget(label)
            value = Label(font_name="Xolonium Regular",
                          text_size=(item_width * 0.6, 0), halign='left',
                          padding=(5, 0), font_size=item_height, max_lines=1)
            self.add_widget(value)
            self.values[field.lower()] = value

    def __setitem__(self, key, value):
        self.values[key].text = str(value)
