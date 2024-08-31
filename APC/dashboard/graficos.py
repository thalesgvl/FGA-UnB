import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


# leitura do dados do dataFrame
data = pd.read_csv('https://raw.githubusercontent.com/thalesgvl/FGA-UnB/main/APC/dashboard/medalhapaises.txt')
df = pd.DataFrame(data)
dados = df.values.tolist()


def cria_grafico_wm(edicoes_olimpicas):
    # Verifica qual estação foi escolhida e calcula as medalhas
    if edicoes_olimpicas == 'Verão':
        df['Medalhas'] = df['summer_total']
    elif edicoes_olimpicas == 'Inverno':
        df['Medalhas'] = df['winter_total']
    else:  # Todas
        df['Medalhas'] = df['summer_total'] + df['winter_total']

    # Crie o gráfico do total de medalhas
    fig = px.choropleth(
        df,
        locations='countries ',
        locationmode='country names',
        color='Medalhas',
        hover_name='countries ',
        color_continuous_scale=px.colors.sequential.Peach,
        title=f'Distribuição de Medalhas - {edicoes_olimpicas}'
    )

    return fig


fig_verao = cria_grafico_wm('Verão')
fig_inverno = cria_grafico_wm('Inverno')
fig_todas = cria_grafico_wm('Todas')

# prepara uma lista para receber os valores de *continentes, *medalhas de ouro, *prata e *bronze
continente = []

# seleciona lista de continentes
for coluna in dados:
    if coluna not in continente:
        continente.append(coluna[-1])  # coluna de continentes
# remove os valores repetidos da lista
continente = list(dict.fromkeys(continente))



def cria_grafico_continente(edicoes_olimpicas):
    ouros = [0, 0, 0, 0, 0, 0, 0, 0]
    pratas = [0, 0, 0, 0, 0, 0, 0, 0]
    bronzes = [0, 0, 0, 0, 0, 0, 0, 0]

    # ['Inverno', 'Verão', 'Todas']
    if edicoes_olimpicas == "Todas":
        id_ouro = -5
        id_prata = -4
        id_bronze = -3

    if edicoes_olimpicas == "Verão":
        id_ouro = -15
        id_prata = -14
        id_bronze = -13

    if edicoes_olimpicas == "Inverno":
        id_ouro = -10
        id_prata = -9
        id_bronze = -8

    for coluna_continente in dados:
        if coluna_continente[-1] == continente[0]:
            ouros[0] = ouros[0] + coluna_continente[id_ouro]
            pratas[0] = pratas[0] + coluna_continente[id_prata]
            bronzes[0] = bronzes[0] + coluna_continente[id_bronze]

        if coluna_continente[-1] == continente[1]:
            ouros[1] = ouros[1] + coluna_continente[id_ouro]
            pratas[1] = pratas[1] + coluna_continente[id_prata]
            bronzes[1] = bronzes[1] + coluna_continente[id_bronze]

        if coluna_continente[-1] == continente[2]:
            ouros[2] = ouros[2] + coluna_continente[id_ouro]
            pratas[2] = pratas[2] + coluna_continente[id_prata]
            bronzes[2] = bronzes[2] + coluna_continente[id_bronze]

        if coluna_continente[-1] == continente[3]:
            ouros[3] = ouros[3] + coluna_continente[id_ouro]
            pratas[3] = pratas[3] + coluna_continente[id_prata]
            bronzes[3] = bronzes[3] + coluna_continente[id_bronze]

        if coluna_continente[-1] == continente[4]:
            ouros[4] = ouros[4] + coluna_continente[id_ouro]
            pratas[4] = pratas[4] + coluna_continente[id_prata]
            bronzes[4] = bronzes[4] + coluna_continente[id_bronze]

        if coluna_continente[-1] == continente[5]:
            ouros[5] = ouros[5] + coluna_continente[id_ouro]
            pratas[5] = pratas[5] + coluna_continente[id_prata]
            bronzes[5] = bronzes[5] + coluna_continente[id_bronze]

        if coluna_continente[-1] == continente[6]:
            ouros[6] = ouros[6] + coluna_continente[id_ouro]
            pratas[6] = pratas[6] + coluna_continente[id_prata]
            bronzes[6] = bronzes[6] + coluna_continente[id_bronze]

        if coluna_continente[-1] == continente[7]:
            ouros[7] = ouros[7] + coluna_continente[id_ouro]
            pratas[7] = pratas[7] + coluna_continente[id_prata]
            bronzes[7] = bronzes[7] + coluna_continente[id_bronze]
    # print(" ------ ")

    # define o formato do gráfico
    fig = px.bar(template="plotly_white", barmode='group')
    # adiciona cada barra do gráfico

    fig.add_trace(go.Bar(x=continente, y=pratas, name='Medalhas de prata',
                         marker_color='#BBBFC9', text=pratas, texttemplate='%{text:.2s}', textposition='outside'))
    fig.add_trace(go.Bar(x=continente, y=ouros, name='Medalhas de ouro', marker_color='#FFDF00',
                         text=ouros, texttemplate='%{text:.2s}', textposition='outside'))
    fig.add_trace(go.Bar(x=continente, y=bronzes, name='Medalhas de bronze',
                         marker_color='#FFA366', text=bronzes, texttemplate='%{text:.2s}', textposition='outside'))

    # edita a aparência do gráfico
    fig.add_layout_image(
        x=0.25,
        sizex=4500,
        y=4590,
        sizey=4500,
        xref="x",
        yref="y",
        opacity=0.3,
        layer="below",
        source="https://cdn-icons-png.flaticon.com/512/523/523676.png"  # imagem das olimpíadas
    )
    fig.update_layout(
        title='Continentes e suas medalhas olímpicas',
        xaxis_tickfont_size=14,
        legend=dict(
            x=0.87, y=0.5
        ),
        barmode='group',
        bargroupgap=0.1  # espaço entre as barras do mesmo continente
    )


    return fig


