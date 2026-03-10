"""
╔══════════════════════════════════════════════════════════════╗
║                  🎮 CODEQUEST PRO 🎮                        ║
║              Academia de Python - Android                   ║
╚══════════════════════════════════════════════════════════════╝
"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
import time

# COLORES NEÓN
CYAN = get_color_from_hex('#00FFFF')
GREEN = get_color_from_hex('#00FF00')
YELLOW = get_color_from_hex('#FFFF00')
PURPLE = get_color_from_hex('#FF00FF')
ORANGE = get_color_from_hex('#FF6600')
WHITE = get_color_from_hex('#FFFFFF')
RED = get_color_from_hex('#FF0033')
PINK = get_color_from_hex('#FF1493')
BLUE = get_color_from_hex('#0066FF')
DARK = get_color_from_hex('#0A0A14')

Window.clearcolor = DARK

# NIVELES
NIVELES = {
    1: ("NOVATO", CYAN, "🌱"),
    2: ("APRENDIZ", GREEN, "📖"),
    3: ("CODER", BLUE, "💻"),
    4: ("HACKER", PURPLE, "🔥"),
    5: ("ÉLITE", ORANGE, "⚡"),
    6: ("LEYENDA", PINK, "👑"),
    7: ("MAESTRO", YELLOW, "🏆"),
    8: ("SUPREMO", WHITE, "💎"),
}

XP_MODULOS = {
    "01: El Despertar": 150, "02: Almacenes": 200, "03: Variables": 200,
    "04: Condicionales": 250, "05: Bucles": 250, "06: Funciones": 300,
    "07: Listas": 300, "08: Diccionarios": 300, "09: Strings": 250,
    "10: Operadores": 200, "11: Debugging": 350, "12: Retos": 400,
    "13: El Desafío": 500, "14: El Maestro": 600,
}

# ═══════════════════════════════════════════════════════════════
# CONTENIDO DE MÓDULOS - TEXTO GRANDE Y CLARO
# ═══════════════════════════════════════════════════════════════

MODULOS = {
    "01: El Despertar": {
        "leccion": """
━━━━━━━━━━━━━━━━━━━━━━
   EL DESPERTAR
━━━━━━━━━━━━━━━━━━━━━━

Tu primera línea de código


CONCEPTO: PRINT
━━━━━━━━━━━━━━━━━━━━━━

print() muestra texto
en la pantalla.


SINTAXIS:

    print("mensaje")


EJEMPLOS:

    print("Hola")

    print(42)

    print(2 + 2)


REGLAS:
━━━━━━━━━━━━━━━━━━━━━━

• Texto va con comillas

• Números sin comillas

• Cada print = nueva línea


━━━━━━━━━━━━━━━━━━━━━━
""",
        "desafio": "Muestra: Soy un hacker",
        "solucion": ['print("Soy un hacker")'],
        "pista": "print() con comillas"
    },
    
    "02: Almacenes": {
        "leccion": """
━━━━━━━━━━━━━━━━━━━━━━
   ALMACENES
━━━━━━━━━━━━━━━━━━━━━━

Variables: Guardar información


CONCEPTO: VARIABLES
━━━━━━━━━━━━━━━━━━━━━━

Una variable guarda un valor.


SINTAXIS:

    nombre = valor


EJEMPLOS:

    nombre = "Ana"

    edad = 25

    altura = 1.75


REGLAS:
━━━━━━━━━━━━━━━━━━━━━━

• Sin espacios en el nombre

• Usa nombres claros

• Mayúsculas importan


━━━━━━━━━━━━━━━━━━━━━━
""",
        "desafio": "Variable codigo = 'secreto' y mostrar: Tu código es: secreto",
        "solucion": ["codigo = 'secreto'\nprint('Tu código es:', codigo)"],
        "pista": "Crear variable, luego print"
    },
    
    "03: Variables": {
        "leccion": """
━━━━━━━━━━━━━━━━━━━━━━
   TIPOS DE DATOS
