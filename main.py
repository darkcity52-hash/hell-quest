"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║     ██████╗ ██████╗ ██████╗ ███████╗    ██████╗  █████╗ ███╗   ███╗███████╗ █████╗ ██████╗ ██████╗ ██████╗ ███████╗                                            ║
║    ██╔════╝██╔═══██╗██╔══██╗██╔════╝    ██╔══██╗██╔══██╗████╗ ████║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝                                           ║
║    ██║     ██║   ██║██║  ██║█████╗      ██████╔╝███████║██╔████╔██║███████╗███████║██████╔╝██████╔╝██║  ██║█████╗                                             ║
║    ██║     ██║   ██║██║  ██║██╔══╝      ██╔══██╗██╔══██║██║╚██╔╝██║╚════██║██╔══██║██╔══██╗██╔══██╗██║  ██║██╔══╝                                             ║
║    ╚██████╗╚██████╔╝██████╔╝███████╗    ██║  ██║██║  ██║██║ ╚═╝ ██║███████║██║  ██║██║  ██║██║  ██║██████╔╝███████╗                                          ║
║     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝                                           ║
║                                                                           ║
║                      🎮 ACADEMIA PRO DE PYTHON 🎮                         ║
║                           Versión 2.5 ULTIMATE                            ║
║                                                                           ║
║                    "El código es tu arma. Úsala bien."                    ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

Desarrollado con ❤️ para la próxima generación de hackers éticos
"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.modalview import ModalView
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.properties import NumericProperty, StringProperty, BooleanProperty, ListProperty
from kivy.graphics import Color, Rectangle, Line, RoundedRectangle, PushMatrix, PopMatrix, Rotate
from kivy.metrics import dp
from kivy.effects.scroll import ScrollEffect
import random
import time
import math
import os
import json

# ═══════════════════════════════════════════════════════════════════════════
# 🎨 PALETA DE COLORES NEÓN BRILLANTE - CYBERPUNK 2.0
# ═══════════════════════════════════════════════════════════════════════════

# Colores Neón Intensos
NEON_CYAN = get_color_from_hex('#00FFFF')
NEON_MAGENTA = get_color_from_hex('#FF00FF')
NEON_GREEN = get_color_from_hex('#00FF00')
NEON_YELLOW = get_color_from_hex('#FFFF00')
NEON_ORANGE = get_color_from_hex('#FF6600')
NEON_PINK = get_color_from_hex('#FF1493')
NEON_PURPLE = get_color_from_hex('#9400D3')
NEON_BLUE = get_color_from_hex('#0066FF')
NEON_RED = get_color_from_hex('#FF0033')
NEON_WHITE = get_color_from_hex('#FFFFFF')

# Fondos
FONDO_OLED = get_color_from_hex('#05050A')
FONDO_OSCURO = get_color_from_hex('#0A0A14')
FONDO_TARJETA = get_color_from_hex('#12121F')
FONDO_INPUT = get_color_from_hex('#0D0D18')

# Gradientes simulados
GRADIENT_START = get_color_from_hex('#1A0A2E')
GRADIENT_END = get_color_from_hex('#0A1A2E')

Window.clearcolor = FONDO_OLED

# ═══════════════════════════════════════════════════════════════════════════
# 📊 SISTEMA DE XP Y NIVELES
# ═══════════════════════════════════════════════════════════════════════════

NIVELES = {
    1: {"nombre": "NOVATO", "xp_min": 0, "color": NEON_CYAN, "icono": "🌱"},
    2: {"nombre": "APRENDIZ", "xp_min": 100, "color": NEON_GREEN, "icono": "📖"},
    3: {"nombre": "CODER", "xp_min": 300, "color": NEON_BLUE, "icono": "💻"},
    4: {"nombre": "HACKER", "xp_min": 600, "color": NEON_PURPLE, "icono": "🔥"},
    5: {"nombre": "ÉLITE", "xp_min": 1000, "color": NEON_ORANGE, "icono": "⚡"},
    6: {"nombre": "LEYENDA", "xp_min": 1500, "color": NEON_PINK, "icono": "👑"},
    7: {"nombre": "MAESTRO", "xp_min": 2500, "color": NEON_YELLOW, "icono": "🏆"},
    8: {"nombre": "MAESTRO SUPREMO", "xp_min": 4000, "color": NEON_WHITE, "icono": "💎"},
}

XP_POR_MODULO = {
    "01: El Despertar": 150,
    "02: Almacenes": 200,
    "03: Variables": 200,
    "04: Condicionales": 250,
    "05: Bucles": 250,
    "06: Funciones": 300,
    "07: Listas": 300,
    "08: Diccionarios": 300,
    "09: Strings": 250,
    "10: Operadores": 200,
    "11: Debugging": 350,
    "12: Retos Finales": 400,
    "13: El Desafío": 500,
    "14: El Maestro": 600,
}

def calcular_nivel(xp):
    """Calcula el nivel basado en XP total"""
    nivel_actual = 1
    for nivel, datos in NIVELES.items():
        if xp >= datos["xp_min"]:
            nivel_actual = nivel
    return nivel_actual

def xp_para_siguiente_nivel(xp):
    """Calcula XP necesario para el siguiente nivel"""
    nivel_actual = calcular_nivel(xp)
    if nivel_actual >= 8:
        return 0, 0, 0  # Máximo nivel
    siguiente = nivel_actual + 1
    xp_actual_nivel = NIVELES[nivel_actual]["xp_min"]
    xp_siguiente = NIVELES[siguiente]["xp_min"]
    progreso = xp - xp_actual_nivel
    necesario = xp_siguiente - xp_actual_nivel
    return progreso, necesario, siguiente

# ═══════════════════════════════════════════════════════════════════════════
# 📖 HISTORIA INMERSIVA - "EL DESPERTAR DEL CÓDIGO"
# ═══════════════════════════════════════════════════════════════════════════

HISTORIA = {
    "intro": {
        "titulo": "PRÓLOGO: EL MENSAJE",
        "texto": """
╔═════════════════════════════════════════════════════════════════╗
║                     📨 MENSAJE INTERCEPTADO                    ║
╚═════════════════════════════════════════════════════════════════╝

Tu teléfono vibra. Es una señal desconocida.

Un mensaje aparece en tu pantalla:

    "Nos han estado observando. El sistema 
     controla todo. Pero el código... el 
     código es libertad.
     
     Si puedes leer esto, tienes potencial.
     La Resistencia te necesita.
     
     - CIPHER"

El mensaje se auto-destruye en 5 segundos.

Tu corazón se acelera. ¿Quién es CIPHER? 
¿Qué es la Resistencia?

Solo hay una forma de averiguarlo...

    [ Aprende Python. Descifra la verdad. ]

""",
    },
    "modulo_1": {
        "titulo": "CAPÍTULO 1: EL DESPERTAR",
        "texto": """
╔═════════════════════════════════════════════════════════════════╗
║                    🌅 EL DESPERTAR                              ║
╚═════════════════════════════════════════════════════════════════╝

CIPHER aparece en tu terminal:

    "Ahí estás. Sabía que responderías.
    
     Todo comienza con un simple PRINT.
     En el mundo digital, es tu primera voz.
     Tu primera declaración de existencia.
     
     El sistema quiere silenciarte.
     PRINT es tu forma de gritar al mundo:
     '¡AQUÍ ESTOY!'
     
     Tu primera misión: Haz que la máquina
     reconozca tu presencia.
     
     Muestra: 'Soy un hacker'"

La pantalla parpadea en espera de tu código...
""",
    },
    "modulo_2": {
        "titulo": "CAPÍTULO 2: LOS ALMACENES",
        "texto": """
╔═════════════════════════════════════════════════════════════════╗
║                    📦 LOS ALMACENES SECRETOS                    ║
╚═════════════════════════════════════════════════════════════════╝

CIPHER te contacta de nuevo:

    "Impresionante. Has dado tu primer paso.
    
     Ahora necesitas aprender a guardar 
     información. En este mundo, el 
     conocimiento es poder. Y el poder
     debe protegerse.
     
     Las VARIABLES son tus almacenes 
     secretos. Donde guardas códigos,
     contraseñas, secretos...
     
     CIPHER tuvo un mentor hace años.
     Su código secreto era: secreto123
     
     Crea una variable que lo recuerde."

Un patrón de luz aparece en tu pantalla...
""",
    },
    "modulo_3": {
        "titulo": "CAPÍTULO 3: LOS TIPOS",
        "texto": """
╔═════════════════════════════════════════════════════════════════╗
║                    🔢 EL ARCHIVO DE TIPOS                       ║
╚═════════════════════════════════════════════════════════════════╝

CIPHER envía un archivo cifrado:

    "No toda información es igual.
     
     TEXTOS para mensajes.
     NÚMEROS para códigos.
     BOOLEANOS para decisiones.
     
     El sistema clasifica todo.
     Si entiendes los TIPOS, entiendes
     cómo organiza datos el enemigo.
     
     Mira este archivo confidencial:
     Nombre: Agente_X
     Nivel: 7
     Activo: True
     
     Tu misión: Identificar cada tipo."

El archivo se descifra parcialmente...
""",
    },
    "modulo_4": {
        "titulo": "CAPÍTULO 4: LA BIFURCACIÓN",
        "texto": """
╔═════════════════════════════════════════════════════════════════╗
║                    🔀 LA BIFURCACIÓN                            ║
╚═════════════════════════════════════════════════════════════════╝

Alarma en tu terminal:

    "¡ALERTA! El sistema te ha detectado.
     
     Tienes que aprender a tomar decisiones.
     IF... ELSE... es tu nave de escape.
     
     Si eres ADMIN, tienes acceso total.
     Si no... te capturan.
     
     El sistema verifica tu ROL.
     Demuestra que puedes hackearlo.
     Haz que el código te dé ACCESO TOTAL."

La pantalla muestra un candado virtual...
""",
    },
    "modulo_5": {
        "titulo": "CAPÍTULO 5: EL CICLO ETERNO",
        "texto": """
╔═════════════════════════════════════════════════════════════════╗
║                    🔄 EL CICLO ETERNO                           ║
╚═════════════════════════════════════════════════════════════════╝

CIPHER reaparece:

    "El sistema está en constante movimiento.
     Datos fluyen, procesos se repiten.
     
     BUCLES son la herramienta del hacker.
     Con FOR, puedes escanear puertos.
     Con WHILE, puedes mantener conexiones.
     
     Pero cuidado... un bucle infinito
     puede ser tu perdición o tu arma.
     
     Los números pares del 2 al 10 son
     la clave del próximo servidor.
     Genéralos."

Una dirección IP parpadea en la pantalla...
""",
    },
    "modulo_6": {
        "titulo": "CAPÍTULO 6: LOS PROTOCOLOS",
        "texto": """
╔═════════════════════════════════════════════════════════════════╗
║                    ⚙️ LOS PROTOCOLOS OCULTOS                    ║
╚═════════════════════════════════════════════════════════════════╝

Mensaje encriptado de CIPHER:

    "Has llegado lejos. La Resistencia
     está impresionada.
     
     Ahora aprenderás FUNCIONES.
     Son protocolos reutilizables.
     Un código que escribes una vez
     y usas infinitas veces.
     
     La conversión de temperatura es
     un protocolo clásico de encriptación.
     Celsius a Fahrenheit... 
     
     Los agentes usan 0°C como señal.
     Conviértelo. Descubre el mensaje."

El código comienza a revelarse...
""",
    },
    "modulo_7": {
        "titulo": "CAPÍTULO 7: LA BASE DE DATOS",
        "texto": """
╔═════════════════════════════════════════════════════════════════╗
║                    📋 LA BASE DE DATOS                          ║
╚═════════════════════════════════════════════════════════════════╝

Acceso concedido a archivo clasificado:

    "Has hackeado la primera capa.
     
     Ahora tienes acceso a LISTAS.
     Arrays de información clasificada.
     Los lenguajes de programación son
     la base de datos del sistema.
     
     Python. Java. C++. JavaScript.
     Y uno nuevo... RUST.
     
     Tu misión: Organiza esta base de datos.
     Ordénala alfabéticamente.
     
     El patrón revelará coordenadas."

Una lista cifrada aparece...
""",
    },
    "modulo_8": {
        "titulo": "CAPÍTULO 8: LOS EXPEDIENTES",
        "texto": """
╔═════════════════════════════════════════════════════════════════╗
║                    📖 LOS EXPEDIENTES SECRETOS                  ║
╚═════════════════════════════════════════════════════════════════╝

CIPHER comparte archivos confidenciales:

    "DICCIONARIOS son expedientes completos.
     Cada clave es un nombre.
     Cada valor es información clasificada.
     
     Mira este perfil de agente:
     
     Nombre: Phantom
     Nivel: 10
     Skills: Python, Linux, Hacking
     
     Crea tu propio perfil de hacker.
     Será tu identidad en la Resistencia."

Un formulario holográfico aparece...
""",
    },
    "modulo_9": {
        "titulo": "CAPÍTULO 9: EL CIFRADOR",
        "texto": """
╔═════════════════════════════════════════════════════════════════╗
║                    🔤 EL CIFRADOR DE TEXTOS                     ║
╚═════════════════════════════════════════════════════════════════╝

Un dispositivo extraño se conecta:

    "STRINGS son la base de las comunicaciones.
     Manipular texto es manipular información.
     
     Cifrar. Descifrar. Transformar.
     
     El mensaje secreto de la Resistencia:
       '  hacker python  '
     
     Límpialo. Mayúsculas. Reemplaza.
     PYTHON debe ser MASTER.
     
     El mensaje final revelará tu próxima 
     coordenada de misión."

El cifrador se activa...
""",
    },
    "modulo_10": {
        "titulo": "CAPÍTULO 10: LA CALCULADORA",
        "texto": """
╔═════════════════════════════════════════════════════════════════╗
║                    ➕ LA CALCULADORA DEL SISTEMA                ║
╚═════════════════════════════════════════════════════════════════╝

CIPHER te envía coordenadas:

    "OPERADORES son tu calculadora mental.
     Suma. Resta. Multiplica. Divide.
     
     Las coordenadas están cifradas:
     (10 + 5) * 2 - 8 / 4
     
     El resultado es una ubicación.
     El residuo al dividir entre 7 es 
     el código de acceso.
     
     Calcula. Ubícate. Avanza."

Un mapa virtual se despliega...
""",
    },
    "modulo_11": {
        "titulo": "CAPÍTULO 11: EL DEPURADOR",
        "texto": """
╔═════════════════════════════════════════════════════════════════╗
║                    🐛 EL DEPURADOR DE ERRORES                   ║
╚═════════════════════════════════════════════════════════════════╝

¡ERROR EN EL SISTEMA!

    "¡CUIDADO! El sistema ha inyectado bugs.
     
     DEBUGGING es encontrar errores.
     El código corrupto:
       numero = input('Dame un número: ')
       print(numero + 10)
     
     ¿Ves el error? El sistema intenta
     sumar texto con número.
     
     Depura el código. Sálvate del crash.
     El sistema no tendrá piedad."

Una cascada de errores aparece...
""",
    },
    "modulo_12": {
        "titulo": "CAPÍTULO 12: LA PRUEBA FINAL",
        "texto": """
╔═════════════════════════════════════════════════════════════════╗
║                    🏆 LA PRUEBA FINAL                           ║
╚═════════════════════════════════════════════════════════════════╝

CIPHER envía su último mensaje:

    "Has llegado lejos, joven hacker.
     
     Los RETOS FINALES combinan todo.
     Variables, bucles, condicionales,
     funciones, listas... TODO.
     
     Tu misión: Filtrar datos.
     Solo los aprobados (nota >= 70)
     son agentes activos.
     
     Las notas son: 85, 60, 90, 45, 70, 55, 95
     
     ¿Cuántos agentes hay en total?"

La última puerta se abre...
""",
    },
    "modulo_13": {
        "titulo": "CAPÍTULO 13: EL SISTEMA",
        "texto": """
╔═════════════════════════════════════════════════════════════════╗
║                    ⚔️ EL SISTEMA CENTRAL                        ║
╚═════════════════════════════════════════════════════════════════╝

Has llegado al núcleo del sistema:

    "Este es EL DESAFÍO INTEGRADOR.
     
     Un sistema de usuarios completo.
     Registrar. Mostrar. Buscar. 
     Actualizar. Eliminar.
     
     Ana (Nivel 5)
     Carlos (Nivel 8)
     Maria (Nivel 3)
     
     Sube a Ana a Nivel 10.
     Muestra todos los usuarios.
     
     El sistema debe reconocerte como
     administrador."

El núcleo del sistema parpadea...
""",
    },
    "modulo_14": {
        "titulo": "CAPÍTULO 14: EL MAESTRO SUPREMO",
        "texto": """
╔═════════════════════════════════════════════════════════════════╗
║                    👑 EL MAESTRO SUPREMO                        ║
╚═════════════════════════════════════════════════════════════════╝

CIPHER aparece por última vez:

    "Has demostrado tu valía.
     
     El EXAMEN FINAL es un COMBATE.
     Dos guerreros. Vidas. Ataques.
     Turnos que deciden el destino.
     
     Jugador 1: Vida 100, Ataque 20
     Jugador 2: Vida 80, Ataque 25
     
     Haz que luchen hasta que uno caiga.
     El ganador será el MAESTRO SUPREMO.
     
     ¿Estás listo para la batalla final?"

La arena digital se materializa...
""",
    },
    "final": {
        "titulo": "🌟 FINAL: NUEVO MAESTRO",
        "texto": """
╔═════════════════════════════════════════════════════════════════╗
║                  🎉 ¡FELICIDADES, MAESTRO! 🎉                   ║
╚═════════════════════════════════════════════════════════════════╝

CIPHER te entrega el mensaje final:

    "Lo has logrado.
     
     Has demostrado dominar Python.
     Has superado todos los desafíos.
     Has vencido al sistema.
     
     Pero esto es solo el comienzo.
     
     La Resistencia te necesita.
     El código es libertad.
     Y tú... tú eres ahora un MAESTRO.
     
     Ve y hackea el mundo... éticamente.
     
     - CIPHER
     
     [TRANSMISIÓN FINALIZADA]"

🌟 ¡Eres oficialmente un MAESTRO SUPREMO! 🌟

""",
    }
}

