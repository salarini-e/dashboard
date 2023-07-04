from dash import Dash, html, dash_table
import pandas as pd

# Lê os dados do arquivo CSV e converte para um DataFrame do pandas
df = pd.read_csv('precos_teclados.csv', encoding='UTF-8', delimiter=';')

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Lista de dados'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10)
])

if __name__ == '__main__':
    app.run(debug=True)

# Ver depois: https://dash-bootstrap-components.opensource.faculty.ai/