━━━━━━━━━━━━━━━━━━━━━━


TIPOS PRINCIPALES:
━━━━━━━━━━━━━━━━━━━━━━

STR - Texto

    nombre = "Hacker"


INT - Números enteros

    edad = 25


FLOAT - Decimales

    precio = 99.99


BOOL - Verdadero/Falso

    activo = True


FUNCIÓN TYPE():
━━━━━━━━━━━━━━━━━━━━━━

    type("Hola")

    → <class 'str'>


━━━━━━━━━━━━━━━━━━━━━━
""",
        "desafio": "Crear nombre, nivel, activo. Mostrar tipos.",
        "solucion": ["nombre = 'Ana'\nnivel = 10\nactivo = True\nprint(type(nombre))\nprint(type(nivel))\nprint(type(activo))"],
        "pista": "Usa type()"
    },
    
    "04: Condicionales": {
        "leccion": """
━━━━━━━━━━━━━━━━━━━━━━
   CONDICIONALES
━━━━━━━━━━━━━━━━━━━━━━

Tomar decisiones


IF-ELSE:
━━━━━━━━━━━━━━━━━━━━━━

    if condición:
        # verdadero
    else:
        # falso


EJEMPLO:

    edad = 18

    if edad >= 18:
        print("Mayor")
    else:
        print("Menor")


OPERADORES:
━━━━━━━━━━━━━━━━━━━━━━

    ==  igual

    !=  diferente

    >   mayor

    <   menor


━━━━━━━━━━━━━━━━━━━━━━
""",
        "desafio": "Si rol='admin' mostrar ACCESO TOTAL",
        "solucion": ["rol = 'admin'\nif rol == 'admin':\n    print('ACCESO TOTAL')\nelse:\n    print('ACCESO LIMITADO')"],
        "pista": "if con =="
    },
    
    "05: Bucles": {
        "leccion": """
━━━━━━━━━━━━━━━━━━━━━━
   BUCLES
━━━━━━━━━━━━━━━━━━━━━━

Repetir código


BUCLE FOR:
━━━━━━━━━━━━━━━━━━━━━━

    for i in range(5):
        print(i)

Muestra: 0 1 2 3 4


BUCLE WHILE:
━━━━━━━━━━━━━━━━━━━━━━

    n = 0
    while n < 5:
        print(n)
        n += 1


CONTROL:
━━━━━━━━━━━━━━━━━━━━━━

    break     → salir

    continue  → saltar


━━━━━━━━━━━━━━━━━━━━━━
""",
        "desafio": "Mostrar pares del 2 al 10",
        "solucion": ["for i in range(2, 11, 2):\n    print(i)"],
        "pista": "range(inicio, fin, paso)"
    },
    
    "06: Funciones": {
        "leccion": """
━━━━━━━━━━━━━━━━━━━━━━
   FUNCIONES
━━━━━━━━━━━━━━━━━━━━━━

Código reutilizable


SINTAXIS:
━━━━━━━━━━━━━━━━━━━━━━

    def nombre():
        return resultado


EJEMPLOS:

    def saludar():
        print("Hola!")


    def suma(a, b):
        return a + b


LLAMAR FUNCIÓN:

    saludar()

    suma(2, 3)


━━━━━━━━━━━━━━━━━━━━━━
""",
        "desafio": "Función a_fahrenheit(celsius) que retenga (c*9/5)+32",
        "solucion": ["def a_fahrenheit(c):\n    return (c * 9/5) + 32\n\nprint(a_fahrenheit(0))"],
        "pista": "def, return"
    },
    
    "07: Listas": {
        "leccion": """
━━━━━━━━━━━━━━━━━━━━━━
   LISTAS
━━━━━━━━━━━━━━━━━━━━━━

Colecciones ordenadas


CREAR:
━━━━━━━━━━━━━━━━━━━━━━

    frutas = ["pera", "uva"]


ACCEDER:

    frutas[0]  → "pera"

    frutas[-1] → "uva"


MÉTODOS:

    append()  → agregar

    remove()  → eliminar

    sort()    → ordenar


