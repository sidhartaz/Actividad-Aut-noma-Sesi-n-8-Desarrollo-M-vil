from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)

        # 1. Label para identificar la interfaz (con color de texto personalizado)
        titulo = Label(text='[b]INICIO DE SESIÓN[/b]', markup=True, color=(0, 0.8, 1, 1)) 
        
        # 2. TextInput para ingresar el usuario
        self.user = TextInput(hint_text='Usuario', multiline=False, background_color=(0.9, 0.9, 0.9, 1))
        
        # 3. TextInput para ingresar la contraseña
        self.pwd = TextInput(hint_text='Contraseña', password=True, multiline=False, background_color=(0.9, 0.9, 0.9, 1))

        # 4. Button para realizar la acción de ingreso (con color de fondo personalizado)
        btn = Button(text='Ingresar', background_color=(0, 0.5, 0.8, 1))
        btn.bind(on_press=self.verificar) 

        # Agregar los widgets al layout
        layout.add_widget(titulo)
        layout.add_widget(self.user)
        layout.add_widget(self.pwd)
        layout.add_widget(btn)

        return layout

    def verificar(self, instance):
        # Imprime en la consola el usuario ingresado
        print(f"Usuario ingresado: {self.user.text}")

if __name__ == '__main__':
    LoginApp().run()