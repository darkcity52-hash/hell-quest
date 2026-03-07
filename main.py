import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

# Forzamos un color de fondo para saber que funciona
Window.clearcolor = (0.1, 0.1, 0.1, 1)

class CodeQuestApp(App):
    def build(self):
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # Etiqueta de bienvenida
        self.label = Label(
            text="¡CodeQuest está Vivo!",
            font_size='32sp',
            color=(0, 1, 0, 1)  # Verde neón
        )
        
        # Botón de prueba
        btn = Button(
            text="Presiona para iniciar Hell Quest",
            size_hint=(1, 0.2),
            background_color=(0.2, 0.6, 1, 1)
        )
        btn.bind(on_press=self.on_click)
        
        layout.add_widget(self.label)
        layout.add_widget(btn)
        
        return layout

    def on_click(self, instance):
        self.label.text = "¡Motor Kivy Funcionando!"
        print("El botón fue presionado con éxito")

if __name__ == "__main__":
    CodeQuestApp().run()
