from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window
from kivy.clock import Clock

# Configuración de fluidez para Android 16
Window.softinput_mode = 'below_target'

# Diseño visual con lenguaje de "Misión"
KV = '''
<Introduccion>:
    canvas.before:
        Color:
            rgba: 0.05, 0.05, 0.1, 1  # Fondo Espacio Profundo
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        padding: 40
        spacing: 20
        Label:
            id: texto_maestro
            text: ""
            markup: True
            font_size: '20sp'
            halign: 'center'
        Button:
            text: "ACEPTAR MISIÓN"
            size_hint: None, None
            size: 250, 60
            pos_hint: {'center_x': 0.5}
            opacity: 0
            id: btn_inicio
            on_release: root.manager.current = 'vpn_panel'

<PanelVPN>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: "[color=00ffff]Santuario de Red[/color]\\n[size=15]Nivel: Iniciado[/size]"
            markup: True
            size_hint_y: 0.2
        
        # Representación del Túnel
        BoxLayout:
            id: area_tunel
            size_hint_y: 0.4
            Label:
                text: "ESTADO: [color=ff3333]PROTECCIÓN DESACTIVADA[/color]"
                markup: True

        # El Teclado de PC Virtual (Base)
        GridLayout:
            cols: 10
            size_hint_y: 0.4
            padding: 2
            spacing: 2
            id: teclado_pc
'''

class Introduccion(Screen):
    def on_enter(self):
        self.mensaje_inicial = (
            "[color=00ff00]Arúspice de Silicio:[/color]\\n"
            "Helios... Las murallas de Android 16 son altas,\\n"
            "pero tu código es la llave.\\n\\n"
            "[i]Tu primera reliquia te espera en la nube.[/i]"
        )
        Clock.schedule_once(self.escribir_texto, 0.5)

    def escribir_texto(self, dt):
        # Animación de máquina de escribir para la historia
        def actualizar_label(interval):
            actual = self.ids.texto_maestro.text
            if len(actual) < len(self.mensaje_inicial):
                self.ids.texto_maestro.text += self.mensaje_inicial[len(actual)]
            else:
                self.ids.btn_inicio.opacity = 1
                return False
        Clock.schedule_interval(actualizar_label, 0.05)

class PanelVPN(Screen):
    def on_enter(self):
        # Aquí generamos las teclas dinámicamente para no saturar el KV
        teclas = ['Esc', '1', '2', '3', '4', 'Del', 'Tab', 'Q', 'W', 'E', 
                  'Ctrl', 'A', 'S', 'D', 'F', 'Ent', 'Shift', 'Z', 'X', 'C']
        for t in teclas:
            self.ids.teclado_pc.add_widget(Button(text=t, font_size='12sp'))

class CodeQuest(App):
    def build(self):
        Builder.load_string(KV)
        sm = ScreenManager(transition=FadeTransition(duration=0.8))
        sm.add_widget(Introduccion(name='intro'))
        sm.add_widget(PanelVPN(name='vpn_panel'))
        return sm

if __name__ == '__main__':
    CodeQuest().run()
