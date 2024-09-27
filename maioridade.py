import flet as ft

def main(page: ft.Page):
    #evento
    def acao(e):
        verificacao  = 'é maior de idade.' if int(idade.value) >= 18 else 'é menor de idade.'
        result.value = f'{nome.value} {verificacao}'

        nome.value   = ''  #zera os valores
        idade.value  = ''  #zera os valores

        page.update() #sem esse page.update() nao funciona


    page.title      = 'Maioridade'
    page.scroll     = 'adaptive'
    page.theme_mode = ft.ThemeMode.LIGHT

    nome   = ft.TextField(label='Nome') #label = legenda da caixa de texto
    idade  = ft.TextField(label='Idade',suffix_text='anos',on_submit=acao) #suffix_text: aparece o texto  no final que voce escolheu apos o usuario digitar sua idade, ex: 25 'anos'
                                                                          #on_submit: faz com que ao clicar a tecla enter funcione para calcular a maioridade
    result = ft.Text(size=30)

    page.add(
         #Linha(row): ajuda a posicionar os elementos na tela
         #cada row voce esta adicionando uma linha 
        ft.Row(
            [ft.Text('Maioridade',size=40,weight='bold')],
            alignment=ft.MainAxisAlignment.CENTER #ajuda a centralizar os elementos
        ),
        ft.Row( #entrada de dados
            [nome],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row( #entrada de dados
            [idade], 
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row( #botao
            [ft.ElevatedButton('Calcular maioridade',on_click=acao)],  #evento acontece no botao, quando o usuario clicar no botao, vai acontecer uma acao de calcular a maioridade 
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row( #saida de dados
            [result], 
            alignment=ft.MainAxisAlignment.CENTER
        )
       
    )

    page.update()

ft.app(main)