# ═══════════════════════════════════════════════════════════════════════════
# 📖 GLOSARIO COMPLETO - 200+ TÉRMINOS
# ═══════════════════════════════════════════════════════════════════════════

GLOSARIO = {
    # A
    "Algoritmo": "Secuencia de pasos para resolver un problema. Como una receta de cocina.",
    "Argumento": "Valor que se pasa a una función cuando se llama. Ejemplo: print('hola') - 'hola' es el argumento.",
    "Array": "Estructura que guarda múltiples valores del mismo tipo. En Python se llaman listas.",
    "Asignación": "Dar un valor a una variable usando =. Ejemplo: x = 5",
    "API": "Application Programming Interface. Puente para que programas se comuniquen.",
    "ASCII": "Código que representa caracteres como números. A=65, B=66, etc.",
    "Async": "Asíncrono. Código que no bloquea, puede ejecutarse en paralelo.",
    "AWK": "Lenguaje de procesamiento de texto en Unix/Linux.",
    
    # B
    "Backend": "Parte del servidor de una aplicación. La lógica oculta.",
    "Bug": "Error en el código que causa comportamiento inesperado.",
    "Boolean": "Tipo de dato que solo puede ser True o False.",
    "Break": "Palabra clave que sale de un bucle inmediatamente.",
    "Buffer": "Área de memoria temporal para almacenar datos.",
    "Byte": "8 bits. Unidad básica de almacenamiento.",
    "Bash": "Shell de Unix. Intérprete de comandos de Linux.",
    "Build": "Proceso de compilar código fuente en ejecutable.",
    
    # C
    "Código fuente": "Instrucciones escritas en lenguaje de programación.",
    "Compilar": "Convertir código fuente a lenguaje máquina.",
    "Clase": "Plantilla para crear objetos. Define atributos y métodos.",
    "Comentario": "Texto en código que no se ejecuta. Se usa # en Python.",
    "Concatenar": "Unir strings. 'Hola' + ' Mundo' = 'Hola Mundo'",
    "Condición": "Expresión que evalúa a True o False.",
    "Constante": "Variable cuyo valor no cambia durante ejecución.",
    "Console": "Interfaz de texto para interactuar con el sistema.",
    "CSS": "Cascading Style Sheets. Lenguaje para estilos web.",
    "CSV": "Comma Separated Values. Formato de archivo con datos separados por comas.",
    "Callback": "Función que se pasa como argumento a otra función.",
    "Cache": "Memoria temporal para acceso rápido a datos frecuentes.",
    
    # D
    "Debugging": "Proceso de encontrar y corregir errores en código.",
    "Diccionario": "Estructura que guarda pares clave:valor. {}",
    "DOM": "Document Object Model. Representación de página web.",
    "Docker": "Plataforma para crear contenedores de aplicaciones.",
    "Data Type": "Tipo de dato: int, str, float, bool, etc.",
    "Debug": "Depurar. Encontrar y corregir errores.",
    "Default": "Valor por defecto si no se especifica otro.",
    "Deprecado": "Código obsoleto que pronto se eliminará.",
    
    # E
    "Editor": "Programa para escribir código. VS Code, Sublime, etc.",
    "Exception": "Error que ocurre durante ejecución. Se maneja con try/except.",
    "Expresión": "Combinación de valores y operadores que produce resultado.",
    "Encapsulamiento": "Ocultar detalles internos de un objeto.",
    "Entorno virtual": "Aislamiento de dependencias Python. venv.",
    "EOF": "End Of File. Marcador de fin de archivo.",
    "Elif": "Else if en Python. Condición adicional.",
    
    # F
    "Frontend": "Parte visible de una aplicación. Interfaz de usuario.",
    "Función": "Bloque de código reutilizable. def en Python.",
    "Float": "Número decimal. 3.14, -0.5, etc.",
    "Framework": "Estructura base para desarrollar aplicaciones.",
    "For": "Bucle que itera sobre secuencia conocida.",
    "F-string": "Formateo de strings en Python. f'Hola {nombre}'",
    "Full Stack": "Desarrollo de frontend y backend.",
    "FTP": "File Transfer Protocol. Protocolo para transferir archivos.",
    
    # G
    "Git": "Sistema de control de versiones distribuido.",
    "GitHub": "Plataforma para hospedar repositorios Git.",
    "GUI": "Graphical User Interface. Interfaz gráfica de usuario.",
    "Glob": "Patrón para buscar archivos. *.py encuentra todos los Python.",
    "Garbage Collection": "Limpieza automática de memoria no usada.",
    
    # H
    "HTML": "HyperText Markup Language. Lenguaje de páginas web.",
    "HTTP": "HyperText Transfer Protocol. Protocolo de comunicación web.",
    "Hash": "Función que convierte datos en valor fijo. MD5, SHA.",
    "Hook": "Punto de extensión en código para agregar funcionalidad.",
    "Hostname": "Nombre de un dispositivo en red.",
    
    # I
    "IDE": "Integrated Development Environment. PyCharm, VS Code.",
    "Import": "Cargar módulo externo. import math",
    "Indentación": "Espacios al inicio de línea. Estructura en Python.",
    "Index": "Posición de elemento en secuencia. Empieza en 0.",
    "Input": "Datos que entran al programa. input() en Python.",
    "Integer": "Número entero. 42, -7, 0, etc.",
    "Interprete": "Programa que ejecuta código línea por línea.",
    "Iteración": "Cada repetición de un bucle.",
    "IDE": "Entorno de desarrollo integrado.",
    "Instance": "Objeto creado a partir de una clase.",
    
    # J
    "JSON": "JavaScript Object Notation. Formato de datos muy usado.",
    "JavaScript": "Lenguaje de programación web.",
    "JVM": "Java Virtual Machine. Ejecuta código Java.",
    "jQuery": "Biblioteca JavaScript para manipular DOM.",
    
    # K
    "Keyword": "Palabra reservada del lenguaje. if, for, def, etc.",
    "Kivy": "Framework Python para apps multiplataforma.",
    
    # L
    "Librería": "Colección de código reutilizable. Módulo.",
    "Loop": "Bucle. Estructura que repite código.",
    "Lambda": "Función anónima en Python. lambda x: x*2",
    "Localhost": "127.0.0.1. Dirección de la propia máquina.",
    "Log": "Registro de eventos del programa.",
    
    # M
    "Método": "Función que pertenece a un objeto o clase.",
    "Módulo": "Archivo Python con código reutilizable.",
    "Main": "Función principal del programa.",
    "Mutable": "Objeto que puede modificarse. Listas son mutables.",
    "Map": "Aplicar función a cada elemento de secuencia.",
    
    # N
    "Null": "Valor vacío o nulo. None en Python.",
    "npm": "Node Package Manager. Gestor de paquetes Node.js.",
    "Namespace": "Espacio de nombres para evitar conflictos.",
    "Nested": "Estructura dentro de otra. Lista de listas.",
    
    # O
    "Objeto": "Instancia de una clase con atributos y métodos.",
    "Operador": "Símbolo para operaciones. +, -, *, /, ==, etc.",
    "Output": "Datos que salen del programa. print() en Python.",
    "Open Source": "Código fuente disponible públicamente.",
    "ORM": "Object-Relational Mapping. Mapeo de objetos a bases de datos.",
    "Overload": "Sobrecarga. Múltiples versiones de una función.",
    
    # P
    "Parámetro": "Variable en definición de función.",
    "Python": "Lenguaje de programación interpretado y de alto nivel.",
    "Package": "Conjunto de módulos relacionados.",
    "Parser": "Programa que analiza texto y extrae información.",
    "Path": "Ruta a un archivo o directorio.",
    "Pipe": "|. Enviar salida de un comando a otro.",
    "Plugin": "Extensión que agrega funcionalidad.",
    "Polimorfismo": "Mismo método con comportamiento diferente en clases distintas.",
    "Prompt": "Indicador de entrada. >>> en Python.",
    "Pseudocódigo": "Descripción de algoritmo en lenguaje natural.",
    
    # Q
    "Query": "Consulta a base de datos.",
    "Queue": "Estructura FIFO (First In First Out).",
    
    # R
    "Return": "Valor que devuelve una función.",
    "Recursión": "Función que se llama a sí misma.",
    "Runtime": "Tiempo de ejecución del programa.",
    "REST": "Representational State Transfer. Estilo de API.",
    "Regex": "Expresión regular. Patrón de búsqueda de texto.",
    "RAM": "Random Access Memory. Memoria volátil.",
    "Root": "Usuario administrador en Unix/Linux.",
    "Repository": "Repositorio. Donde se guarda código Git.",
    
    # S
    "String": "Cadena de texto. 'Hola mundo'",
    "Script": "Archivo con código que se ejecuta directamente.",
    "Scope": "Ámbito donde una variable es válida.",
    "SDK": "Software Development Kit. Herramientas de desarrollo.",
    "Server": "Computadora que provee servicios a clientes.",
    "Shell": "Intérprete de comandos. Terminal.",
    "Slice": "Porción de secuencia. lista[1:4]",
    "Stack": "Estructura LIFO (Last In First Out).",
    "Syntax": "Reglas de escritura del lenguaje.",
    "SSL": "Secure Sockets Layer. Protocolo de seguridad.",
    "SQL": "Structured Query Language. Lenguaje de bases de datos.",
    
    # T
    "Terminal": "Interfaz de línea de comandos.",
    "Type": "Tipo de dato. int, str, float, etc.",
    "Try": "Bloque para capturar excepciones.",
    "Tuple": "Secuencia inmutable. (1, 2, 3)",
    "Template": "Plantilla para generar contenido.",
    "Thread": "Hilo de ejecución. Proceso ligero.",
    
    # U
    "URL": "Uniform Resource Locator. Dirección web.",
    "User": "Usuario del sistema o aplicación.",
    "Unicode": "Estándar para representar caracteres de todos los idiomas.",
    
    # V
    "Variable": "Nombre que guarda un valor.",
    "Vector": "Array unidimensional.",
    "Virtualenv": "Entorno virtual Python aislado.",
    "Version Control": "Control de versiones. Git, SVN.",
    
    # W
    "Web": "World Wide Web. Sistema de documentos enlazados.",
    "While": "Bucle que repite mientras condición sea True.",
    "Widget": "Componente de interfaz gráfica.",
    
    # X
    "XML": "eXtensible Markup Language. Formato de datos.",
    
    # Y
    "YAML": "YAML Ain't Markup Language. Formato de configuración.",
    
    # Z
    "ZIP": "Formato de archivo comprimido.",
    
    # Símbolos y operadores
    "==": "Comparación de igualdad. ¿Son iguales?",
    "!=": "Comparación de diferencia. ¿Son diferentes?",
    ">": "Mayor que.",
    "<": "Menor que.",
    ">=": "Mayor o igual que.",
    "<=": "Menor o igual que.",
    "=": "Asignación. Guardar valor en variable.",
    "+=": "Sumar y asignar. x += 1 es x = x + 1",
    "-=": "Restar y asignar. x -= 1 es x = x - 1",
    "*=": "Multiplicar y asignar.",
    "/=": "Dividir y asignar.",
    "//": "División entera. Redondea hacia abajo.",
    "%": "Módulo. Resto de división.",
    "**": "Potencia. 2**3 = 8",
    "and": "Operador lógico Y. True si ambos True.",
    "or": "Operador lógico O. True si al menos uno True.",
    "not": "Operador lógico NO. Invierte booleano.",
    "in": "Verifica pertenencia. 'a' in 'hola' → True",
    "is": "Verifica identidad de objeto.",
    "\\n": "Nueva línea en string.",
    "\\t": "Tabulación en string.",
    "\\": "Carácter de escape.",
    "#": "Comentario en Python.",
    "[]": "Lista o índice.",
    "{}": "Diccionario o conjunto.",
    "()": "Tupla o llamada a función.",
    "[:]": "Slice. Porción de secuencia.",
    
    # Conceptos avanzados
    "API REST": "API que sigue principios REST. Usa HTTP.",
    "Base de datos": "Sistema para almacenar y organizar datos.",
    "Big O": "Notación para complejidad algorítmica.",
    "Callback Hell": "Código con muchos callbacks anidados.",
    "Closure": "Función que recuerda su entorno de creación.",
    "Concurrency": "Ejecución de múltiples tareas en paralelo.",
    "CORS": "Cross-Origin Resource Sharing. Política de seguridad web.",
    "CRUD": "Create, Read, Update, Delete. Operaciones básicas.",
    "Dependency": "Librería que necesita tu proyecto.",
    "Deploy": "Poner aplicación en producción.",
    "Design Pattern": "Solución reusable a problema común.",
    "DNS": "Domain Name System. Traduce dominios a IP.",
    "Encrypted": "Cifrado. Datos convertidos a formato seguro.",
    "Endpoint": "URL de una API.",
    "Event Loop": "Bucle que maneja eventos asíncronos.",
    "Herencia": "Clase que hereda atributos de otra.",
    "JWT": "JSON Web Token. Token de autenticación.",
    "Memory Leak": "Memoria no liberada que se acumula.",
    "Microservices": "Arquitectura de servicios pequeños independientes.",
    "Middleware": "Software entre aplicación y sistema.",
    "MVC": "Model-View-Controller. Patrón de arquitectura.",
    "NoSQL": "Base de datos no relacional. MongoDB, Redis.",
    "OAuth": "Protocolo de autorización.",
    "Refactor": "Mejorar código sin cambiar su función.",
    "Responsive": "Diseño que se adapta a cualquier pantalla.",
    "SaaS": "Software as a Service. Software en la nube.",
    "SOLID": "Principios de diseño de software.",
    "SSH": "Secure Shell. Protocolo de conexión segura.",
    "SSL/TLS": "Protocolos de seguridad para web.",
    "Testing": "Pruebas de código. Unit tests, integration tests.",
    "Token": "Credencial de autenticación.",
    "WebSocket": "Protocolo de comunicación bidireccional.",
}

