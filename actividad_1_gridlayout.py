from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class GridLayoutApp(App):
    def build(self):
        # Utilizar un GridLayout con cols=2
        layout = GridLayout(cols=2)

        # Incorporar un Label que funcione como título y ocupe una celda
        layout.add_widget(Label(text='Menú Principal'))

        # Incorporar 3 Button
        btn1 = Button(text='Opción A')
        btn1.bind(on_press=self.accion_a)

        btn2 = Button(text='Opción B')
        btn2.bind(on_press=self.accion_b)

        btn3 = Button(text='Opción C')
        btn3.bind(on_press=self.accion_c)

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)

        return layout

    # Acciones diferenciadas en la consola
    def accion_a(self, instance):
        print("Ejecutando la acción A...")

    def accion_b(self, instance):
        print("Ejecutando la acción B...")

    def accion_c(self, instance):
        print("Ejecutando la acción C...")

if __name__ == '__main__':
    GridLayoutApp().run()