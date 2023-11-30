from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px
import matplotlib as plt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot', methods=['GET', 'POST'])
def plot():
    if request.method == 'POST':
        selected_plot = request.form['plot_type']
    else:
        selected_plot = 'scatter_matplotlib'  # Valeur par défaut

    # Charger le dataset
    df = pd.read_csv('data/SkillCraft1_Dataset.csv')

    if selected_plot == 'TotalHours':
        fig = px.scatter(df, x='TotalHours', y='LeagueIndex',
                         labels={'TotalHours': 'Total Hours', 'LeagueIndex': 'League Index'})
        fig.update_layout(title='Scatter Plot of Total Hours vs League Index (Plotly)')
        graph_json = fig.to_json()
    elif selected_plot == 'APM':
        # Créer un graphique Plotly
        fig = px.scatter(df, x='APM', y='LeagueIndex', labels={'APM': 'APM', 'LeagueIndex': 'League Index'})
        fig.update_layout(title='Scatter Plot of APM vs League Index (Plotly)')
        graph_json = fig.to_json()
    elif selected_plot == 'NumberOfPACs':
        fig = px.scatter(df, x='NumberOfPACs', y='LeagueIndex',
                         labels={'NumberOfPACs': 'Number of PACs', 'LeagueIndex': 'League Index'})
        fig.update_layout(title='Scatter Plot of Number of PACs vs League Index (Plotly)')
        graph_json = fig.to_json()
    elif selected_plot == 'GapBetweenPACs':
        fig = px.scatter(df, x='GapBetweenPACs', y='LeagueIndex',
                         labels={'GapBetweenPACs': 'Gap Between PACs', 'LeagueIndex': 'League Index'})
        fig.update_layout(title='Scatter Plot of Gap Between PACs vs League Index (Plotly)')
        graph_json = fig.to_json()
    elif selected_plot == 'SelectByHotkeys':
        fig = px.scatter(df, x='SelectByHotkeys', y='LeagueIndex',
                         labels={'SelectByHotkeys': 'Select By Hotkeys', 'LeagueIndex': 'League Index'})
        fig.update_layout(title='Scatter Plot of Select By Hotkeys vs League Index (Plotly)')
        graph_json = fig.to_json()
    elif selected_plot == 'Age':
        fig = px.scatter(df, x='Age', y='LeagueIndex', labels={'Age': 'Age', 'LeagueIndex': 'League Index'})
        fig.update_layout(title='Scatter Plot of Age vs League Index (Plotly)')
        graph_json = fig.to_json()
    else:
        return render_template('error.html', message='Invalid plot type')

    return render_template('graph.html', graph_json=graph_json)


if __name__ == '__main__':
    app.run(debug=True)