━━━━━━━━━━━━━━━━━━━━━━
""",
        "desafio": "Lista: Python, Java, C++. Agregar Rust. Ordenar.",
        "solucion": ["l = ['Python', 'Java', 'C++']\nl.append('Rust')\nl.sort()\nprint(l)"],
        "pista": "append(), sort()"
    },
    
    "08: Diccionarios": {
        "leccion": """
━━━━━━━━━━━━━━━━━━━━━━
   DICCIONARIOS
━━━━━━━━━━━━━━━━━━━━━━

Pares clave:valor


CREAR:
━━━━━━━━━━━━━━━━━━━━━━

    user = {
        "nombre": "Ana",
        "edad": 25
    }


ACCEDER:

    user["nombre"]


RECORRER:

    for k, v in user.items():
        print(k, v)


━━━━━━━━━━━━━━━━━━━━━━
""",
        "desafio": "Diccionario perfil con nombre, nivel, skills.",
        "solucion": ["p = {'nombre': 'Ana', 'nivel': 5}\nfor k, v in p.items():\n    print(k, v)"],
        "pista": "items()"
    },
    
    "09: Strings": {
        "leccion": """
━━━━━━━━━━━━━━━━━━━━━━
   STRINGS
━━━━━━━━━━━━━━━━━━━━━━

Manipular texto


MÉTODOS:
━━━━━━━━━━━━━━━━━━━━━━

    upper()   → MAYÚSCULAS

    lower()   → minúsculas

    strip()   → quita espacios

    replace() → reemplaza


EJEMPLO:

    t = "  hola  "

    t.strip().upper()

    → "HOLA"


F-STRING:

    n = "Ana"

    print(f"Hola, {n}")


━━━━━━━━━━━━━━━━━━━━━━
""",
        "desafio": "Texto='  hacker  ' → quitar espacios y mayúsculas",
        "solucion": ["t = '  hacker  '\nt = t.strip().upper()\nprint(t)"],
        "pista": "strip(), upper()"
    },
    
    "10: Operadores": {
        "leccion": """
━━━━━━━━━━━━━━━━━━━━━━
   OPERADORES
━━━━━━━━━━━━━━━━━━━━━━


ARITMÉTICOS:
━━━━━━━━━━━━━━━━━━━━━━

    +   suma

    -   resta

    *   multiplica

    /   divide

    //  entero

    %   residuo

    **  potencia


COMPARACIÓN:

    ==  igual

    !=  diferente

    >   mayor

    <   menor


━━━━━━━━━━━━━━━━━━━━━━
""",
        "desafio": "Calcular (10+5)*2 - 8/4 y residuo entre 7",
        "solucion": ["r = (10+5)*2 - 8/4\nprint(r)\nprint(int(r) % 7)"],
        "pista": "% para residuo"
    },
    
    "11: Debugging": {
        "leccion": """
━━━━━━━━━━━━━━━━━━━━━━
   DEBUGGING
━━━━━━━━━━━━━━━━━━━━━━

Buscar errores


ERRORES COMUNES:
━━━━━━━━━━━━━━━━━━━━━━

SyntaxError

    → Error de sintaxis


NameError

    → Variable no existe


TypeError

    → Tipo incorrecto


TRY-EXCEPT:

    try:
        x = 10/0
    except:
        print("Error")


━━━━━━━━━━━━━━━━━━━━━━
""",
        "desafio": "Corregir: n = input(); print(n + 10)",
        "solucion": ["n = int(input())\nprint(n + 10)"],
        "pista": "int() para convertir"
    },
    
    "12: Retos": {
        "leccion": """
━━━━━━━━━━━━━━━━━━━━━━
   RETOS FINALES
━━━━━━━━━━━━━━━━━━━━━━

Combinar todo


ESTRATEGIAS:
━━━━━━━━━━━━━━━━━━━━━━

1. Leer problema completo

2. Identificar pasos

3. Implementar

4. Probar


CONCEPTOS:

