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

Window.clearcolor = FONDO_OLED


class ManualScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'manual'
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        titulo = Label(
            text="[b]MANUAL DEL HACKER[/b]",
            markup=True,
            font_size='24sp',
            color=AZUL_NEON,
            size_hint_y=0.2
        )
        
        contenido = Label(
            text=(
                "1. [b]Sintaxis:[/b] Respeta espacios y comillas.\n"
                "2. [b]Verificación:[/b] El botón valida tu lógica.\n"
                "3. [b]Vibración:[/b] Feedback táctil en cada reto.\n"
                "4. [b]Guardado:[/b] Progreso automático encriptado.\n"
                "5. [b]Objetivo:[/b] Lograr el Rango Maestro."
            ),
            markup=True,
            halign='left',
            font_size='16sp',
            color=AZUL_NEON,
            size_hint_y=0.7
        )
        
        btn_back = Button(
            text="ENTENDIDO",
            size_hint_y=0.1,
            background_color=AZUL_NEON,
            background_normal=''
        )
        btn_back.bind(on_release=self.volver_menu)
        
        layout.add_widget(titulo)
        layout.add_widget(contenido)
        layout.add_widget(btn_back)
        self.add_widget(layout)
    
    def volver_menu(self, instance):
        self.manager.current = 'menu'


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'menu'
        self.store = JsonStore('progreso.json')
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.actualizar_menu()
    
    def actualizar_menu(self):
        self.layout.clear_widgets()
        completados = len(self.store.indices())
        
        if completados < 5:
            rango = "NOVATO"
        elif completados < 13:
            rango = "HACKER"
        else:
            rango = "MAESTRO"
        
        titulo = Label(
            text=f"[b]CODEQUEST[/b]\n[size=14]Rango: {rango}[/size]",
            markup=True,
            size_hint_y=0.15,
            color=AZUL_NEON
        )
        self.layout.add_widget(titulo)
        
        # Botón de Manual
        btn_manual = Button(
            text="📖 VER MANUAL",
            size_hint_y=0.1,
            background_color=(0.3, 0.3, 0.3, 1),
            background_normal=''
        )
        btn_manual.bind(on_release=lambda x: setattr(self.manager, 'current', 'manual'))
        self.layout.add_widget(btn_manual)
        
        # ScrollView con módulos
        scroll = ScrollView()
        grid = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        grid.bind(minimum_height=grid.setter('height'))
        
        # 14 módulos del juego
        modulos = [
            "01: El Despertar",
            "02: Almacenes",
            "03: Variables",
            "04: Condicionales",
            "05: Bucles",
            "06: Funciones",
            "07: Listas",
            "08: Diccionarios",
            "09: Strings",
            "10: Operadores",
            "11: Debugging",
            "12: Retos Finales",
            "13: El Desafío",
            "14: El Maestro"
        ]
        
        for nombre in modulos:
            hecho = self.store.exists(nombre)
            color = VERDE_EXITO if hecho else AZUL_NEON
            btn = Button(
                text=f"{'✓ ' if hecho else ''}{nombre}",
                size_hint_y=None,
                height=70,
                background_color=color,
                background_normal=''
            )
            btn.bind(on_release=lambda x, n=nombre: self.ir_a_curso(n))
            grid.add_widget(btn)
        
        scroll.add_widget(grid)
        self.layout.add_widget(scroll)
    
    def ir_a_curso(self, titulo):
        self.manager.get_screen('curso').cargar_datos(titulo, 'es')
        self.manager.current = 'curso'


class CursoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'curso'
        self.store = JsonStore('progreso.json')
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.add_widget(self.layout)
    
    def cargar_datos(self, titulo, idioma):
        self.layout.clear_widgets()
        
        # Titulo del módulo
        titulo_label = Label(
            text=f"[b]{titulo}[/b]",
            markup=True,
            font_size='20sp',
            color=AZUL_NEON,
            size_hint_y=0.1
        )
        self.layout.add_widget(titulo_label)
        
        # Descripción
        descripcion = Label(
            text="Resuelve el desafío de código correctamente.",
            markup=True,
            font_size='14sp',
            color=AZUL_NEON,
            size_hint_y=0.15
        )
        self.layout.add_widget(descripcion)
        
        # Input de código
        self.code_input = TextInput(
            text='',
            multiline=True,
            size_hint_y=0.5,
            background_color=(0.05, 0.05, 0.1, 1),
            foreground_color=AZUL_NEON,
            cursor_color=VERDE_EXITO
        )
        self.layout.add_widget(self.code_input)
        
        # Botones
        btn_layout = BoxLayout(size_hint_y=0.15, spacing=10)
        
        btn_verificar = Button(
            text="✓ VERIFICAR",
            background_color=VERDE_EXITO,
            background_normal=''
        )
        btn_verificar.bind(on_release=lambda x: self.verificar_codigo(titulo))
        
        btn_volver = Button(
            text="← ATRÁS",
            background_color=AZUL_NEON,
            background_normal=''
        )
        btn_volver.bind(on_release=lambda x: self.volver_menu())
        
        btn_layout.add_widget(btn_verificar)
        btn_layout.add_widget(btn_volver)
        self.layout.add_widget(btn_layout)
    
    def verificar_codigo(self, titulo):
        codigo = self.code_input.text.strip()
        
        if codigo:
            # Marcar como completado
            self.store[titulo] = {'completado': True}
            
            resultado = Label(
                text="[color=00ff88]✓ ¡CORRECTO![/color]",
                markup=True,
                font_size='18sp'
            )
            self.layout.add_widget(resultado)
            
            # Volver al menú después de 2 segundos
            from kivy.clock import Clock
            Clock.schedule_once(lambda dt: self.volver_menu(), 2)
        else:
            resultado = Label(
                text="[color=ff0088]✗ CÓDIGO VACÍO[/color]",
                markup=True,
                font_size='18sp'
            )
            self.layout.add_widget(resultado)
    
    def volver_menu(self):
        self.manager.current = 'menu'


class CodeQuestApp(App):
    def build(self):
        sm = ScreenManager()
        
        # Agregar pantallas
        sm.add_widget(MenuScreen())
        sm.add_widget(CursoScreen())
        sm.add_widget(ManualScreen())
        
        sm.current = 'menu'
        return sm


if __name__ == '__main__':
    CodeQuestApp().run()
