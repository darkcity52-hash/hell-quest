from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivy.utils import platform, get_color_from_hex

# Estética Cyberpunk OLED
AZUL_NEON = get_color_from_hex('#0088ff')
VERDE_EXITO = get_color_from_hex('#00ff88')
FONDO_OLED = get_color_from_hex('#020205')

# Datos de los retos (Versión resumida para estabilidad)
LECCIONES_DATA = {
    'es': {
        '01: El Despertar': {'texto': "Usa [color=00ff88]print('Hola Mundo')[/color]", 'reto': "print('Hola Mundo')", 'err': "Error en comillas o paréntesis."},
        '02: Almacenes': {'texto': "Crea una variable [color=00ff88]x = 10[/color]", 'reto': "x = 10", 'err': "Escribe: x = 10"},
        '03: El Camino IF': {'texto': "Escribe: [color=00ff88]if 5 > 3:[/color]", 'reto': "if 5 > 3:", 'err': "Olvidas los ':' al final."},
        '14: El Maestro': {'texto': "Escribe [color=00ff88]soy hacker[/color] para terminar.", 'reto': "soy hacker", 'err': "Escribe 'soy hacker'"}
    }
}

class ManualScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        layout.add_widget(Label(text="[b]MANUAL DEL HACKER[/b]", markup=True, font_size='24sp', color=AZUL_NEON, size_hint_y=0.2))
        layout.add_widget(Label(text="1. Respeta espacios.\n2. Pulsa Verificar.\n3. Logra el Rango Maestro.", markup=True, halign='center'))
        btn_back = Button(text="ENTENDIDO", size_hint_y=0.15, background_color=AZUL_NEON, background_normal='')
        btn_back.bind(on_release=lambda x: setattr(self.manager, 'current', 'menu'))
        layout.add_widget(btn_back)
        self.add_widget(layout)

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.store = JsonStore('progreso.json')
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.actualizar_menu()

    def actualizar_menu(self):
        self.layout.clear_widgets()
        completados = len(self.store.indices())
        rango = "NOVATO" if completados < 3 else "HACKER"
        self.layout.add_widget(Label(text=f"[b]CODEQUEST[/b]\n[size=14]Rango: {rango}[/size]", markup=True, size_hint_y=0.15, color=AZUL_NEON))
        
        btn_manual = Button(text="📖 VER MANUAL", size_hint_y=0.1, background_color=(0.3, 0.3, 0.3, 1), background_normal='')
        btn_manual.bind(on_release=lambda x: setattr(self.manager, 'current', 'manual'))
        self.layout.add_widget(btn_manual)

        scroll = ScrollView()
        grid = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        grid.bind(minimum_height=grid.setter('height'))

        for nombre in LECCIONES_DATA['es'].keys():
            hecho = self.store.exists(nombre)
            btn = Button(text=f"{'✓ ' if hecho else ''}{nombre}", size_hint_y=None, height=70, background_color=(VERDE_EXITO if hecho else AZUL_NEON), background_normal='')
            btn.bind(on_release=lambda x, n=nombre: self.ir_a_curso(n))
            grid.add_widget(btn)

        scroll.add_widget(grid)
        self.layout.add_widget(scroll)
        self.add_widget(self.layout)

    def ir_a_curso(self, titulo):
        self.manager.get_screen('curso').cargar_datos(titulo, 'es')
        self.manager.current = 'curso'

class CursoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        self.ids['lbl_titulo'] = Label(text="", font_size='22sp', size_hint_y=0.1, color=AZUL_NEON)
        self.ids['lbl_cont'] = Label(text="", markup=True, halign='center', size_hint_y=0.2)
        self.ids['codigo_input'] = TextInput(hint_text='Escribe código...', background_color=(0.1, 0.1, 0.1, 1), foreground_color=(0, 1, 0, 1), size_hint_y=0.4)
        
        btn_validar = Button(text="VERIFICAR", size_hint_y=0.15, background_color=AZUL_NEON, background_normal='')
        btn_validar.bind(on_release=lambda x: self.verificar())
        
        btn_back = Button(text="VOLVER", size_hint_y=0.1, background_color=(0.2, 0.2, 0.2, 1))
        btn_back.bind(on_release=lambda x: setattr(self.manager, 'current', 'menu'))
        
        for w in [self.ids.lbl_titulo, self.ids.lbl_cont, self.ids.codigo_input, btn_validar, btn_back]: self.layout.add_widget(w)
        self.add_widget(self.layout)

    def cargar_datos(self, titulo, lang):
        self.titulo_actual = titulo
        self.ids.lbl_titulo.text = titulo
        self.ids.lbl_cont.text = LECCIONES_DATA[lang][titulo]['texto']
        self.ids.codigo_input.text = ""

    def verificar(self):
        codigo = self.ids.codigo_input.text.strip()
        meta = LECCIONES_DATA['es'][self.titulo_actual]
        if meta['reto'].lower() in codigo.lower():
            self.ids.lbl_cont.text = "[color=00ff88]¡LOGRADO![/color]"
            JsonStore('progreso.json').put(self.titulo_actual, done=True)
            self.manager.get_screen('menu').actualizar_menu()
        else:
            self.ids.lbl_cont.text = f"[color=ff4444]{meta['err']}[/color]"

class CodeQuestApp(App):
    def build(self):
        Window.clearcolor = FONDO_OLED
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(ManualScreen(name='manual'))
        sm.add_widget(CursoScreen(name='curso'))
        return sm

if __name__ == '__main__':
    CodeQuestApp().run()
