# .venv\Scripts\activate
# flet -r flet_front.py


import flet as ft
import webbrowser
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from flet.matplotlib_chart import MatplotlibChart


matplotlib.use("svg")
def main(page: ft.Page):

    #Название страницы, тема, выравнивание по центру
    page.title = 'Главная'
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    
    
    #Dataframe
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    fig, ax = plt.subplots()
    ax.plot(df['col1'], df['col2'], label="Выпускаемая продукция")
    ax.plot([1,1], [1,2], label="Остановки")
    ax.legend()

    
    fig.tight_layout()
    chart = MatplotlibChart(fig, expand=True)
    #Смена темы
    def Change_Theme(e):
        page.theme_mode='light' if page.theme_mode == 'dark' else 'dark'
        page.update()
    
    def AtlasCopco_web1(e):
        webbrowser.open('http://192.168.20.20/')
    def AtlasCopco_web2(e):
        webbrowser.open('http://192.168.20.21/')
    def AtlasCopco_web3(e):
        webbrowser.open('http://192.168.20.22/')

   
    #Домашняя страница
    AtlasCopco=ft.Row([
            ft.ElevatedButton(text="Compressor 1", on_click=AtlasCopco_web1) ,   
            ft.ElevatedButton(text="Compressor 2", on_click=AtlasCopco_web2)  ,
            ft.ElevatedButton(text="Compressor 3", on_click=AtlasCopco_web3)  
        ],
        alignment = ft.MainAxisAlignment.CENTER
        ) 
    
    
    
    #Страница таймлайна
    graph=ft.Row([
            ft.Icon(ft.icons.BACK_HAND)
        ],
        alignment = ft.MainAxisAlignment.CENTER 
        )

    
    #Домашняя страница при запуске
    page.add(AtlasCopco)



    #Апп бар верхний
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.MEDICATION),
        leading_width=100,
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.SUNNY, on_click=Change_Theme),
            ft.IconButton(ft.icons.LOGIN),
            
        ],
    )



    #Навигация и содержание страниц
    def navigate(e):
        index = page.navigation_bar.selected_index
        page.clean()
        
        if index == 0: page.add(AtlasCopco)
        elif index == 1: page.add(chart, graph)



    #Нижняя паннель навигации
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME, label='Home'),
            ft.NavigationDestination(icon=ft.icons.AUTO_GRAPH, label='KAHLE'),
        ], on_change=navigate
    )
    page.update()
ft.app(target=main)#, view=ft.AppView.WEB_BROWSER)