• Variables

• Condicionales

• Bucles

• Funciones

• Listas


━━━━━━━━━━━━━━━━━━━━━━
""",
        "desafio": "Función que filtre notas >= 70",
        "solucion": ["def filtro(notas):\n    return [n for n in notas if n >= 70]\n\nprint(filtro([85, 60, 90, 70]))"],
        "pista": "for e if"
    },
    
    "13: El Desafío": {
        "leccion": """
━━━━━━━━━━━━━━━━━━━━━━
   EL DESAFÍO
━━━━━━━━━━━━━━━━━━━━━━

Proyecto integrador


SISTEMA DE USUARIOS:
━━━━━━━━━━━━━━━━━━━━━━

• Registrar

• Mostrar

• Buscar

• Actualizar

• Eliminar


ESTRUCTURA:

    users = {}

    users["Ana"] = {"nivel": 5}


━━━━━━━━━━━━━━━━━━━━━━
""",
        "desafio": "Registrar Ana(5), Carlos(8). Subir Ana a 10. Mostrar.",
        "solucion": ["u = {}\nu['Ana'] = {'nivel': 5}\nu['Carlos'] = {'nivel': 8}\nu['Ana']['nivel'] = 10\nfor n, d in u.items():\n    print(n, d['nivel'])"],
        "pista": "Diccionario anidado"
    },
    
    "14: El Maestro": {
        "leccion": """
━━━━━━━━━━━━━━━━━━━━━━
   EL MAESTRO
━━━━━━━━━━━━━━━━━━━━━━

Examen final


JUEGO DE COMBATE:
━━━━━━━━━━━━━━━━━━━━━━

• Vida y ataque

• Turnos

• Ganador


ESTRUCTURA:

    p1_vida = 100

    p1_ataque = 20

    while p1 > 0 and p2 > 0:

        # combatir


━━━━━━━━━━━━━━━━━━━━━━
""",
        "desafio": "2 guerreros pelean por turnos",
        "solucion": ["p1, a1 = 100, 20\np2, a2 = 80, 25\nwhile p1 > 0 and p2 > 0:\n    p2 -= a1\n    if p2 > 0:\n        p1 -= a2\nprint('Gana:', 'P1' if p1 > 0 else 'P2')"],
        "pista": "while con vidas"
    }
}

GLOSARIO = """
━━━━━━━━━━━━━━━━━━━━━━
   GLOSARIO
━━━━━━━━━━━━━━━━━━━━━━

ALGORITMO
Pasos para resolver problema.

BOOLEAN
True o False.

BUG
Error en código.

CLASE
Plantilla para objetos.

DEBUGGING
Buscar errores.

DICIONARIO
Pares clave:valor.

FUNCIÓN
Código reutilizable.

INTEGER
Número entero.

LISTA
Colección ordenada.

LOOP
Bucle, repetición.

MÉTODO
Función en objeto.

STRING
Texto.

VARIABLE
Nombre con valor.

━━━━━━━━━━━━━━━━━━━━━━
"""

CONSEJOS = """
━━━━━━━━━━━━━━━━━━━━━━
   CONSEJOS PRO
━━━━━━━━━━━━━━━━━━━━━━

• Practica todos los días

• Lee código de otros

• Los errores enseñan

• Nombres descriptivos

• Funciones pequeñas

• Comenta el POR QUÉ

• No copies, escribe

━━━━━━━━━━━━━━━━━━━━━━
"""

ATAJOS = """
━━━━━━━━━━━━━━━━━━━━━━
   ATAJOOS
━━━━━━━━━━━━━━━━━━━━━━

PYTHON:

    [x for x in lista]

    a, b = b, a

    texto[::-1]


TERMINAL:

    Tab = autocompletar

    Ctrl+C = cancelar

    ↑↓ = historial


VS CODE:

    Ctrl+S = guardar

    Ctrl+Z = deshacer

    Ctrl+/ = comentar

