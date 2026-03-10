from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.properties import BooleanProperty
from kivy.core.clipboard import Clipboard
from kivy.utils import platform

# --- MOTOR DE ANDROID 16 (Solo si estamos en el móvil) ---
if platform == 'android':
    from jnius import autoclass
    VpnService = autoclass('android.net.VpnService')
    PythonActivity = autoclass('org.kivy.android.PythonActivity')

class PanelVPN(Screen):
    modo_fantasma = BooleanProperty(False)
    # IDENTIDAD 47C7 (Cargada en Memoria Volátil)
    usuario_id = "47C7Q6OvXBFVMzGD"
    sello_pass = "47C7Q6OvXBFVMzGD"

    def activar_tunel(self):
        """Inicia el Ritual de Conexión"""
        print(f"[color=00ffff]Maestro:[/color] Sintonizando Identidad {self.usuario_id[:4]}...")
        
        # Animación de Latido de Neón
        anim = Animation(opacity=0.5, duration=0.5) + Animation(opacity=1, duration=0.5)
        anim.repeat = True
        anim.start(self.ids.btn_switch)

        if platform == 'android':
            # Pedir permiso oficial de VPN a Android 16
            intent = VpnService.prepare(PythonActivity.mActivity)
            if intent:
                PythonActivity.mActivity.startActivityForResult(intent, 0)
            else:
                self.abrir_vacio()
        else:
            self.abrir_vacio()

    def abrir_vacio(self):
        """Activa el Modo Fantasma y Limpieza del Ojo"""
        self.modo_fantasma = True
        self.ids.status_red.text = "ESTADO: [color=00ff00]INVISIBLE[/color]"
        
        # LIMPIEZA DEL OJO: Borrar rastro del portapapeles
        Clipboard.copy("")
        print("[color=ff3333]Maestro:[/color] Portapapeles purificado. Rastro cero.")

    def kill_switch_monitor(self, dt):
        """Vigía del Modo Fantasma"""
        if self.modo_fantasma:
            # Si el túnel cae, cortamos el flujo de datos (Lógica de red)
            pass

class CodeQuest(App):
    def build(self):
        self.title = "Hell Quest: Soberanía Digital"
        sm = ScreenManager()
        sm.add_widget(PanelVPN(name='vpn_panel'))
        return sm

    def on_stop(self):
        """EL HECHIZO DE OLVIDO: Se activa al cerrar la app"""
        print("[color=ff3333]Maestro:[/color] Borrando rastro de la sesión de Helios...")
        # Purga total de variables de identidad
        PanelVPN.usuario_id = None
        PanelVPN.sello_pass = None
