from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.animation import Animation

# --- EL SECRETO DE LA FLUIDEZ EN ANDROID 16 ---
Window.softinput_mode = 'below_target' 

KV = '''
<Introduccion>:
    canvas.before:
        Color:
            rgba: 0.02, 0.02, 0.05, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        padding: 30
        Label:
            id: mensaje_maestro
            text: "CONECTANDO CON EL ARÚSPICE..."
            markup: True
            halign: 'center'
            font_size: '18sp'
        Button:
            text: "SELLAR PACTO"
            size_hint: None, None
            size: 200, 60
            pos_hint: {'center_x': 0.5}
            on_release: root.manager.current = 'vpn_panel'

<PanelVPN>:
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 0.02, 0.02, 0.08, 1
            Rectangle:
                pos: self.pos
                size: self.size
        
        Label:
            text: "[color=00ffff]NÚCLEO DE RED[/color]"
            markup: True
            size_hint_y: 0.2
            font_size: '22sp'

        # Monitor de datos ligero
        Label:
            id: status_red
            text: "Túnel: [color=ff3333]Inactivo[/color]"
            markup: True
            size_hint_y: 0.3

        # Teclado Virtual Optimizado (No traba la vista)
        GridLayout:
            id: teclado_grid
            cols: 5
            spacing: 5
            padding: 10
            size_hint_y: 0.5
'''

class Introduccion(Screen):
    def on_enter(self):
        # Efecto de escritura para evitar lag al cargar
        self.texto = "[color=00ff00]Maestro:[/color]\\nHelios, el túnel te espera.\\nLa privacidad es tu escudo."
        self.ids.mensaje_maestro.text = ""
        Clock.schedule_once(self.animar_texto, 0.2)

    def animar_texto(self, dt):
        def add_char(interval):
            actual = self.ids.mensaje_maestro.text
            if len(actual) < len(self.texto):
                self.ids.mensaje_maestro.text += self.texto[len(actual)]
            else:
                return False
        Clock.schedule_interval(add_char, 0.04)

class PanelVPN(Screen):
    def on_enter(self):
        # Generar teclas de forma asíncrona para no congelar la UI
        Clock.schedule_once(self.crear_teclado, 0.1)

    def crear_teclado(self, dt):
        self.ids.teclado_grid.clear_widgets()
        teclas = ['ESC', 'UP', 'DEL', 'TAB', 'ENT', 
                  'CTRL', 'A', 'S', 'D', 'F']
        for t in teclas:
            btn = Button(text=t, background_color=(0.1, 0.4, 0.4, 1))
            self.ids.teclado_grid.add_widget(btn)

class CodeQuest(App):
    def build(self):
        Builder.load_string(KV)
        sm = ScreenManager(transition=FadeTransition(duration=0.5))
        sm.add_widget(Introduccion(name='intro'))
        sm.add_widget(PanelVPN(name='vpn_panel'))
        return sm

if __name__ == '__main__':
    CodeQuest().run()
