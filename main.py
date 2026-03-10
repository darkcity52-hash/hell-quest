from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window

# Configuración de color de fondo
Window.clearcolor = (1, 1, 1, 1)

class PantallaSeleccion(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        # Imagen de fondo: splash.png 
        self.bg = Image(
            source='assets/icons/splash.png', 
            allow_stretch=True,
            keep_ratio=True
        )
        layout.add_widget(self.bg)

        # Botones invisibles posicionados por coordenadas relativas
        # Centro (Helios)
        self.add_widget(Button(size_hint=(.3, .3), pos_hint={'center_x': .5, 'center_y': .55},
                               background_color=(0,0,0,0), on_press=lambda x: self.log("Helios")))
        # Arriba (Fabio)
        self.add_widget(Button(size_hint=(.22, .22), pos_hint={'center_x': .5, 'center_y': .85},
                               background_color=(0,0,0,0), on_press=lambda x: self.log("Fabio")))
        # Izquierda (Nahomy)
        self.add_widget(Button(size_hint=(.22, .22), pos_hint={'center_x': .15, 'center_y': .5},
                               background_color=(0,0,0,0), on_press=lambda x: self.log("Nahomy")))
        # Derecha (Nora)
        self.add_widget(Button(size_hint=(.22, .22), pos_hint={'center_x': .85, 'center_y': .5},
                               background_color=(0,0,0,0), on_press=lambda x: self.log("Usuario 4")))

        self.add_widget(layout)

    def log(self, nombre):
        print(f"Perfil activo: {nombre}")

class CodeQuestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(PantallaSeleccion(name='seleccion'))
        return sm

if __name__ == '__main__':
    CodeQuestApp().run()
