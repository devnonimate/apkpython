# pip install kivy
#pip install buildozer
#buildozer init
#buildozer -v android debug

#title = ContadorApp
#package.name = contador
#package.domain = com.exemplo
#requirements = python3, kivy
#https://chatgpt.com/share/672f5811-738c-8008-8597-6d72200f9b49


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class ContadorApp(App):
    def build(self):
        # Criação do layout principal
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Label para mostrar o valor do contador
        self.contador_label = Label(text="0", font_size=50)
        layout.add_widget(self.contador_label)
        
        # Botão para incrementar o contador
        botao = Button(text="Incrementar", font_size=30, size_hint=(1, 0.5))
        botao.bind(on_press=self.incrementar_contador)
        layout.add_widget(botao)
        
        return layout

    def incrementar_contador(self, instance):
        # Incrementa o valor e atualiza a Label
        valor_atual = int(self.contador_label.text)
        valor_atual += 1
        self.contador_label.text = str(valor_atual)


if __name__ == "__main__":
    ContadorApp().run()