# ═══════════════════════════════════════════════════════════════════════════
# 💡 CONSEJOS Y ATAJOOS
# ═══════════════════════════════════════════════════════════════════════════

CONSEJOS_PRO = """
╔═════════════════════════════════════════════════════════════════╗
║                 💎 CONSEJOS DE PROGRAMADORES PRO                ║
╚═════════════════════════════════════════════════════════════════╝

📚 APRENDIZAJE:
• Lee código de otros programadores
• Practica TODOS los días, aunque sea 30 min
• No copies y pegues, escribe el código
• Aprende a leer documentación
• Los errores son tus maestros, no tus enemigos

🧠 MENTALIDAD:
• Divide problemas grandes en pequeños
• Piensa antes de codificar
• Simplicidad > Complejidad
• El código se escribe una vez, se lee muchas
• Comenta el POR QUÉ, no el QUÉ

⚡ PRODUCTIVIDAD:
• Usa un buen editor (VS Code es gratis y excelente)
• Aprende atajos de teclado
• Automatiza tareas repetitivas
• Control de versiones desde el día 1
• Haz commits pequeños y frecuentes

🐛 DEBUGGING:
• Lee los errores COMPLETOS
• print() es tu amigo
• Aísla el problema
• Busca en Stack Overflow
• Toma descansos cuando te atores

🔒 BUENAS PRÁCTICAS:
• Nombres descriptivos de variables
• Funciones que hacen UNA cosa
• Código limpio desde el inicio
• Tests para código importante
• No reinventes la rueda

"""

ATAJOS_PYTHON = """
╔═════════════════════════════════════════════════════════════════╗
║                   ⌨️ ATAJOOS DE PYTHON                          ║
╚═════════════════════════════════════════════════════════════════╝

📝 ATAJOOS DE SINTAXIS:
───────────────────────────────────────────────────────────────────
# Lista por comprensión
[ x**2 for x in range(10) ]          # [0, 1, 4, 9, 16, ...]

# Diccionario por comprensión
{ k: v for k, v in enumerate(['a', 'b', 'c']) }

# Condición en una línea
"par" if x % 2 == 0 else "impar"

# Intercambio de variables
a, b = b, a

# Desempaquetar lista
primero, *resto = [1, 2, 3, 4, 5]    # primero=1, resto=[2,3,4,5]

# Unir strings
", ".join(['a', 'b', 'c'])           # "a, b, c"

# Enumerar con índice
for i, item in enumerate(lista):
    print(f"{i}: {item}")

# Máximo/mínimo con key
max(palabras, key=len)               # Palabra más larga

# Zip de listas
for a, b in zip(lista1, lista2):
    print(a, b)

# Invertir string/lista
texto[::-1]                          # Invierte

# Verificar si es número
texto.isdigit()

# Leer archivo en una línea
texto = open('archivo.txt').read()

# Escribir archivo en una línea
open('archivo.txt', 'w').write('contenido')

# Lambda funciones
doble = lambda x: x * 2

# Map con lambda
list(map(lambda x: x**2, [1,2,3,4]))

# Filter
list(filter(lambda x: x > 5, lista))

# Any / All
any(x > 10 for x in lista)           # True si alguno cumple
all(x > 0 for x in lista)            # True si todos cumplen

"""

ATAJOS_VSCODE = """
╔═════════════════════════════════════════════════════════════════╗
║                   ⌨️ ATAJOOS DE VS CODE                         ║
╚═════════════════════════════════════════════════════════════════╝

🔥 ESENCIALES:
───────────────────────────────────────────────────────────────────
Ctrl + S                    Guardar
Ctrl + Z                    Deshacer
Ctrl + Shift + Z            Rehacer
Ctrl + C                    Copiar línea (sin selección)
Ctrl + X                    Cortar línea
Ctrl + V                    Pegar
Ctrl + A                    Seleccionar todo

🔍 NAVEGACIÓN:
───────────────────────────────────────────────────────────────────
Ctrl + P                    Abrir archivo rápido
Ctrl + Shift + P            Paleta de comandos
Ctrl + G                    Ir a línea
Ctrl + Click                Ir a definición
Ctrl + Tab                  Cambiar entre archivos
Ctrl + B                    Mostrar/ocultar sidebar

✏️ EDICIÓN:
───────────────────────────────────────────────────────────────────
Ctrl + D                    Seleccionar siguiente ocurrencia
Ctrl + Shift + K            Eliminar línea
Alt + ↑/↓                   Mover línea
Shift + Alt + ↑/↓           Duplicar línea
Ctrl + /                    Comentar/descomentar
Ctrl + Shift + [            Colapsar bloque
Ctrl + Shift + ]            Expandir bloque

🪟 MÚLTIPLES CURSORES:
───────────────────────────────────────────────────────────────────
Alt + Click                 Añadir cursor
Ctrl + Alt + ↑/↓            Cursor arriba/abajo
Ctrl + Shift + L            Seleccionar todas las ocurrencias

🔧 TERMINAL:
───────────────────────────────────────────────────────────────────
Ctrl + `                    Abrir/cerrar terminal
Ctrl + Shift + `            Nueva terminal

"""

