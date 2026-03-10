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
from kivy.metrics import dp
from kivy.graphics import Color, Rectangle

# Configuración de ventana (para pruebas en PC)
Window.clearcolor = (0.05, 0.05, 0.07, 1) # Fondo oscuro estilo "Hell"

# --- BASE DE DATOS DE DESAFÍOS (PAREDES DE PROGRAMACIÓN) ---
# Puedes agregar tantos niveles como quieras aquí
DESAFIOS = [
    {
        "titulo": "Puerta del Bucle",
        "descripcion": "El muro requiere un bucle infinito para romperse.",
        "codigo_incorrecto": "while False:",
        "solucion": "while True:",
        "pista": "True"
    },
    {
        "titulo": "Muro de la Variable",
        "descripcion": "Define la variable 'poder' con el valor 100.",
        "codigo_incorrecto": "poder = 'cien'",
        "solucion": "poder = 100",
        "pista": "100"
    },
    {
        "titulo": "Muralla de la Impresión",
        "descripcion": "Imprime la palabra 'CLAVE' para abrir la cerradura.",
        "codigo_incorrecto": "print(clave)",
        "solucion": "print('CLAVE')",
        "pista": "'CLAVE'"
    }
]

# --- PANTALLA DE SELECCIÓN DE PERSONAJE ---
class PantallaSeleccion(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        # Imagen de fondo (Asegúrate que la ruta sea correcta en tu proyecto)
        # Si la imagen no carga, el color de fondo de Window se verá.
        try:
            self.bg = Image(source='assets/icons/splash.png', allow_stretch=True, keep_ratio=False)
            layout.add_widget(self.bg)
        except:
            print("Advertencia: No se encontró splash.png")

        # Título Estilizado
        title_label = Label(
            text="[b]HELL QUEST[/b]\nSelecciona tu Guerrero",
            markup=True,
            font_size='24sp',
            color=(1, 0.3, 0.3, 1), # Rojo Hell
            size_hint=(1, .1),
            pos_hint={'top': 1}
        )
        layout.add_widget(title_label)

        # Botones de Personajes (Reorganizados para mejor UX)
        # En lugar de botones invisibles, usaré botones estilizados transparentes
        # para que funcionen en cualquier resolución.
        
        personajes = [
            ("Helios", 0.5, 0.65),
            ("Fabio", 0.5, 0.45),
            ("Nahomy", 0.25, 0.55),
            ("Nora", 0.75, 0.55)
        ]

        for nombre, x, y in personajes:
            btn = Button(
                text=nombre,
                size_hint=(.3, .1),
                pos_hint={'center_x': x, 'center_y': y},
                background_color=(0.8, 0.2, 0.2, 0.6), # Rojo semitransparente
                color=(1, 1, 1, 1),
                font_size='18sp'
            )
            btn.bind(on_press=lambda instance, n=nombre: self.seleccionar_personaje(n))
            layout.add_widget(btn)

        self.add_widget(layout)

    def seleccionar_personaje(self, nombre):
        print(f"Personaje seleccionado: {nombre}")
        # Guardamos el personaje en las variables globales de la App
        App.get_running_app().personaje_actual = nombre
        # Cambiamos a la pantalla de juego
        self.manager.current = 'juego'

# --- PANTALLA DEL JUEGO (PAREDES DE PROGRAMACIÓN) ---
class PantallaJuego(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nivel_actual = 0
        self.layout_principal = FloatLayout()
        self.add_widget(self.layout_principal)
        
        # Fondo del juego (puede ser diferente al menú)
        # self.bg_juego = Image(source='assets/icons/bg_game.png', allow_stretch=True)
        # self.layout_principal.add_widget(self.bg_juego)

    def on_enter(self):
        # Se llama cada vez que entramos a esta pantalla
        self.cargar_nivel(self.nivel_actual)

    def cargar_nivel(self, indice):
        self.layout_principal.clear_widgets()
        
        if indice >= len(DESAFIOS):
            self.mostrar_victoria()
            return

        desafio = DESAFIOS[indice]
        
        # Contenedor UI
        ui_box = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # 1. Título del Desafío
        titulo = Label(
            text=f"[b]{desafio['titulo']}[/b]",
            markup=True,
            font_size='28sp',
            size_hint=(1, .15),
            color=(0.9, 0.5, 0.1, 1)
        )
        ui_box.add_widget(titulo)

        # 2. Descripción
        desc = Label(
            text=desafio['descripcion'],
            font_size='18sp',
            size_hint=(1, .1),
            color=(1, 1, 1, 1)
        )
        ui_box.add_widget(desc)

        # 3. El Muro (Código Incorrecto) - Visualización
        muro_container = BoxLayout(size_hint=(1, .3))
        with muro_container.canvas.before:
            Color(0.2, 0.2, 0.2, 1) # Gris oscuro (Piedra)
            self.rect = Rectangle(size=muro_container.size, pos=muro_container.pos)
            muro_container.bind(size=self._update_rect, pos=self._update_rect)
        
        self.codigo_muro_label = Label(
            text=desafio['codigo_incorrecto'],
            font_name='RobotoMono', # Tipografía de código
            font_size='22sp',
            color=(1, 0, 0, 1), # Rojo error
            canvas_after=None
        )
        muro_container.add_widget(self.codigo_muro_label)
        ui_box.add_widget(muro_container)

        # 4. Entrada del Usuario
        self.input_codigo = TextInput(
            hint_text="Escribe la línea de código correcta aquí...",
            multiline=False,
            font_size='20sp',
            size_hint=(1, .1),
            background_color=(0.9, 0.9, 0.9, 1),
            foreground_color=(0, 0, 0, 1)
        )
        self.input_codigo.bind(on_text_validate=self.verificar_codigo)
        ui_box.add_widget(self.input_codigo)

        # 5. Botón de Acción
        btn_accion = Button(
            text="GOLPEAR MURO",
            size_hint=(1, .1),
            background_color=(0.8, 0.1, 0.1, 1)
        )
        btn_accion.bind(on_press=self.verificar_codigo)
        ui_box.add_widget(btn_accion)

        # 6. Barra de Progreso
        progreso_text = Label(
            text=f"Nivel {indice + 1} / {len(DESAFIOS)}",
            size_hint=(1, .1),
            font_size='14sp'
        )
        ui_box.add_widget(progreso_text)

        self.layout_principal.add_widget(ui_box)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def verificar_codigo(self, instance):
        usuario_resp = self.input_codigo.text.strip()
        desafio = DESAFIOS[self.nivel_actual]
        
        if usuario_resp == desafio['solucion']:
            print("¡Correcto!")
            self.animar_destruccion()
        else:
            print("Incorrecto")
            self.animar_fallo()

    def animar_destruccion(self):
        # Animación simple: fundir a verde y pasar nivel
        anim = Animation(color=(0, 1, 0, 1), duration=0.5) + Animation(opacity=0)
        anim.start(self.codigo_muro_label)
        
        # Esperar un segundo y cargar siguiente nivel
        Clock = __import__('kivy.clock').Clock
        Clock.schedule_once(lambda dt: self.siguiente_nivel(), 1.5)

    def animar_fallo(self):
        # Vibrar el input (efecto de sacudida)
        anim = Animation(x=self.input_codigo.x - 10, duration=0.05)
        anim += Animation(x=self.input_codigo.x + 10, duration=0.05)
        anim += Animation(x=self.input_codigo.x, duration=0.05)
        anim.start(self.input_codigo)
        self.input_codigo.text = "" # Limpiar

    def siguiente_nivel(self):
        self.nivel_actual += 1
        # Restaurar opacidad para el siguiente nivel
        self.codigo_muro_label.opacity = 1
        self.cargar_nivel(self.nivel_actual)

    def mostrar_victoria(self):
        self.layout_principal.clear_widgets()
        label = Label(
            text="¡HAS ESCAPADO DEL INFIERNO!\n¡Victoria Total!",
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

# --- GESTOR DE PANTALLAS ---
class HellQuestManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = FadeTransition()
        self.add_widget(PantallaSeleccion(name='seleccion'))
        self.add_widget(PantallaJuego(name='juego'))

# --- APP PRINCIPAL ---
class HellQuestApp(App):
    personaje_actual = None # Variable global para guardar quién juega

    def build(self):
        return HellQuestManager()

if __name__ == '__main__':
    HellQuestApp().run()
