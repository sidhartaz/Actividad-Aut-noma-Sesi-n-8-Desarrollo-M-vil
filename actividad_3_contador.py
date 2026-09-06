from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class ContadorApp(App):
    def build(self):
        # Variable para almacenar el estado del contador
        self.contador = 0
        
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)

        # Label que inicialmente muestra el número 0
        self.label_contador = Label(text='0', font_size=60)
        
        # Button que permite incrementar el contador
        btn_incrementar = Button(text='Incrementar', font_size=30)
        btn_incrementar.bind(on_press=self.incrementar)

        layout.add_widget(self.label_contador)
        layout.add_widget(btn_incrementar)

        return layout

    def incrementar(self, instance):
        # Aumentar en 1 el contador y actualizar el Label
        self.contador += 1
        self.label_contador.text = str(self.contador)

if __name__ == '__main__':
    ContadorApp().run()