ATAJOS_TERMINAL = """
╔═════════════════════════════════════════════════════════════════╗
║                   ⌨️ ATAJOOS DE TERMINAL                        ║
╚═════════════════════════════════════════════════════════════════╝

🔥 NAVEGACIÓN:
───────────────────────────────────────────────────────────────────
cd ..                       Subir un directorio
cd ~                        Ir al home
cd -                        Directorio anterior
pwd                         Mostrar directorio actual
ls -la                      Listar con detalles

⚡ ATAJOOS DE TECLADO:
───────────────────────────────────────────────────────────────────
Tab                         Autocompletar
Ctrl + C                    Cancelar comando
Ctrl + L                    Limpiar pantalla
Ctrl + R                    Buscar en historial
Ctrl + A                    Inicio de línea
Ctrl + E                    Fin de línea
Ctrl + U                    Borrar desde cursor al inicio
Ctrl + K                    Borrar desde cursor al final
↑ / ↓                       Historial de comandos

🔥 COMANDOS ÚTILES:
───────────────────────────────────────────────────────────────────
history                     Ver historial de comandos
!!                          Repetir último comando
!n                          Ejecutar comando n del historial
comando &                   Ejecutar en segundo plano
comando1 && comando2        Ejecutar comando2 si comando1 funciona
comando1 || comando2        Ejecutar comando2 si comando1 falla
|                           Pipe: pasar salida a otro comando
>                           Redirigir salida a archivo
>>                          Añadir salida a archivo

📝 EJEMPLOS PODEROSOS:
───────────────────────────────────────────────────────────────────
find . -name "*.py"         Buscar archivos Python
grep -r "texto" .           Buscar texto en archivos
ps aux | grep python        Procesos Python corriendo
kill -9 PID                 Matar proceso por ID
chmod +x script.sh          Hacer ejecutable
tar -xzvf archivo.tar.gz    Descomprimir tar.gz

"""

# ═══════════════════════════════════════════════════════════════════════════
# 📚 CONTENIDO DE MÓDULOS
# ═══════════════════════════════════════════════════════════════════════════

MODULOS = {
    "01: El Despertar": {
        "leccion": """╔═════════════════════════════════════════════════════════════════╗
║                    🌅 EL DESPERTAR                              ║
║                  Tu primera línea de código                     ║
╚═════════════════════════════════════════════════════════════════╝

📖 CONCEPTO: PRINT
El comando print() muestra texto en pantalla.
Es la forma más básica de comunicación con el usuario.

📝 SINTAXIS:
    print("Tu mensaje aquí")

💡 EJEMPLOS:
    print("Hola, mundo")      → Muestra: Hola, mundo
    print(42)                 → Muestra: 42
    print(2 + 2)              → Muestra: 4

🔑 REGLAS:
• El texto va entre comillas "" o ''
• Los números NO llevan comillas
• Cada print() crea una nueva línea
• Puedes imprimir cálculos matemáticos

⚡ DATO CURIOSO:
El primer programa que escribió Brian Kernighan
en 1972 fue: printf("hello, world");
Desde entonces, "Hola Mundo" es tradición.

🎮 TU MISIÓN:
Escribe un programa que muestre tu nombre de hacker.

⚡ BONUS XP: +50 XP si usas f-string
""",
        "desafio": "Crea un print que muestre: 'Soy un hacker'",
        "solucion": ["print(\"Soy un hacker\")", "print('Soy un hacker')"],
        "pista": "Usa print() con comillas dobles o simples"
    },
    
    "02: Almacenes": {
        "leccion": """╔═════════════════════════════════════════════════════════════════╗
║                    📦 ALMACENES                                 ║
║              Variables: Guardando información                   ║
╚═════════════════════════════════════════════════════════════════╝

Las variables son como cajas donde guardas información.
Piensa en ellas como contenedores con etiquetas.

📖 CONCEPTO: VARIABLES
Una variable es un nombre que guarda un valor.

📝 SINTAXIS:
    nombre_variable = valor

💡 EJEMPLOS:
    nombre = "Hacker"         → Guarda texto
    edad = 25                 → Guarda número
    altura = 1.75             → Guarda decimal
    es_hacker = True          → Guarda booleano

🔑 REGLAS:
• El nombre NO puede empezar con número
• NO puede tener espacios (usa _)
• Python distingue mayúsculas de minúsculas
• Nombre debe ser descriptivo

⚠️ ERRORES COMUNES:
    1nombre = "Error"         ❌ Empieza con número
    mi nombre = "Error"       ❌ Tiene espacio
    Nombre ≠ nombre           ⚠️ Son diferentes

⚡ BONUS XP: +30 XP por buena práctica de nombres
""",
        "desafio": "Crea una variable 'codigo' con valor 'secreto123' y muestra: Tu código es: secreto123",
        "solucion": ["codigo = 'secreto123'\nprint('Tu código es:', codigo)", "codigo = \"secreto123\"\nprint(\"Tu código es:\", codigo)"],
        "pista": "Primero crea la variable, luego úsala en print()"
    },
    
    "03: Variables": {
        "leccion": """╔═════════════════════════════════════════════════════════════════╗
║                    🔢 TIPOS DE DATOS                            ║
║              Entendiendo los datos en Python                    ║
╚═════════════════════════════════════════════════════════════════╝

Python maneja diferentes tipos de información.
Cada tipo tiene características únicas.

📖 TIPOS PRINCIPALES:

📝 STR (String) - Texto
    nombre = "Hacker"

🔢 INT (Integer) - Números enteros
    edad = 25

💯 FLOAT (Decimal) - Números con punto
    dinero = 99.99

✅ BOOL (Boolean) - Verdadero/Falso
    vivo = True

🔍 FUNCIÓN TYPE():
    type("Hola")      → <class 'str'>
    type(42)          → <class 'int'>

🔄 CONVERSIÓN:
    int("42")         → 42 (texto a número)
    str(42)           → "42" (número a texto)

⚡ BONUS XP: +40 XP por usar type() correctamente
""",
        "desafio": "Crea: nombre (str), nivel (int), y activo (bool). Muestra el tipo de cada uno.",
        "solucion": ["nombre = 'Hacker'\nnivel = 10\nactivo = True\nprint(type(nombre))\nprint(type(nivel))\nprint(type(activo))"],
        "pista": "Usa type() para mostrar el tipo"
    },
    
    "04: Condicionales": {
        "leccion": """╔═════════════════════════════════════════════════════════════════╗
║                    🔀 CONDICIONALES                             ║
║              Tomando decisiones con el código                   ║
╚═════════════════════════════════════════════════════════════════╝

Los condicionales permiten que tu programa tome decisiones.
Es el cerebro lógico de cualquier aplicación.

📖 ESTRUCTURA IF-ELSE:

    if condición:
        # código si es verdadero
    else:
        # código si es falso

💡 EJEMPLO:
    edad = 18
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

📖 IF-ELIF-ELSE:
    if nota >= 90:
        print("Excelente")
    elif nota >= 70:
        print("Aprobado")
    else:
        print("Reprobado")

🔑 OPERADORES:
    ==   Igual        !=   Diferente
    >    Mayor        <    Menor
    >=   Mayor igual  <=   Menor igual

⚡ BONUS XP: +50 XP por usar elif correctamente
""",
        "desafio": "Si rol = 'admin', mostrar 'ACCESO TOTAL'. Si no, mostrar 'ACCESO LIMITADO'",
        "solucion": ["rol = 'admin'\nif rol == 'admin':\n    print('ACCESO TOTAL')\nelse:\n    print('ACCESO LIMITADO')"],
        "pista": "Usa if con == para comparar"
    },
    
    "05: Bucles": {
        "leccion": """╔═════════════════════════════════════════════════════════════════╗
║                    🔄 BUCLES                                    ║
║              Repitiendo acciones automáticamente                ║
╚═════════════════════════════════════════════════════════════════╝

Los bucles permiten repetir código sin escribirlo múltiples veces.

📖 BUCLE FOR:
    for i in range(5):
        print(i)  # 0, 1, 2, 3, 4

    for letra in "HACKER":
        print(letra)

📖 BUCLE WHILE:
    contador = 0
    while contador < 5:
        print(contador)
        contador += 1

🛑 CONTROL:
    break    → Sale del bucle
    continue → Salta a siguiente iteración

⚡ BONUS XP: +60 XP por usar range() con paso
""",
        "desafio": "Muestra los números pares del 2 al 10 usando un bucle for",
        "solucion": ["for i in range(2, 11, 2):\n    print(i)", "for i in range(2, 11):\n    if i % 2 == 0:\n        print(i)"],
        "pista": "range(inicio, fin, paso) o usa % para verificar pares"
    },
    
    "06: Funciones": {
        "leccion": """╔═════════════════════════════════════════════════════════════════╗
║                    ⚙️ FUNCIONES                                 ║
║              Creando código reutilizable                        ║
╚═════════════════════════════════════════════════════════════════╝

Las funciones son bloques de código reutilizable.
Una vez creadas, puedes usarlas infinitas veces.

📖 SINTAXIS:
    def nombre_funcion():
        return resultado

💡 FUNCIÓN SIMPLE:
    def saludar():
        print("¡Hola!")

💡 CON PARÁMETROS:
    def saludar(nombre):
        print(f"¡Hola, {nombre}!")

💡 CON RETORNO:
    def sumar(a, b):
        return a + b

⚡ BONUS XP: +70 XP por usar return correctamente
""",
        "desafio": "Crea función 'a_fahrenheit(celsius)' que retorne (celsius * 9/5) + 32. Prueba con 0°C",
        "solucion": ["def a_fahrenheit(celsius):\n    return (celsius * 9/5) + 32\n\nprint(a_fahrenheit(0))"],
        "pista": "La fórmula es: (celsius * 9/5) + 32"
    },
    
    "07: Listas": {
        "leccion": """╔═════════════════════════════════════════════════════════════════╗
║                    📋 LISTAS                                    ║
║              Colecciones ordenadas de datos                     ║
╚═════════════════════════════════════════════════════════════════╝

Las listas guardan múltiples elementos en orden.

📖 CREAR LISTA:
    frutas = ["manzana", "banana", "cereza"]

📖 ACCEDER:
    frutas[0]       → "manzana"
    frutas[-1]      → "cereza"

📖 MODIFICAR:
    frutas.append("uva")      # Agregar
    frutas.remove("banana")   # Eliminar
    frutas.sort()             # Ordenar

⚡ BONUS XP: +50 XP por usar sort()
""",
        "desafio": "Crea lista 'lenguajes' con: Python, Java, C++, JavaScript. Agrega 'Rust', ordénala y muéstrala.",
        "solucion": ["lenguajes = ['Python', 'Java', 'C++', 'JavaScript']\nlenguajes.append('Rust')\nlenguajes.sort()\nprint(lenguajes)"],
        "pista": "Usa append() y sort()"
    },
    
    "08: Diccionarios": {
        "leccion": """╔═════════════════════════════════════════════════════════════════╗
║                    📖 DICCIONARIOS                              ║
║              Datos estructurados con claves                     ║
╚═════════════════════════════════════════════════════════════════╝

Los diccionarios guardan datos en pares clave:valor.

📖 CREAR:
    usuario = {
        "nombre": "Carlos",
        "edad": 25
    }

📖 ACCEDER:
    usuario["nombre"]       → "Carlos"
    usuario.get("edad")     → 25

📖 RECORRER:
    for clave, valor in usuario.items():
        print(f"{clave}: {valor}")

⚡ BONUS XP: +60 XP por usar items()
""",
        "desafio": "Crea diccionario 'perfil' con: nombre, nivel (int), skills (lista). Muestra cada clave-valor.",
        "solucion": ["perfil = {\n    'nombre': 'Hacker',\n    'nivel': 10,\n    'skills': ['Python', 'Linux', 'Hacking']\n}\nfor clave, valor in perfil.items():\n    print(f'{clave}: {valor}')"],
        "pista": "Usa items() para recorrer"
    },
    
    "09: Strings": {
        "leccion": """╔═════════════════════════════════════════════════════════════════╗
║                    🔤 STRINGS (TEXTO)                           ║
║              Manipulando cadenas de caracteres                  ║
╚═════════════════════════════════════════════════════════════════╝

Los strings son secuencias de caracteres.

📖 MÉTODOS IMPORTANTES:
    texto.upper()           → "HOLA"
    texto.lower()           → "hola"
    texto.strip()           → Quita espacios
    texto.replace("a","e")  → Reemplaza
    texto.split()           → Divide en lista

📖 F-STRINGS:
    nombre = "Carlos"
    print(f"Hola, {nombre}")

⚡ BONUS XP: +40 XP por combinar métodos
""",
        "desafio": "Dado texto = '  hacker python  ': quita espacios, pon mayúsculas y reemplaza 'PYTHON' por 'MASTER'",
        "solucion": ["texto = '  hacker python  '\ntexto = texto.strip().upper()\ntexto = texto.replace('PYTHON', 'MASTER')\nprint(texto)"],
        "pista": "Usa strip(), upper() y replace()"
    },
    
    "10: Operadores": {
        "leccion": """╔═════════════════════════════════════════════════════════════════╗
║                    ➕ OPERADORES                                ║
║              Herramientas de cálculo y comparación              ║
╚═════════════════════════════════════════════════════════════════╝

📖 ARITMÉTICOS:
    +    Suma          -    Resta
    *    Multiplica    /    Divide
    //   Entero        %    Residuo
    **   Potencia

📖 COMPARACIÓN:
    ==   Igual        !=   Diferente
    >    Mayor        <    Menor
    >=   Mayor igual  <=   Menor igual

📖 LÓGICOS:
    and   Y lógico
    or    O lógico
    not   No lógico

⚡ BONUS XP: +50 XP por usar ** correctamente
""",
        "desafio": "Calcula: (10 + 5) * 2 - 8 / 4 y muestra el resultado y su residuo al dividir entre 7",
        "solucion": ["resultado = (10 + 5) * 2 - 8 / 4\nprint(f'Resultado: {resultado}')\nresiduo = int(resultado) % 7\nprint(f'Residuo: {residuo}')"],
        "pista": "Usa paréntesis para ordenar operaciones"
    },
    
    "11: Debugging": {
        "leccion": """╔═════════════════════════════════════════════════════════════════╗
║                    🐛 DEBUGGING                                 ║
║              Encontrando y corrigiendo errores                  ║
╚═════════════════════════════════════════════════════════════════╝

📖 TIPOS DE ERRORES:

❌ SyntaxError      → Error de sintaxis
❌ NameError        → Variable no definida
❌ TypeError        → Tipo incorrecto
❌ ValueError       → Valor inválido
❌ IndexError       → Índice fuera de rango
❌ ZeroDivisionError → División entre cero

📖 TRY-EXCEPT:
    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        print("Error!")

⚡ BONUS XP: +80 XP por usar try/except
""",
        "desafio": "Corrige: numero = input('Dame un número: '); print(numero + 10)",
        "solucion": ["numero = input('Dame un número: ')\nnumero = int(numero)\nprint(numero + 10)", "numero = int(input('Dame un número: '))\nprint(numero + 10)"],
        "pista": "input() devuelve string, necesitas convertirlo a int"
    },
    
    "12: Retos Finales": {
        "leccion": """╔═════════════════════════════════════════════════════════════════╗
║                    🏆 RETOS FINALES                             ║
║              Poniendo a prueba todo lo aprendido                ║
╚═════════════════════════════════════════════════════════════════╝

Es hora de combinar todo lo que has aprendido.

💡 ESTRATEGIAS:
1. Lee el problema completo
2. Identifica los pasos necesarios
3. Implementa paso a paso
4. Prueba con diferentes valores

⚡ BONUS XP: +100 XP por primera solución correcta
""",
        "desafio": "Crea función 'filtrar_aprobados' que reciba lista de notas y retorne solo las >= 70. Muestra cuántos aprobaron.",
        "solucion": ["def filtrar_aprobados(notas):\n    aprobados = []\n    for nota in notas:\n        if nota >= 70:\n            aprobados.append(nota)\n    return aprobados\n\nnotas = [85, 60, 90, 45, 70, 55, 95]\naprobados = filtrar_aprobados(notas)\nprint(f'Aprobados: {len(aprobados)}')\nprint(f'Notas: {aprobados}')"],
        "pista": "Combina: función, for, if, listas, len()"
    },
    
    "13: El Desafío": {
        "leccion": """╔═════════════════════════════════════════════════════════════════╗
║                    ⚔️ EL DESAFÍO                                ║
║              Proyecto integrador de nivel medio                 ║
╚═════════════════════════════════════════════════════════════════╝

📋 PROYECTO: SISTEMA DE USUARIOS

Crea un sistema que permita:
• Registrar usuarios
• Mostrar lista de usuarios
• Actualizar nivel
• Eliminar usuario

⚡ BONUS XP: +150 XP por sistema completo
""",
        "desafio": "Crea sistema que registre 3 usuarios: Ana (5), Carlos (8), Maria (3). Sube nivel de Ana a 10 y muestra todos.",
        "solucion": ["usuarios = {}\n\nusuarios['Ana'] = {'nivel': 5}\nusuarios['Carlos'] = {'nivel': 8}\nusuarios['Maria'] = {'nivel': 3}\n\nusuarios['Ana']['nivel'] = 10\n\nfor nombre, datos in usuarios.items():\n    print(f'{nombre}: Nivel {datos[\"nivel\"]}')"],
        "pista": "Usa diccionario anidado"
    },
    
    "14: El Maestro": {
        "leccion": """╔═════════════════════════════════════════════════════════════════╗
║                    👑 EL MAESTRO                                ║
║              El desafío final de la academia                    ║
╚═════════════════════════════════════════════════════════════════╝

📋 PROYECTO FINAL: MINI-JUEGO DE COMBATE

Crea un juego donde:
• Cada jugador tiene vida y ataque
• Se atacan por turnos
• Gana el que sobreviva

⚡ BONUS XP: +200 XP por juego funcional
""",
        "desafio": "Crea 2 guerreros (vidas 100 y 80, ataques 20 y 25). Haz que peleen por turnos hasta que uno gane.",
        "solucion": ["p1_vida, p1_ataque = 100, 20\np2_vida, p2_ataque = 80, 25\n\nturno = 1\nwhile p1_vida > 0 and p2_vida > 0:\n    if turno % 2 == 1:\n        p2_vida -= p1_ataque\n        print(f'P1 ataca! P2 vida: {p2_vida}')\n    else:\n        p1_vida -= p2_ataque\n        print(f'P2 ataca! P1 vida: {p1_vida}')\n    turno += 1\n\nif p1_vida > 0:\n    print('Ganador: Jugador 1')\nelse:\n    print('Ganador: Jugador 2')"],
        "pista": "Usa while con condición de vida > 0"
    }
}

