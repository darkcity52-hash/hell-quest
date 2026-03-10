from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.clock import Clock # CORRECCIÓN: Importación correcta al inicio
from kivy.graphics import Color, Rectangle

# Configuración
Window.clearcolor = (0.05, 0.05, 0.07, 1)

# --- BASE DE DATOS DE DESAFÍOS ---
DESAFIOS = [
    {
        "titulo": "Puerta del Bucle",
        "descripcion": "El muro requiere un bucle infinito.",
        "codigo_incorrecto": "while False:",
        "solucion": "while True:",
    },
    {
        "titulo": "Muro de la Variable",
        "descripcion": "Define 'poder' igual a 100.",
        "codigo_incorrecto": "poder = 'cien'",
        "solucion": "poder = 100",
    }
]

# --- PANTALLA DE SELECCIÓN ---
class PantallaSeleccion(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        # Intentamos cargar la imagen, si falla, seguimos sin ella
        try:
            self.bg = Image(source='assets/icons/splash.png', allow_stretch=True, keep_ratio=False)
            layout.add_widget(self.bg)
        except:
            print("No se encontró imagen de fondo, usando color solido.")

        title_label = Label(
            text="[b]HELL QUEST[/b]\nSelecciona tu Guerrero",
            markup=True,
            font_size='24sp',
            color=(1, 0.3, 0.3, 1),
            size_hint=(1, .1),
            pos_hint={'top': 1}
        )
        layout.add_widget(title_label)

        personajes = [
            ("Helios", 0.5, 0.65), ("Fabio", 0.5, 0.45),
            ("Nahomy", 0.25, 0.55), ("Nora", 0.75, 0.55)
        ]

        for nombre, x, y in personajes:
            btn = Button(
                text=nombre,
                size_hint=(.3, .1),
                pos_hint={'center_x': x, 'center_y': y},
                background_color=(0.8, 0.2, 0.2, 0.7),
                color=(1, 1, 1, 1)
            )
            btn.bind(on_press=lambda instance, n=nombre: self.seleccionar_personaje(n))
            layout.add_widget(btn)

        self.add_widget(layout)

    def seleccionar_personaje(self, nombre):
        App.get_running_app().personaje_actual = nombre
        self.manager.current = 'juego'

# --- PANTALLA DEL JUEGO (SEGURA) ---
class PantallaJuego(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nivel_actual = 0
        self.layout_principal = FloatLayout()
        self.add_widget(self.layout_principal)

    def on_enter(self):
        # Intentamos cargar el nivel. Si falla, mostramos el error.
        try:
            self.cargar_nivel(self.nivel_actual)
        except Exception as e:
            self.layout_principal.clear_widgets()
            error_label = Label(
                text=f"Error al cargar nivel:\n{str(e)}",
                color=(1, 0, 0, 1),
                font_size='16sp'
            )
            self.layout_principal.add_widget(error_label)
            print(f"ERROR: {e}")

    def cargar_nivel(self, indice):
        self.layout_principal.clear_widgets()
        
        if indice >= len(DESAFIOS):
            self.mostrar_victoria()
            return

        desafio = DESAFIOS[indice]
        
        ui_box = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Título
        titulo = Label(
            text=f"[b]{desafio['titulo']}[/b]",
            markup=True,
            font_size='28sp',
            size_hint=(1, .15),
            color=(0.9, 0.5, 0.1, 1)
        )
        ui_box.add_widget(titulo)

        # Descripción
        desc = Label(
            text=desafio['descripcion'],
            font_size='18sp',
            size_hint=(1, .1),
            color=(1, 1, 1, 1)
        )
        ui_box.add_widget(desc)

        # El Muro (Contenedor)
        muro_container = BoxLayout(size_hint=(1, .3))
        # Dibujamos fondo negro manualmente
        with muro_container.canvas.before:
            Color(0.1, 0.1, 0.1, 1) # Gris oscuro
            self.rect = Rectangle(size=muro_container.size, pos=muro_container.pos)
        
        # Actualizamos el rectángulo cuando el contenedor cambie
        muro_container.bind(size=self._update_rect, pos=self._update_rect)
        
        self.codigo_muro_label = Label(
            text=desafio['codigo_incorrecto'],
            font_name='Roboto', # CAMBIO: Usamos fuente segura 'Roboto'
            font_size='22sp',
            color=(1, 0, 0, 1)
        )
        muro_container.add_widget(self.codigo_muro_label)
        ui_box.add_widget(muro_container)

        # Entrada
        self.input_codigo = TextInput(
            hint_text="Escribe la línea correcta...",
            multiline=False,
            font_size='20sp',
            size_hint=(1, .1),
            background_color=(0.9, 0.9, 0.9, 1),
            foreground_color=(0, 0, 0, 1)
        )
        self.input_codigo.bind(on_text_validate=self.verificar_codigo)
        ui_box.add_widget(self.input_codigo)

        # Botón
        btn_accion = Button(
            text="GOLPEAR MURO",
            size_hint=(1, .1),
            background_color=(0.8, 0.1, 0.1, 1)
        )
        btn_accion.bind(on_press=self.verificar_codigo)
        ui_box.add_widget(btn_accion)

        self.layout_principal.add_widget(ui_box)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def verificar_codigo(self, instance):
        usuario_resp = self.input_codigo.text.strip()
        desafio = DESAFIOS[self.nivel_actual]
        
        if usuario_resp == desafio['solucion']:
            self.animar_destruccion()
        else:
            self.animar_fallo()

    def animar_destruccion(self):
        anim = Animation(color=(0, 1, 0, 1), duration=0.5) + Animation(opacity=0)
        anim.start(self.codigo_muro_label)
        Clock.schedule_once(lambda dt: self.siguiente_nivel(), 1.5)

    def animar_fallo(self):
        # Efecto simple de parpadeo rojo
        self.input_codigo.background_color = (1, 0.5, 0.5, 1)
        Clock.schedule_once(lambda dt: setattr(self.input_codigo, 'background_color', (0.9, 0.9, 0.9, 1)), 0.2)
        self.input_codigo.text = ""

    def siguiente_nivel(self):
        self.nivel_actual += 1
        self.codigo_muro_label.opacity = 1
        self.cargar_nivel(self.nivel_actual)

    def mostrar_victoria(self):
        self.layout_principal.clear_widgets()
        label = Label(
            text="¡HAS ESCAPADO DEL INFIERNO!\n¡Victoria!",
            font_size='40sp',
            color=(1, 0.8, 0, 1),
            bold=True
        )
        self.layout_principal.add_widget(label)
        
        btn_reiniciar = Button(
            text="Volver a Jugar",
            size_hint=(.5, .1),
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            background_color=(0.1, 0.5, 0.1, 1)
        )
        btn_reiniciar.bind(on_press=self.reiniciar)
        self.layout_principal.add_widget(btn_reiniciar)

    def reiniciar(self, instance):
        self.nivel_actual = 0
        self.manager.current = 'seleccion'

class HellQuestManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = FadeTransition()
        self.add_widget(PantallaSeleccion(name='seleccion'))
        self.add_widget(PantallaJuego(name='juego'))

class HellQuestApp(App):
    personaje_actual = None

    def build(self):
        return HellQuestManager()

if __name__ == '__main__':
    HellQuestApp().run()