━━━━━━━━━━━━━━━━━━━━━━
"""

# ═══════════════════════════════════════════════════════════════
# PANTALLAS
# ═══════════════════════════════════════════════════════════════

class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)
        self.name = 'splash'
        layout = BoxLayout(orientation='vertical', padding=50)
        
        layout.add_widget(Label(
            text="[b]CODEQUEST[/b]",
            markup=True, font_size='50sp', color=CYAN,
            size_hint_y=0.6
        ))
        layout.add_widget(Label(
            text="Academia Python",
            font_size='24sp', color=PURPLE,
            size_hint_y=0.2
        ))
        self.progress = ProgressBar(max=100, value=0, size_hint_y=0.1)
        layout.add_widget(self.progress)
        self.status = Label(text="Iniciando...", font_size='18sp', color=GREEN, size_hint_y=0.1)
        layout.add_widget(self.status)
        
        self.add_widget(layout)
        Clock.schedule_once(self.animar, 0.5)
    
    def animar(self, dt):
        for i, (v, t) in enumerate([(33, "Cargando..."), (66, "Preparando..."), (100, "¡Listo!")]):
            Clock.schedule_once(lambda dt, v=v, t=t: self.set_prog(v, t), (i+1)*0.3)
        Clock.schedule_once(lambda dt: setattr(self.manager, 'current', 'menu'), 1.5)
    
    def set_prog(self, v, t):
        self.progress.value = v
        self.status.text = t


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.name = 'menu'
        self.store = JsonStore('cq_xp.json')
        self.layout = BoxLayout(orientation='vertical', padding=15, spacing=8)
        self.add_widget(self.layout)
        Clock.schedule_once(self.load, 0.1)
    
    def load(self, dt):
        self.layout.clear_widgets()
        
        # XP total
        xp = 0
        done = 0
        try:
            for k in self.store.keys():
                if k.startswith('m_'):
                    d = self.store.get(k)
                    if d.get('ok'):
                        done += 1
                        xp += d.get('xp', 0)
        except:
            pass
        
        # Nivel
        nivel = 1
        if xp >= 100: nivel = 2
        if xp >= 300: nivel = 3
        if xp >= 600: nivel = 4
        if xp >= 1000: nivel = 5
        if xp >= 1500: nivel = 6
        if xp >= 2500: nivel = 7
        if xp >= 4000: nivel = 8
        
        nombre_nivel, color_nivel, icono = NIVELES[nivel]
        
        # Header
        header = BoxLayout(size_hint_y=0.2)
        header.add_widget(Label(
            text=f"{icono} [b]CODEQUEST[/b]",
            markup=True, font_size='32sp', color=CYAN
        ))
        header.add_widget(Label(
            text=f"⭐ {xp} XP",
            font_size='26sp', color=YELLOW
        ))
        self.layout.add_widget(header)
        
        # Rango
        self.layout.add_widget(Label(
            text=f"🏆 Rango: {nombre_nivel} | {done}/14 módulos",
            font_size='18sp', color=color_nivel, size_hint_y=0.08
        ))
        
        # Botones recursos
        btns1 = BoxLayout(size_hint_y=0.12, spacing=5)
        for txt, col, scr in [("📖 Glosario", PURPLE, 'glosario'), ("💡 Consejos", ORANGE, 'consejos'),
                              ("⌨️ Atajos", PINK, 'atajos'), ("💻 Terminal", GREEN, 'terminal')]:
            b = Button(text=txt, background_color=col, background_normal='', font_size='16sp', color=DARK)
            b.bind(on_release=lambda x, s=scr: self.go(s))
            btns1.add_widget(b)
        self.layout.add_widget(btns1)
        
        # Separador
        self.layout.add_widget(Label(text="━━━━━ MÓDULOS ━━━━━", size_hint_y=0.05, color=CYAN, font_size='16sp'))
        
        # Módulos
        scroll = ScrollView()
        grid = BoxLayout(orientation='vertical', size_hint_y=None, spacing=6)
        grid.bind(minimum_height=grid.setter('height'))
        
        for nombre in MODULOS.keys():
            key = f"m_{nombre[:2]}"
            hecho = False
            try:
                hecho = self.store.exists(key) and self.store.get(key).get('ok')
            except:
                pass
            
            xp_m = XP_MODULOS.get(nombre, 100)
            col = GREEN if hecho else CYAN
            
            b = Button(
                text=f"{'✓' if hecho else '○'} {nombre} (+{xp_m} XP)",
                size_hint_y=None, height=65,
                background_color=col, background_normal='',
                font_size='18sp', color=DARK
            )
            b.bind(on_release=lambda x, n=nombre: self.go_mod(n))
            grid.add_widget(b)
        
        scroll.add_widget(grid)
        self.layout.add_widget(scroll)
    
    def go(self, screen):
        self.manager.current = screen
    
    def go_mod(self, titulo):
        self.manager.get_screen('leccion').cargar(titulo)
        self.manager.current = 'leccion'


class GlosarioScreen(Screen):
    def __init__(self, **kwargs):
        super(GlosarioScreen, self).__init__(**kwargs)
        self.name = 'glosario'
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        layout.add_widget(Label(text="[b]📖 GLOSARIO[/b]", markup=True, font_size='28sp', color=PURPLE, size_hint_y=0.1))
        
        scroll = ScrollView()
        lbl = Label(text=GLOSARIO, font_size='22sp', color=WHITE, size_hint_y=None, halign='left', valign='top')
        lbl.bind(size=lbl.setter('text_size'))
        lbl.bind(texture_size=lbl.setter('size'))
        scroll.add_widget(lbl)
        layout.add_widget(scroll)
        
        btn = Button(text="← VOLVER", background_color=PURPLE, background_normal='', size_hint_y=0.1, font_size='20sp')
        btn.bind(on_release=lambda x: self.back())
        layout.add_widget(btn)
        
        self.add_widget(layout)
    
    def back(self):
        self.manager.get_screen('menu').load(0)
        self.manager.current = 'menu'


class ConsejosScreen(Screen):
    def __init__(self, **kwargs):
        super(ConsejosScreen, self).__init__(**kwargs)
        self.name = 'consejos'
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        layout.add_widget(Label(text="[b]💡 CONSEJOS PRO[/b]", markup=True, font_size='28sp', color=ORANGE, size_hint_y=0.1))
        
        scroll = ScrollView()
        lbl = Label(text=CONSEJOS, font_size='22sp', color=WHITE, size_hint_y=None, halign='left', valign='top')
        lbl.bind(size=lbl.setter('text_size'))
        lbl.bind(texture_size=lbl.setter('size'))
        scroll.add_widget(lbl)
        layout.add_widget(scroll)
        
        btn = Button(text="← VOLVER", background_color=ORANGE, background_normal='', size_hint_y=0.1, font_size='20sp')
        btn.bind(on_release=lambda x: self.back())
        layout.add_widget(btn)
        
        self.add_widget(layout)
    
    def back(self):
        self.manager.get_screen('menu').load(0)
        self.manager.current = 'menu'


class AtajosScreen(Screen):
    def __init__(self, **kwargs):
        super(AtajosScreen, self).__init__(**kwargs)
        self.name = 'atajos'
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        layout.add_widget(Label(text="[b]⌨️ ATAJOOS[/b]", markup=True, font_size='28sp', color=PINK, size_hint_y=0.1))
        
        scroll = ScrollView()
        lbl = Label(text=ATAJOS, font_size='22sp', color=WHITE, size_hint_y=None, halign='left', valign='top')
        lbl.bind(size=lbl.setter('text_size'))
        lbl.bind(texture_size=lbl.setter('size'))
        scroll.add_widget(lbl)
        layout.add_widget(scroll)
        
        btn = Button(text="← VOLVER", background_color=PINK, background_normal='', size_hint_y=0.1, font_size='20sp')
        btn.bind(on_release=lambda x: self.back())
        layout.add_widget(btn)
        
        self.add_widget(layout)
    
    def back(self):
        self.manager.get_screen('menu').load(0)
        self.manager.current = 'menu'


class TerminalScreen(Screen):
    def __init__(self, **kwargs):
        super(TerminalScreen, self).__init__(**kwargs)
        self.name = 'terminal'
        layout = BoxLayout(orientation='vertical', padding=10, spacing=8)
        
        layout.add_widget(Label(text="[b]💻 TERMINAL[/b]", markup=True, font_size='24sp', color=GREEN, size_hint_y=0.08))
        
        self.output = TextInput(
            text='💻 Terminal\nEscribe: help\n\n',
            readonly=True, multiline=True, size_hint_y=0.76,
            background_color=DARK, foreground_color=GREEN,
            font_name='DroidSansMono', font_size='18sp'
        )
        layout.add_widget(self.output)
        
        self.input = TextInput(
            hint_text='Comando...', multiline=False, size_hint_y=0.08,
            background_color=DARK, foreground_color=GREEN,
            font_name='DroidSansMono', font_size='18sp'
        )
        self.input.bind(on_text_validate=self.ejec)
        layout.add_widget(self.input)
        
        btn = Button(text="← VOLVER", background_color=GREEN, background_normal='', size_hint_y=0.08, font_size='18sp', color=DARK)
        btn.bind(on_release=lambda x: self.back())
        layout.add_widget(btn)
        
        self.add_widget(layout)
    
    def ejec(self, instance):
        cmd = self.input.text.strip().lower()
        self.input.text = ''
        if not cmd:
            return
        
        self.output.text += f"\n> {cmd}\n"
        
        if cmd == 'help':
            self.output.text += "Comandos: help, clear, print, calc\n"
        elif cmd == 'clear':
            self.output.text = ''
        elif cmd.startswith('print '):
            self.output.text += cmd[6:] + '\n'
        elif cmd.startswith('calc '):
            try:
                self.output.text += str(eval(cmd[5:])) + '\n'
            except:
                self.output.text += 'Error\n'
        else:
            self.output.text += "Escribe 'help'\n"
    
    def back(self):
        self.manager.get_screen('menu').load(0)
        self.manager.current = 'menu'


class LeccionScreen(Screen):
    def __init__(self, **kwargs):
        super(LeccionScreen, self).__init__(**kwargs)
        self.name = 'leccion'
        self.store = JsonStore('cq_xp.json')
        self.titulo = None
        self.layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        self.add_widget(self.layout)
    
    def cargar(self, titulo):
        self.titulo = titulo
        self.layout.clear_widgets()
        
        mod = MODULOS.get(titulo, {})
        xp = XP_MODULOS.get(titulo, 100)
        
        # Header
        header = BoxLayout(size_hint_y=0.1, spacing=10)
        
        btn_back = Button(text="←", size_hint_x=0.15, background_color=RED, background_normal='', font_size='24sp')
        btn_back.bind(on_release=lambda x: self.back())
        header.add_widget(btn_back)
        
        header.add_widget(Label(text=f"[b]{titulo}[/b]", markup=True, font_size='22sp', color=CYAN))
        header.add_widget(Label(text=f"+{xp} XP", font_size='18sp', color=YELLOW))
        self.layout.add_widget(header)
        
        # Tabs
        tabs = BoxLayout(size_hint_y=0.1, spacing=8)
        
        self.btn_lec = Button(text="📖 LECCIÓN", background_color=CYAN, background_normal='', font_size='18sp', color=DARK)
        self.btn_lec.bind(on_release=lambda x: self.show_lec(mod))
        
        self.btn_des = Button(text="💻 DESAFÍO", background_color=PURPLE, background_normal='', font_size='18sp')
        self.btn_des.bind(on_release=lambda x: self.show_des(mod))
        
        tabs.add_widget(self.btn_lec)
        tabs.add_widget(self.btn_des)
        self.layout.add_widget(tabs)
        
        # Contenido
        self.cont = BoxLayout(size_hint_y=0.8)
        self.layout.add_widget(self.cont)
        
        self.show_lec(mod)
    
    def show_lec(self, mod):
        self.btn_lec.background_color = CYAN
        self.btn_des.background_color = PURPLE
        self.cont.clear_widgets()
        
        scroll = ScrollView()
        lbl = Label(
            text=mod.get('leccion', 'Sin contenido'),
            font_size='22sp', color=WHITE,
            size_hint_y=None, halign='left', valign='top'
        )
        lbl.bind(size=lbl.setter('text_size'))
        lbl.bind(texture_size=lbl.setter('size'))
        scroll.add_widget(lbl)
        self.cont.add_widget(scroll)
    
    def show_des(self, mod):
        self.btn_lec.background_color = PURPLE
        self.btn_des.background_color = GREEN
        self.cont.clear_widgets()
        
        layout = BoxLayout(orientation='vertical', spacing=10)
        
        layout.add_widget(Label(
            text=f"[b]DESAFÍO:[/b] {mod.get('desafio', '')}",
            markup=True, font_size='20sp', color=YELLOW,
            size_hint_y=0.12, halign='left'
        ))
        
        layout.add_widget(Label(
            text=f"💡 {mod.get('pista', '')}",
            font_size='16sp', color=WHITE, size_hint_y=0.08
        ))
        
        self.code = TextInput(
            hint_text='Tu código aquí...',
            multiline=True, size_hint_y=0.5,
            background_color=DARK, foreground_color=GREEN,
            font_name='DroidSansMono', font_size='18sp'
        )
        layout.add_widget(self.code)
        
        btns = BoxLayout(size_hint_y=0.12, spacing=10)
        
        btn_check = Button(text="✓ VERIFICAR", background_color=GREEN, background_normal='', font_size='20sp', color=DARK)
        btn_check.bind(on_release=lambda x: self.check(mod))
        
        btn_sol = Button(text="👁 SOLUCIÓN", background_color=PURPLE, background_normal='', font_size='20sp')
        btn_sol.bind(on_release=lambda x: self.show_sol(mod))
        
        btns.add_widget(btn_check)
        btns.add_widget(btn_sol)
        layout.add_widget(btns)
        
        self.res = Label(text="", markup=True, font_size='20sp', size_hint_y=0.1)
        layout.add_widget(self.res)
        
        self.cont.add_widget(layout)
    
    def check(self, mod):
        codigo = self.code.text.strip()
        sols = mod.get('solucion', [])
        xp = XP_MODULOS.get(self.titulo, 100)
        
        if not codigo:
            self.res.text = "[color=ff3366]❌ Escribe código[/color]"
            return
        
        ok = any(codigo.replace(' ', '').lower() == s.replace(' ', '').lower() for s in sols)
        
        if ok:
            self.res.text = f"[color=00ff00]✓ ¡CORRECTO! +{xp} XP[/color]"
            key = f"m_{self.titulo[:2]}"
            try:
                self.store.put(key, ok=True, xp=xp)
            except:
                pass
            Clock.schedule_once(lambda dt: self.back(), 2)
        else:
            self.res.text = "[color=ff3366]❌ Intenta de nuevo[/color]"
    
    def show_sol(self, mod):
        sols = mod.get('solucion', [])
        if sols:
            Popup(
                title='Solución',
                content=Label(text=sols[0], font_size='18sp', color=GREEN),
                size_hint=(0.9, 0.5),
                background=DARK
            ).open()
    
    def back(self):
        self.manager.get_screen('menu').load(0)
        self.manager.current = 'menu'


class CodeQuestApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition(duration=0.2))
        sm.add_widget(SplashScreen())
        sm.add_widget(MenuScreen())
        sm.add_widget(LeccionScreen())
        sm.add_widget(GlosarioScreen())
        sm.add_widget(ConsejosScreen())
        sm.add_widget(AtajosScreen())
        sm.add_widget(TerminalScreen())
        return sm
    
    def on_pause(self):
        return True


if __name__ == '__main__':
    CodeQuestApp().run()