# ═══════════════════════════════════════════════════════════════════════════
# 📖 HISTORIA DE LENGUAJES
# ═══════════════════════════════════════════════════════════════════════════

HISTORIA_LENGUAJES = """╔═════════════════════════════════════════════════════════════════╗
║                📚 HISTORIA DE LA PROGRAMACIÓN                   ║
╚═════════════════════════════════════════════════════════════════╝

🕰️ LÍNEA TEMPORAL:

┌─────────────────────────────────────────────────────────────────┐
│ 1843 - ALGORITMO DE ADA LOVELACE                                 │
│   Primera programadora de la historia                            │
├─────────────────────────────────────────────────────────────────┤
│ 1957 - FORTRAN                                                   │
│   Primer lenguaje de alto nivel                                  │
├─────────────────────────────────────────────────────────────────┤
│ 1972 - C                                                         │
│   Base de Unix, Linux, Windows, macOS                           │
├─────────────────────────────────────────────────────────────────┤
│ 1991 - PYTHON                                                    │
│   Creado por Guido van Rossum                                   │
│   #1 en ciencia de datos, IA                                    │
├─────────────────────────────────────────────────────────────────┤
│ 1995 - JAVA                                                      │
│   "Write once, run anywhere"                                     │
│   Base de Android                                                │
├─────────────────────────────────────────────────────────────────┤
│ 1995 - JAVASCRIPT                                                │
│   Lenguaje de la web                                            │
│   97% de sitios web lo usan                                      │
├─────────────────────────────────────────────────────────────────┤
│ 2010 - RUST                                                      │
│   Lenguaje más amado                                            │
│   Seguridad de memoria                                          │
├─────────────────────────────────────────────────────────────────┤
│ 2015 - KOTLIN                                                    │
│   Lenguaje oficial de Android                                   │
└─────────────────────────────────────────────────────────────────┘

📊 TOP 10 LENGUAJES 2024:

1. 🥇 Python     - IA, Data Science, Web
2. 🥈 JavaScript - Web, Apps
3. 🥉 Java       - Empresarial, Android
4. 🏅 C/C++      - Sistemas, Juegos
5. 🏅 C#         - Windows, Unity
6. 🏅 Go         - Cloud, DevOps
7. 🏅 Rust       - Sistemas, Seguridad
8. 🏅 TypeScript - Web
9. 🏅 PHP        - Web
10. 🏅 Swift     - iOS

"""

# ═══════════════════════════════════════════════════════════════════════════
# 📱 GUÍA TERMUX
# ═══════════════════════════════════════════════════════════════════════════

GUIA_TERMUX = """╔═════════════════════════════════════════════════════════════════╗
║                    📱 GUÍA DE TERMUX                            ║
╚═════════════════════════════════════════════════════════════════╝

📖 ¿QUÉ ES TERMUX?
Emulador de terminal Linux para Android.
Ejecuta comandos Linux, instala paquetes, programa.

📦 INSTALACIÓN:
Descarga desde F-Droid (NO Play Store):
https://f-droid.org/packages/com.termux/

🎮 COMANDOS ESENCIALES:

📁 NAVEGACIÓN:
    pwd             → Directorio actual
    ls              → Lista archivos
    cd carpeta      → Entra a carpeta
    cd ..           → Retrocede

📦 PAQUETES:
    pkg update      → Actualiza repositorios
    pkg install X   → Instala paquete X
    pkg search X    → Busca paquete

🐍 PYTHON EN TERMUX:
    pkg install python
    python archivo.py

⚡ PERMISOS:
    termux-setup-storage

"""

# ═══════════════════════════════════════════════════════════════════════════
# 🌍 ECOSISTEMAS
# ═══════════════════════════════════════════════════════════════════════════

ECOSISTEMAS = """╔═════════════════════════════════════════════════════════════════╗
║                🌍 ECOSISTEMAS DE DESARROLLO                     ║
╚═════════════════════════════════════════════════════════════════╝

🐧 LINUX:
✅ Gratuito, open source
✅ Terminal poderosa
✅ Servidores
❌ Software profesional limitado

🪟 WINDOWS:
✅ Software comercial
✅ Visual Studio
✅ Juegos
❌ Licencias costosas

🍎 MACOS:
✅ Unix + Diseño
✅ Xcode
✅ Desarrollo iOS
❌ Hardware costoso

📱 ANDROID (Termux):
✅ Siempre contigo
✅ Linux completo
❌ Pantalla pequeña

"""

# ═══════════════════════════════════════════════════════════════════════════
# 🎨 WIDGETS PERSONALIZADOS CON EFECTOS
# ═══════════════════════════════════════════════════════════════════════════

