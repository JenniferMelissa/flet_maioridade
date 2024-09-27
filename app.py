#Programacao Orientada a Eventos
#voce tem uma tela (front end) e nessa tela tem eventos que acontecem (eventos, clique,digitar, passar o mouse em cima de um elemento)
#voce aciona o evento e quando acionado, esse evento chama funcao ou metodo que foi programado anteriormente

#importar biblioteca grafica 
import flet as ft

#funcoes que serao chamdas para algum evento precisamos criar dentro da main

#funcao principal
def main (page: ft.Page):
    #acao ao evento on_change (on_change: muda em tempo real, quando digitamos)
    def acao(e): #coloca a letra 'e' de evento, se colocar outra letra nao vai funcionar
        result.value = texto.value
        page.update()

    #configuracao da janela
    page.title      = 'Meu Flet App' #titulo da pagina web
    page.scroll     = 'adaptive' #tela se adapta no celular, computador
    page.theme_mode = ft.ThemeMode.LIGHT #deixa o fundo da pagina branco

    #declaracao de variaveis
    texto = ft.TextField(label='Digite aqui um texto',on_change=acao) #caixa de texto
    result = ft.Text(size=30) #string, tipo o print

    #conteudo da janela
    page.add(
        texto,
        result
    )

    #atualizacao do app
    page.update()

#executa aplicacao
ft.app(main)
