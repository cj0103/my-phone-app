# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.label = Label(text='欢迎使用我的App！', font_size=20)
        self.input = TextInput(hint_text='请输入内容...', multiline=False, size_hint_y=None, height=40)
        button = Button(text='点击显示', size_hint_y=None, height=50)
        button.bind(on_press=self.on_click)
        
        layout.add_widget(self.label)
        layout.add_widget(self.input)
        layout.add_widget(button)
        
        return layout

    def on_click(self, instance):
        self.label.text = f'你输入了：{self.input.text}'

MainApp().run()