class NeonButton(Button):
    """Botón con efecto neón brillante"""
    def __init__(self, texto="", color=NEON_CYAN, **kwargs):
        super().__init__(**kwargs)
        self.text = texto
        self.base_color = color
        self.background_color = color
        self.background_normal = ''
        self.font_size = '16sp'
        self.color = FONDO_OLED
        self.bold = True
        
        # Efectos
        self.bind(on_press=self.on_press_effect)
        self.bind(on_release=self.on_release_effect)
    
    def on_press_effect(self, instance):
        anim = Animation(background_color=(1, 1, 1, 1), duration=0.1)
        anim.start(self)
    
    def on_release_effect(self, instance):
        anim = Animation(background_color=self.base_color, duration=0.2)
        anim.start(self)


class GlitchLabel(Label):
    """Label con efecto glitch"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.original_color = self.color if hasattr(self, 'color') else NEON_CYAN
        Clock.schedule_interval(self.glitch_effect, 3.0)
    
    def glitch_effect(self, dt):
        if random.random() < 0.3:  # 30% de probabilidad
            glitch_anim = Animation(color=NEON_MAGENTA, duration=0.05)
            glitch_anim += Animation(color=NEON_CYAN, duration=0.05)
            glitch_anim += Animation(color=self.original_color, duration=0.1)
            glitch_anim.start(self)


class XPBar(ProgressBar):
    """Barra de XP con animación"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.max = 100
        self.value = 0
        self.color = NEON_GREEN
    
    def animated_set(self, value):
        anim = Animation(value=value, duration=0.5)
        anim.start(self)


# ═══════════════════════════════════════════════════════════════════════════
# 💻 TERMINAL INTERACTIVA
# ═══════════════════════════════════════════════════════════════════════════

class TerminalEmulator(BoxLayout):
    """Terminal funcional interactiva"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.history = []
        self.history_index = 0
        self.variables = {}
        self.current_dir = "/home/hacker"
        
        # Output
        self.output = TextInput(
            text='''╔═════════════════════════════════════════════════════════════════╗
║           💻 TERMINAL CODEQUEST v2.5                             ║
║           Escribe 'help' para comandos disponibles               ║
╚═════════════════════════════════════════════════════════════════╝

''',
            readonly=True,
            multiline=True,
            size_hint_y=0.85,
            background_color=FONDO_OSCURO,
            foreground_color=NEON_GREEN,
            font_name='DroidSansMono',
            font_size='13sp',
            cursor_color=NEON_GREEN
        )
        self.add_widget(self.output)
        
        # Input
        input_layout = BoxLayout(size_hint_y=0.15, spacing=5)
        
        self.prompt = Label(
            text=f"[{self.current_dir}]$ ",
            size_hint_x=0.25,
            color=NEON_CYAN,
            font_name='DroidSansMono',
            font_size='13sp'
        )
        
        self.input = TextInput(
            text='',
            multiline=False,
            size_hint_x=0.75,
            background_color=FONDO_OSCURO,
            foreground_color=NEON_GREEN,
            font_name='DroidSansMono',
            font_size='13sp',
            cursor_color=NEON_GREEN,
            hint_text='Escribe un comando...'
        )
        self.input.bind(on_text_validate=self.ejecutar_comando)
        
        input_layout.add_widget(self.prompt)
        input_layout.add_widget(self.input)
        self.add_widget(input_layout)
        
        self.mostrar("🚀 Sistema iniciado. ¡Bienvenido, Hacker!\n")
    
    def mostrar(self, texto):
        self.output.text += texto
    
    def ejecutar_comando(self, instance):
        comando = self.input.text.strip()
        self.input.text = ''
        
        if not comando:
            return
        
        self.history.append(comando)
        self.history_index = len(self.history)
        self.mostrar(f"[{self.current_dir}]$ {comando}\n")
        
        partes = comando.split()
        cmd = partes[0].lower()
        args = partes[1:] if len(partes) > 1 else []
        
        resultado = self.procesar_comando(cmd, args)
        if resultado:
            self.mostrar(resultado + "\n")
        
        self.prompt.text = f"[{self.current_dir}]$ "
    
    def procesar_comando(self, cmd, args):
        comandos = {
            'help': '''╔══════════════════════════════════════════╗
║              COMANDOS DISPONIBLES        ║
╚══════════════════════════════════════════╝
📁 NAVEGACIÓN:
  pwd           - Directorio actual
  ls            - Lista archivos
  cd [dir]      - Cambia directorio

💻 PYTHON:
  print [texto] - Imprime texto
  calc [expr]   - Calcula expresión
  var [n=v]     - Crea variable
  show          - Muestra variables

⚡ SISTEMA:
  clear         - Limpia pantalla
  neofetch      - Info del sistema
  whoami        - Tu identidad
  date          - Fecha actual
  exit          - Salir''',
            
            'pwd': lambda: self.current_dir,
            'ls': lambda: "📁 Documentos/  📁 Scripts/  📁 Proyectos/  📄 data.json  📄 readme.txt",
            'cd': lambda: self._cd(args),
            'print': lambda: ' '.join(args).strip('"\'') if args else "Uso: print [texto]",
            'calc': lambda: self._calc(args),
            'var': lambda: self._var(args),
            'show': lambda: '\n'.join([f"{k} = {v}" for k, v in self.variables.items()]) if self.variables else "No hay variables",
            'clear': self._clear,
            'neofetch': lambda: '''
    ███████████████████    
  ██                  ██    hacker@codequest
██    ████████████    ██   ─────────────────
██   ██          ██   ██   OS: CodeQuest OS 2.5
██   ██    ████  ██   ██   Kernel: Python 3.11
██   ██          ██   ██   Shell: CyberTerminal
██    ████████████    ██   Terminal: 80x24
  ██                  ██   CPU: Hacker Mind
    ███████████████████    Memory: ∞ GB
''',
            'whoami': lambda: "🧑‍💻 hacker",
            'date': lambda: time.strftime("%Y-%m-%d %H:%M:%S"),
            'python': lambda: '''Python 3.11.0 (CodeQuest Edition)
>>> Modo interactivo: print(), calc, var''',
            'exit': lambda: "👋 ¡Hasta pronto, Hacker!",
        }
        
        if cmd in comandos:
            result = comandos[cmd]
            return result() if callable(result) else result
        return f"❌ Comando no reconocido: {cmd}\nEscribe 'help' para ayuda."
    
    def _cd(self, args):
        if args:
            if args[0] == '..':
                self.current_dir = "/home/hacker"
            else:
                self.current_dir = f"{self.current_dir}/{args[0]}"
        return None
    
    def _calc(self, args):
        try:
            expr = ' '.join(args)
            permitidos = '0123456789+-*/.() %'
            if all(c in permitidos for c in expr):
                return f"= {eval(expr)}"
            return "❌ Expresión no válida"
        except:
            return "❌ Error en cálculo"
    
    def _var(self, args):
        if '=' in ' '.join(args):
            nombre, valor = ' '.join(args).split('=', 1)
            self.variables[nombre.strip()] = valor.strip().strip('"\'')
            return f"✅ Variable creada: {nombre.strip()} = {valor.strip()}"
        return "Uso: var nombre=valor"
    
    def _clear(self):
        self.output.text = ''
        return None


# ═══════════════════════════════════════════════════════════════════════════
# 📱 PANTALLAS DE LA APLICACIÓN
# ═══════════════════════════════════════════════════════════════════════════

class SplashScreen(Screen):
    """Pantalla de carga épica"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'splash'
        
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # Logo con animación
        self.logo = Label(
            text="[b]🎮 CODEQUEST[/b]",
            markup=True,
            font_size='42sp',
            color=NEON_CYAN,
            size_hint_y=0.5
        )
        layout.add_widget(self.logo)
        
        # Subtítulo
        self.subtitulo = GlitchLabel(
            text="ACADEMIA PRO DE PYTHON",
            font_size='16sp',
            color=NEON_PURPLE,
            size_hint_y=0.15
        )
        layout.add_widget(self.subtitulo)
        
        # Barra de progreso
        self.progress = XPBar(size_hint_y=0.1)
        layout.add_widget(self.progress)
        
        # Estado
        self.status = Label(
            text="⚡ Iniciando sistema...",
            font_size='14sp',
            color=NEON_GREEN,
            size_hint_y=0.1
        )
        layout.add_widget(self.status)
        
        # Versión
        version = Label(
            text="v2.5 ULTIMATE",
            font_size='12sp',
            color=NEON_YELLOW,
            size_hint_y=0.15
        )
        layout.add_widget(version)
        
        self.add_widget(layout)
        
        # Animación de carga
        Clock.schedule_once(self.animar_inicio, 0.5)
    
    def animar_inicio(self, dt):
        estados = [
            (20, "⚡ Cargando módulos..."),
            (40, "💻 Preparando terminal..."),
            (60, "📖 Cargando lecciones..."),
            (80, "🎮 Configurando sistema XP..."),
            (100, "✨ ¡Listo para hackear!")
        ]
        
        for i, (valor, texto) in enumerate(estados):
            Clock.schedule_once(lambda dt, v=valor, t=texto: self.actualizar(v, t), (i + 1) * 0.3)
        
        Clock.schedule_once(lambda dt: self.ir_menu(), 2.0)
    
    def actualizar(self, valor, texto):
        self.progress.animated_set(valor)
        self.status.text = texto
    
    def ir_menu(self):
        self.manager.current = 'menu'