# cria_grafico_continente('Inverno')
# cria_grafico_continente('Verão')

def cria_grafico_pizza(edicao_olimpica):
    # criar listas
    paises = []
    valores = []
    estrutura = []

    #############VARIÁVEIS
    listsummertot = []
    listsummern = []
    listwintertot = []
    listwintern = []
    estrutura2 = []
    estrutura3 = []

    def seleciona_valor(indice_estrutura):  # buscando os valores de medalha relacionado a um pais
        return indice_estrutura[1]

    def seleciona_valor2(indice_estrutura):
        return indice_estrutura[1]

    def seleciona_valor3(indice_estrutura):
        return indice_estrutura[1]

    if edicao_olimpica == 'Todas':

        for coluna in dados:
            pais_valor = []  # lista que armazena o pais e o valor da repetição da coluna
            pais_valor.append(coluna[0])  # coluna de paises
            pais_valor.append(coluna[-2])  # coluna de valores totais
            estrutura.append(pais_valor)  # lista de lista para armazenar pais e valor de todas iteraçoes
            # para ordenar baseado no parametro valor mantendo a conexão com o n
            # e retorna o valor de medalhas como um criterio de ordenaçao

        estrutura.sort(reverse=True,
                       key=seleciona_valor)  # ordenando de forma decrescente atraves do atributo valor_total da lista

        for i in range(15):  # 15 paises e 1 se5 valores
            paises.append(estrutura[i][0])  # agrupando todos os paises
            valores.append(estrutura[i][1])  # agrupando todos os valores de medalha

        grafico = px.pie(template="plotly_white", values=valores, names=paises,
                         title='15 países que mais conquistaram medalhas em todas as edições das Olimpíadas', hole=.2, color_discrete_sequence=px.colors.sequential.RdBu)

    ############### GRAFICO DE OLIMIPADAS DE VERÃO - SUMMERTOT
    if edicao_olimpica == 'Verão':

        for coluna in dados:
            pais_valor2 = []
            pais_valor2.append(coluna[0])
            pais_valor2.append(coluna[6])
            estrutura2.append(pais_valor2)

        estrutura2.sort(reverse=True, key=seleciona_valor2)

        for i in range(15):
            listsummern.append(estrutura2[i][0])
            listsummertot.append(estrutura2[i][1])
        grafico = px.pie(df, values=listsummertot, names=listsummern,
                         hole=.2, color_discrete_sequence=px.colors.sequential.solar,
                         title='15 países que mais conquistaram medalhas em edições de Verão das Olimpíadas')

    ############### GRAFICO DE OLIMIPADAS DE INVERNO - SUMMERTOT
    if edicao_olimpica == 'Inverno':
        for coluna in dados:
            pais_valor3 = []
            pais_valor3.append(coluna[0])
            pais_valor3.append(coluna[11])
            estrutura3.append(pais_valor3)

        estrutura3.sort(reverse=True, key=seleciona_valor3)

        for i in range(15):
            listwintern.append(estrutura3[i][0])
            listwintertot.append(estrutura3[i][1])

        grafico = px.pie(df, values=listwintertot, names=listwintern,
                         hole=.2, color_discrete_sequence=px.colors.sequential.ice,
                         title='15 países que mais conquistaram medalhas em edições de Inverno das Olimpíadas')

    return grafico


opcoes_grafico_pizza = ['Inverno', 'Verão', 'Todas']
