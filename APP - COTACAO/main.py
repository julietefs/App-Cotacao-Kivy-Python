from kivy.app import App
import requests
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MeuAplicativo(App):

    def build(self):
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(Button(text=f"Dólar R${self.pegar_cotacao('USD')}", font_size=30))
        layout.add_widget(Button(text=f"Boliviano R${self.pegar_cotacao('BOB')}", font_size=30))
        layout.add_widget(Button(text=f"Euro R${self.pegar_cotacao('EUR')}", font_size=30))
        layout.add_widget(Button(text=f"Peso Chileno R${self.pegar_cotacao('CLP')}", font_size=30))
        return layout    

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao

MeuAplicativo().run()