class MenuScreen(Screen):
    """Menú principal con sistema XP"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'menu'
        self.store = JsonStore('codequest_xp.json')
        
        self.layout = BoxLayout(orientation='vertical', padding=15, spacing=8)
        self.add_widget(self.layout)
        
        Clock.schedule_once(self.cargar_menu, 0.1)
    
    def cargar_menu(self, dt):
        self.layout.clear_widgets()
        
        # Calcular XP total
        xp_total = 0
        modulos_completados = []
        try:
            for key in self.store.keys():
                if key.startswith('modulo_'):
                    data = self.store.get(key)
                    if data.get('completado'):
                        modulos_completados.append(key)
                        xp_total += data.get('xp', 0)
        except:
            pass
        
        # Calcular nivel
        nivel = calcular_nivel(xp_total)
        nivel_data = NIVELES[nivel]
        progreso, necesario, siguiente = xp_para_siguiente_nivel(xp_total)
        
        # === HEADER CON XP ===
        header = BoxLayout(size_hint_y=0.18, spacing=10)
        
        # Info de nivel
        info_box = BoxLayout(orientation='vertical', size_hint_x=0.55)
        
        titulo = Label(
            text=f"{nivel_data['icono']} [b]CODEQUEST[/b]",
            markup=True,
            font_size='26sp',
            color=NEON_CYAN
        )
        
        rango = Label(
            text=f"[color={get_color_from_hex('#ffffff')}]Rango: [/color][color={nivel_data['color']}]{nivel_data['nombre']}[/color]",
            markup=True,
            font_size='14sp'
        )
        
        info_box.add_widget(titulo)
        info_box.add_widget(rango)
        
        # Barra de XP
        xp_box = BoxLayout(orientation='vertical', size_hint_x=0.45)
        
        xp_label = Label(
            text=f"⭐ {xp_total} XP",
            font_size='20sp',
            color=NEON_YELLOW
        )
        
        if necesario > 0:
            progress = XPBar(max=necesario, value=progreso)
            xp_box.add_widget(xp_label)
            xp_box.add_widget(progress)
        else:
            max_label = Label(
                text="👑 NIVEL MÁXIMO",
                font_size='14sp',
                color=NEON_WHITE
            )
            xp_box.add_widget(xp_label)
            xp_box.add_widget(max_label)
        
        header.add_widget(info_box)
        header.add_widget(xp_box)
        self.layout.add_widget(header)
        
        # === ESTADÍSTICAS ===
        stats = BoxLayout(size_hint_y=0.08, spacing=5)
        
        mod_label = Label(
            text=f"📚 {len(modulos_completados)}/14 Módulos",
            font_size='12sp',
            color=NEON_GREEN
        )
        
        xp_label2 = Label(
            text=f"⭐ {xp_total} XP Total",
            font_size='12sp',
            color=NEON_YELLOW
        )
        
        nivel_label = Label(
            text=f"🏆 Nivel {nivel}",
            font_size='12sp',
            color=nivel_data['color']
        )
        
        stats.add_widget(mod_label)
        stats.add_widget(xp_label2)
        stats.add_widget(nivel_label)
        self.layout.add_widget(stats)
        
        # === SECCIÓN DE RECURSOS ===
        recursos_label = Label(
            text="━━━━━━━ RECURSOS Y HERRAMIENTAS ━━━━━━━",
            size_hint_y=0.05,
            color=NEON_PURPLE,
            font_size='11sp'
        )
        self.layout.add_widget(recursos_label)
        
        recursos = BoxLayout(size_hint_y=0.1, spacing=5)
        
        btn_glosario = NeonButton(texto="📖 Glosario", color=NEON_PURPLE, size_hint_x=0.25)
        btn_glosario.bind(on_release=lambda x: self.ir_a('glosario'))
        
        btn_consejos = NeonButton(texto="💡 Consejos", color=NEON_ORANGE, size_hint_x=0.25)
        btn_consejos.bind(on_release=lambda x: self.ir_a('consejos'))
        
        btn_atajos = NeonButton(texto="⌨️ Atajos", color=NEON_PINK, size_hint_x=0.25)
        btn_atajos.bind(on_release=lambda x: self.ir_a('atajos'))
        
        btn_terminal = NeonButton(texto="💻 Terminal", color=NEON_GREEN, size_hint_x=0.25)
        btn_terminal.bind(on_release=lambda x: self.ir_a('terminal'))
        
        recursos.add_widget(btn_glosario)
        recursos.add_widget(btn_consejos)
        recursos.add_widget(btn_atajos)
        recursos.add_widget(btn_terminal)
        self.layout.add_widget(recursos)
        
        # === SECCIÓN DE HISTORIA ===
        historia_btns = BoxLayout(size_hint_y=0.08, spacing=5)
        
        btn_historia_py = NeonButton(texto="📚 Historia Python", color=NEON_BLUE, size_hint_x=0.33)
        btn_historia_py.bind(on_release=lambda x: self.ir_a('historia'))
        
        btn_termux = NeonButton(texto="📱 Guía Termux", color=NEON_ORANGE, size_hint_x=0.33)
        btn_termux.bind(on_release=lambda x: self.ir_a('termux'))
        
        btn_ecosistemas = NeonButton(texto="🌍 Ecosistemas", color=NEON_YELLOW, size_hint_x=0.34)
        btn_ecosistemas.bind(on_release=lambda x: self.ir_a('ecosistemas'))
        
        historia_btns.add_widget(btn_historia_py)
        historia_btns.add_widget(btn_termux)
        historia_btns.add_widget(btn_ecosistemas)
        self.layout.add_widget(historia_btns)
        
        # === MÓDULOS ===
        separador = Label(
            text="━━━━━━━ MÓDULOS DE APRENDIZAJE ━━━━━━━",
            size_hint_y=0.05,
            color=NEON_CYAN,
            font_size='11sp'
        )
        self.layout.add_widget(separador)
        
        scroll = ScrollView()
        grid = BoxLayout(orientation='vertical', size_hint_y=None, spacing=6)
        grid.bind(minimum_height=grid.setter('height'))
        
        modulos_nombres = list(MODULOS.keys())
        
        for nombre in modulos_nombres:
            key = f"modulo_{nombre.split(':')[0]}"
            hecho = key in [f"modulo_{m.split(':')[0]}" for m in modulos_completados]
            xp_modulo = XP_POR_MODULO.get(nombre, 100)
            
            color = NEON_GREEN if hecho else NEON_CYAN
            
            btn = NeonButton(
                texto=f"{'✓ ' if hecho else '○ '}{nombre} (+{xp_modulo} XP)",
                color=color,
                size_hint_y=None,
                height=55
            )
            btn.bind(on_release=lambda x, n=nombre: self.ir_a_modulo(n))
            grid.add_widget(btn)
        
        scroll.add_widget(grid)
        self.layout.add_widget(scroll)
    
    def ir_a(self, pantalla):
        self.manager.current = pantalla
    
    def ir_a_modulo(self, titulo):
        self.manager.get_screen('leccion').cargar_modulo(titulo)
        self.manager.current = 'leccion'


class GlosarioScreen(Screen):
    """Pantalla de glosario completo"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'glosario'
        
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Header
        header = BoxLayout(size_hint_y=0.1)
        titulo = Label(
            text="[b]📖 GLOSARIO COMPLETO (200+ Términos)[/b]",
            markup=True,
            font_size='20sp',
            color=NEON_PURPLE
        )
        header.add_widget(titulo)
        layout.add_widget(header)
        
        # Buscador
        buscador = BoxLayout(size_hint_y=0.08, spacing=5)
        self.search_input = TextInput(
            hint_text="🔍 Buscar término...",
            size_hint_x=0.8,
            background_color=FONDO_INPUT,
            foreground_color=NEON_WHITE,
            cursor_color=NEON_CYAN
        )
        self.search_input.bind(text=self.filtrar_glosario)
        
        btn_search = NeonButton(texto="🔍", color=NEON_PURPLE, size_hint_x=0.2)
        buscador.add_widget(self.search_input)
        buscador.add_widget(btn_search)
        layout.add_widget(buscador)
        
        # Contenido
        self.scroll = ScrollView()
        self.contenido = Label(
            text=self.formatear_glosario(GLOSARIO),
            markup=True,
            font_size='12sp',
            color=NEON_WHITE,
            size_hint_y=None,
            halign='left',
            valign='top'
        )
        self.contenido.bind(size=self.contenido.setter('text_size'))
        self.contenido.bind(texture_size=self.contenido.setter('size'))
        self.scroll.add_widget(self.contenido)
        layout.add_widget(self.scroll)
        
        # Botón volver
        btn_volver = NeonButton(texto="← VOLVER AL MENÚ", color=NEON_PURPLE, size_hint_y=0.08)
        btn_volver.bind(on_release=lambda x: self.volver())
        layout.add_widget(btn_volver)
        
        self.add_widget(layout)
    
    def formatear_glosario(self, glosario):
        texto = ""
        for termino, definicion in sorted(glosario.items()):
            texto += f"[color={NEON_CYAN}][b]{termino}[/b][/color]\n"
            texto += f"  {definicion}\n\n"
        return texto
    
    def filtrar_glosario(self, instance, texto):
        if texto:
            filtrado = {k: v for k, v in GLOSARIO.items() if texto.lower() in k.lower()}
        else:
            filtrado = GLOSARIO
        self.contenido.text = self.formatear_glosario(filtrado)
    
    def volver(self):
        self.manager.get_screen('menu').cargar_menu(0)
        self.manager.current = 'menu'


class ConsejosScreen(Screen):
    """Pantalla de consejos pro"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'consejos'
        
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Header
        header = BoxLayout(size_hint_y=0.1)
        titulo = Label(
            text="[b]💡 CONSEJOS DE PROGRAMADORES PRO[/b]",
            markup=True,
            font_size='18sp',
            color=NEON_ORANGE
        )
        header.add_widget(titulo)
        layout.add_widget(header)
        
        # Contenido
        scroll = ScrollView()
        contenido = Label(
            text=CONSEJOS_PRO,
            markup=True,
            font_size='12sp',
            color=NEON_WHITE,
            size_hint_y=None,
            halign='left',
            valign='top'
        )
        contenido.bind(size=contenido.setter('text_size'))
        contenido.bind(texture_size=contenido.setter('size'))
        scroll.add_widget(contenido)
        layout.add_widget(scroll)
        
        # Botón volver
        btn_volver = NeonButton(texto="← VOLVER AL MENÚ", color=NEON_ORANGE, size_hint_y=0.08)
        btn_volver.bind(on_release=lambda x: self.volver())
        layout.add_widget(btn_volver)
        
        self.add_widget(layout)
    
    def volver(self):
        self.manager.get_screen('menu').cargar_menu(0)
        self.manager.current = 'menu'


class AtajosScreen(Screen):
    """Pantalla de atajos"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'atajos'
        
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Header
        header = BoxLayout(size_hint_y=0.08)
        titulo = Label(
            text="[b]⌨️ ATAJOOS DE TECLADO[/b]",
            markup=True,
            font_size='18sp',
            color=NEON_PINK
        )
        header.add_widget(titulo)
        layout.add_widget(header)
        
        # Tabs
        tabs = BoxLayout(size_hint_y=0.08, spacing=5)
        
        self.btn_py = NeonButton(texto="Python", color=NEON_CYAN, size_hint_x=0.33)
        self.btn_py.bind(on_release=lambda x: self.mostrar('python'))
        
        self.btn_vs = NeonButton(texto="VS Code", color=NEON_PURPLE, size_hint_x=0.33)
        self.btn_vs.bind(on_release=lambda x: self.mostrar('vscode'))
        
        self.btn_term = NeonButton(texto="Terminal", color=NEON_GREEN, size_hint_x=0.34)
        self.btn_term.bind(on_release=lambda x: self.mostrar('terminal'))
        
        tabs.add_widget(self.btn_py)
        tabs.add_widget(self.btn_vs)
        tabs.add_widget(self.btn_term)
        layout.add_widget(tabs)
        
        # Contenido
        self.scroll = ScrollView()
        self.contenido = Label(
            text=ATAJOS_PYTHON,
            markup=True,
            font_size='11sp',
            color=NEON_WHITE,
            size_hint_y=None,
            halign='left',
            valign='top'
        )
        self.contenido.bind(size=self.contenido.setter('text_size'))
        self.contenido.bind(texture_size=self.contenido.setter('size'))
        self.scroll.add_widget(self.contenido)
        layout.add_widget(self.scroll)
        
        # Botón volver
        btn_volver = NeonButton(texto="← VOLVER AL MENÚ", color=NEON_PINK, size_hint_y=0.08)
        btn_volver.bind(on_release=lambda x: self.volver())
        layout.add_widget(btn_volver)
        
        self.add_widget(layout)
        
        # Mostrar Python por defecto
        self.mostrar('python')
    
    def mostrar(self, tipo):
        contenidos = {
            'python': ATAJOS_PYTHON,
            'vscode': ATAJOS_VSCODE,
            'terminal': ATAJOS_TERMINAL
        }
        self.contenido.text = contenidos.get(tipo, ATAJOS_PYTHON)
    
    def volver(self):
        self.manager.get_screen('menu').cargar_menu(0)
        self.manager.current = 'menu'


class TerminalScreen(Screen):
    """Pantalla de terminal"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'terminal'
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=5)
        
        # Header
        header = BoxLayout(size_hint_y=0.08)
        titulo = Label(
            text="[b]💻 TERMINAL INTERACTIVA[/b]",
            markup=True,
            font_size='18sp',
            color=NEON_GREEN
        )
        header.add_widget(titulo)
        layout.add_widget(header)
        
        # Terminal
        self.terminal = TerminalEmulator(size_hint_y=0.84)
        layout.add_widget(self.terminal)
        
        # Botón volver
        btn_volver = NeonButton(texto="← VOLVER AL MENÚ", color=NEON_GREEN, size_hint_y=0.08)
        btn_volver.bind(on_release=lambda x: self.volver())
        layout.add_widget(btn_volver)
        
        self.add_widget(layout)
    
    def volver(self):
        self.manager.get_screen('menu').cargar_menu(0)
        self.manager.current = 'menu'


class HistoriaScreen(Screen):
    """Pantalla de historia"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'historia'
        
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        header = BoxLayout(size_hint_y=0.1)
        titulo = Label(
            text="[b]📚 HISTORIA DE LA PROGRAMACIÓN[/b]",
            markup=True,
            font_size='18sp',
            color=NEON_BLUE
        )
        header.add_widget(titulo)
        layout.add_widget(header)
        
        scroll = ScrollView()
        contenido = Label(
            text=HISTORIA_LENGUAJES,
            markup=True,
            font_size='11sp',
            color=NEON_WHITE,
            size_hint_y=None,
            halign='left',
            valign='top'
        )
        contenido.bind(size=contenido.setter('text_size'))
        contenido.bind(texture_size=contenido.setter('size'))
        scroll.add_widget(contenido)
        layout.add_widget(scroll)
        
        btn_volver = NeonButton(texto="← VOLVER AL MENÚ", color=NEON_BLUE, size_hint_y=0.08)
        btn_volver.bind(on_release=lambda x: self.volver())
        layout.add_widget(btn_volver)
        
        self.add_widget(layout)
    
    def volver(self):
        self.manager.get_screen('menu').cargar_menu(0)
        self.manager.current = 'menu'


