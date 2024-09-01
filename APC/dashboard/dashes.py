from dash import Dash, dcc, html, Output, Input
import graficos as gr


colors = {
    'background': '#FFFFFF',  # Cor de fundo geral
    'text': '#000000'
}

# cria gráficos iniciais
fig1 = gr.cria_grafico_pizza("Verão")
fig2 = gr.cria_grafico_continente("Verão")
fig3 = gr.cria_grafico_wm("Verão")
# INÍCIO DO DASH
app = Dash(__name__)

app.layout = html.Div(style={'backgroundColor': colors['background'], 'height': '100vh'}, children=[
    html.H1(
        children='Análise de Medalhas Olímpicas',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Visualize a distribuição de medalhas olímpicas por continente, países e o total de medalhas por país.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.RadioItems(
        options=[
            {'label': 'Verão', 'value': 'Verão'},
            {'label': 'Inverno', 'value': 'Inverno'},
            {'label': 'Todas', 'value': 'Todas'},
        ],
        value='Verão',
        id='edicao_olimpicas',
        style={'color': colors['text']}
    ),
    dcc.Graph(
        id='grafico_continente',
        figure=fig2
    ),
    dcc.RadioItems(
        options=[
            {'label': 'Verão', 'value': 'Verão'},
            {'label': 'Inverno', 'value': 'Inverno'},
            {'label': 'Todas', 'value': 'Todas'}
        ],
        value='Verão',
        id='summ_wint',
        style={'color': colors['text']}
    ),
    dcc.Graph(
        id='grafico_setor',
        figure=fig1
    ),
    dcc.RadioItems(
        options=[
            {'label': 'Verão', 'value': 'Verão'},
            {'label': 'Inverno', 'value': 'Inverno'},
            {'label': 'Todas', 'value': 'Todas'}
        ],
        value='Verão',
        id='mapa_edicao',
        style={'color': colors['text']}

    ),
    dcc.Graph(
        id='grafico_mapa',
        figure=fig3
    ),
    
])

@app.callback(
    Output('grafico_continente', 'figure'),
    [Input('edicao_olimpicas', 'value')]
)
def update_grafico_continente(value):
    return gr.cria_grafico_continente(value)

@app.callback(
    Output('grafico_setor', 'figure'),
    [Input('summ_wint', 'value')]
)
def update_grafico_pizza(value):
    return gr.cria_grafico_pizza(value)

@app.callback(
    Output('grafico_mapa', 'figure'),
    [Input('mapa_edicao', 'value')]
)
def update_grafico_mapa(value):
    return gr.cria_grafico_wm(value)

if __name__ == '__main__':
    app.run_server(debug=False)