class TermuxScreen(Screen):
    """Pantalla de guía Termux"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'termux'
        
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        header = BoxLayout(size_hint_y=0.1)
        titulo = Label(
            text="[b]📱 GUÍA DE TERMUX[/b]",
            markup=True,
            font_size='18sp',
            color=NEON_ORANGE
        )
        header.add_widget(titulo)
        layout.add_widget(header)
        
        scroll = ScrollView()
        contenido = Label(
            text=GUIA_TERMUX,
            markup=True,
            font_size='12sp',
            color=NEON_WHITE,
            size_hint_y=None,
            halign='left',
            valign='top'
        )
        contenido.bind(size=contenido.setter('text_size'))
        contenido.bind(texture_size=contenido.setter('size'))
        scroll.add_widget(contenido)
        layout.add_widget(scroll)
        
        btn_volver = NeonButton(texto="← VOLVER AL MENÚ", color=NEON_ORANGE, size_hint_y=0.08)
        btn_volver.bind(on_release=lambda x: self.volver())
        layout.add_widget(btn_volver)
        
        self.add_widget(layout)
    
    def volver(self):
        self.manager.get_screen('menu').cargar_menu(0)
        self.manager.current = 'menu'


class EcosistemasScreen(Screen):
    """Pantalla de ecosistemas"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'ecosistemas'
        
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        header = BoxLayout(size_hint_y=0.1)
        titulo = Label(
            text="[b]🌍 ECOSISTEMAS DE DESARROLLO[/b]",
            markup=True,
            font_size='18sp',
            color=NEON_YELLOW
        )
        header.add_widget(titulo)
        layout.add_widget(header)
        
        scroll = ScrollView()
        contenido = Label(
            text=ECOSISTEMAS,
            markup=True,
            font_size='12sp',
            color=NEON_WHITE,
            size_hint_y=None,
            halign='left',
            valign='top'
        )
        contenido.bind(size=contenido.setter('text_size'))
        contenido.bind(texture_size=contenido.setter('size'))
        scroll.add_widget(contenido)
        layout.add_widget(scroll)
        
        btn_volver = NeonButton(texto="← VOLVER AL MENÚ", color=NEON_YELLOW, size_hint_y=0.08)
        btn_volver.bind(on_release=lambda x: self.volver())
        layout.add_widget(btn_volver)
        
        self.add_widget(layout)
    
    def volver(self):
        self.manager.get_screen('menu').cargar_menu(0)
        self.manager.current = 'menu'


class LeccionScreen(Screen):
    """Pantalla de lección interactiva con historia"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'leccion'
        self.store = JsonStore('codequest_xp.json')
        self.modulo_actual = None
        
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=8)
        self.add_widget(self.layout)
    
    def cargar_modulo(self, titulo):
        self.modulo_actual = titulo
        self.layout.clear_widgets()
        
        modulo = MODULOS.get(titulo, {})
        historia_key = f"modulo_{titulo.split(':')[0].replace('0', '')}"
        historia_key = historia_key.replace('modulo_1', 'modulo_1').replace('modulo_2', 'modulo_2')
        historia = HISTORIA.get(historia_key, HISTORIA.get('intro'))
        
        # Header
        header = BoxLayout(size_hint_y=0.08, spacing=10)
        
        btn_volver = NeonButton(texto="←", color=NEON_RED, size_hint_x=0.12)
        btn_volver.bind(on_release=lambda x: self.volver_menu())
        
        titulo_label = Label(
            text=f"[b]{titulo}[/b]",
            markup=True,
            font_size='16sp',
            color=NEON_CYAN
        )
        
        xp_label = Label(
            text=f"+{XP_POR_MODULO.get(titulo, 100)} XP",
            font_size='14sp',
            color=NEON_YELLOW
        )
        
        header.add_widget(btn_volver)
        header.add_widget(titulo_label)
        header.add_widget(xp_label)
        self.layout.add_widget(header)
        
        # Tabs
        tabs = BoxLayout(size_hint_y=0.08, spacing=5)
        
        self.btn_historia = NeonButton(texto="🎬 HISTORIA", color=NEON_MAGENTA, size_hint_x=0.33)
        self.btn_historia.bind(on_release=lambda x: self.mostrar_historia(historia, modulo))
        
        self.btn_leccion = NeonButton(texto="📖 LECCIÓN", color=NEON_CYAN, size_hint_x=0.33)
        self.btn_leccion.bind(on_release=lambda x: self.mostrar_leccion(modulo))
        
        self.btn_desafio = NeonButton(texto="💻 DESAFÍO", color=NEON_GREEN, size_hint_x=0.34)
        self.btn_desafio.bind(on_release=lambda x: self.mostrar_desafio(modulo))
        
        tabs.add_widget(self.btn_historia)
        tabs.add_widget(self.btn_leccion)
        tabs.add_widget(self.btn_desafio)
        self.layout.add_widget(tabs)
        
        # Área de contenido
        self.contenido_area = BoxLayout(size_hint_y=0.84)
        self.layout.add_widget(self.contenido_area)
        
        # Mostrar historia por defecto
        self.mostrar_historia(historia, modulo)
    
    def mostrar_historia(self, historia, modulo):
        self.btn_historia.color = NEON_MAGENTA
        self.btn_leccion.color = NEON_PURPLE
        self.btn_desafio.color = NEON_PURPLE
        
        self.contenido_area.clear_widgets()
        
        scroll = ScrollView()
        contenido = Label(
            text=historia.get('texto', ''),
            markup=True,
            font_size='12sp',
            color=NEON_WHITE,
            size_hint_y=None,
            halign='left',
            valign='top'
        )
        contenido.bind(size=contenido.setter('text_size'))
        contenido.bind(texture_size=contenido.setter('size'))
        scroll.add_widget(contenido)
        self.contenido_area.add_widget(scroll)
    
    def mostrar_leccion(self, modulo):
        self.btn_historia.color = NEON_PURPLE
        self.btn_leccion.color = NEON_CYAN
        self.btn_desafio.color = NEON_PURPLE
        
        self.contenido_area.clear_widgets()
        
        scroll = ScrollView()
        contenido = Label(
            text=modulo.get('leccion', 'Contenido no disponible'),
            markup=True,
            font_size='12sp',
            color=NEON_WHITE,
            size_hint_y=None,
            halign='left',
            valign='top'
        )
        contenido.bind(size=contenido.setter('text_size'))
        contenido.bind(texture_size=contenido.setter('size'))
        scroll.add_widget(contenido)
        self.contenido_area.add_widget(scroll)
    
    def mostrar_desafio(self, modulo):
        self.btn_historia.color = NEON_PURPLE
        self.btn_leccion.color = NEON_PURPLE
        self.btn_desafio.color = NEON_GREEN
        
        self.contenido_area.clear_widgets()
        
        desafio_layout = BoxLayout(orientation='vertical', spacing=8)
        
        # Descripción
        desafio = modulo.get('desafio', '')
        descripcion = Label(
            text=f"[b]📝 DESAFÍO:[/b]\n{desafio}",
            markup=True,
            font_size='14sp',
            color=NEON_YELLOW,
            size_hint_y=0.12,
            halign='left'
        )
        descripcion.bind(size=descripcion.setter('text_size'))
        desafio_layout.add_widget(descripcion)
        
        # Pista
        pista = modulo.get('pista', '')
        pista_label = Label(
            text=f"[color=888888]💡 Pista: {pista}[/color]",
            markup=True,
            font_size='11sp',
            size_hint_y=0.06
        )
        desafio_layout.add_widget(pista_label)
        
        # Editor
        self.code_input = TextInput(
            text='',
            multiline=True,
            size_hint_y=0.55,
            background_color=FONDO_OSCURO,
            foreground_color=NEON_GREEN,
            font_name='DroidSansMono',
            font_size='13sp',
            cursor_color=NEON_GREEN,
            hint_text='💻 Escribe tu código aquí...'
        )
        desafio_layout.add_widget(self.code_input)
        
        # Botones
        btn_layout = BoxLayout(size_hint_y=0.12, spacing=10)
        
        btn_verificar = NeonButton(texto="✓ VERIFICAR", color=NEON_GREEN)
        btn_verificar.bind(on_release=lambda x: self.verificar_codigo(modulo))
        
        btn_solucion = NeonButton(texto="👁 SOLUCIÓN", color=NEON_PURPLE)
        btn_solucion.bind(on_release=lambda x: self.mostrar_solucion(modulo))
        
        btn_layout.add_widget(btn_verificar)
        btn_layout.add_widget(btn_solucion)
        desafio_layout.add_widget(btn_layout)
        
        # Resultado
        self.resultado = Label(
            text="",
            markup=True,
            font_size='14sp',
            size_hint_y=0.08
        )
        desafio_layout.add_widget(self.resultado)
        
        self.contenido_area.add_widget(desafio_layout)
    
    def verificar_codigo(self, modulo):
        codigo = self.code_input.text.strip()
        soluciones = modulo.get('solucion', [])
        xp_modulo = XP_POR_MODULO.get(self.modulo_actual, 100)
        
        if not codigo:
            self.resultado.text = "[color=ff3366]❌ Escribe código para verificar[/color]"
            return
        
        # Verificar solución
        es_correcto = False
        for solucion in soluciones:
            codigo_limpio = codigo.replace(' ', '').replace('\n', '').lower()
            solucion_limpia = solucion.replace(' ', '').replace('\n', '').lower()
            if codigo_limpio == solucion_limpia or solucion_limpia in codigo_limpio:
                es_correcto = True
                break
        
        if es_correcto:
            self.resultado.text = f"[color=00ff88]✓ ¡CORRECTO! +{xp_modulo} XP[/color]"
            
            # Guardar progreso
            if self.modulo_actual:
                key = f"modulo_{self.modulo_actual.split(':')[0]}"
                try:
                    self.store.put(key, completado=True, xp=xp_modulo)
                except:
                    pass
            
            # Volver después de 2 segundos
            Clock.schedule_once(lambda dt: self.volver_menu(), 2)
        else:
            self.resultado.text = "[color=ff3366]❌ Incorrecto. Revisa tu código.[/color]"
    
    def mostrar_solucion(self, modulo):
        soluciones = modulo.get('solucion', [])
        if soluciones:
            popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
            
            popup_layout.add_widget(Label(
                text="[b]💡 SOLUCIÓN[/b]",
                markup=True,
                font_size='16sp',
                color=NEON_PURPLE,
                size_hint_y=0.15
            ))
            
            codigo = TextInput(
                text=soluciones[0],
                readonly=True,
                multiline=True,
                size_hint_y=0.7,
                background_color=FONDO_OSCURO,
                foreground_color=NEON_GREEN,
                font_name='DroidSansMono',
                font_size='12sp'
            )
            popup_layout.add_widget(codigo)
            
            cerrar = NeonButton(texto="CERRAR", color=NEON_PURPLE, size_hint_y=0.15)
            popup_layout.add_widget(cerrar)
            
            popup = Popup(
                title='',
                content=popup_layout,
                size_hint=(0.9, 0.7),
                background=FONDO_OLED,
                separator_color=NEON_PURPLE
            )
            cerrar.bind(on_release=popup.dismiss)
            popup.open()
    
    def volver_menu(self):
        self.manager.get_screen('menu').cargar_menu(0)
        self.manager.current = 'menu'


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 APLICACIÓN PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════════

class CodeQuestApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition(duration=0.25))
        
        # Agregar todas las pantallas
        sm.add_widget(SplashScreen())
        sm.add_widget(MenuScreen())
        sm.add_widget(LeccionScreen())
        sm.add_widget(GlosarioScreen())
        sm.add_widget(ConsejosScreen())
        sm.add_widget(AtajosScreen())
        sm.add_widget(TerminalScreen())
        sm.add_widget(HistoriaScreen())
        sm.add_widget(TermuxScreen())
        sm.add_widget(EcosistemasScreen())
        
        return sm
    
    def on_pause(self):
        return True


# ═══════════════════════════════════════════════════════════════════════════
# ▶️ PUNTO DE ENTRADA
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    CodeQuestApp().run()
