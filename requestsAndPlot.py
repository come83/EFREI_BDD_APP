import plotly.graph_objects as go
import pymysql 
from flask import render_template


def connect():
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='alternance',
    cursorclass=pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()  

    return cursor

def endConnection():
    connection.commit()
    connection.close()

def r1():
    command = '''SELECT s.libelle_specialite, COUNT(*) AS nombre_etudiants FROM Diplome d JOIN Specialite s ON s.id_specialite = d.id_specialite JOIN Apprenti a ON a.id_diplome = d.id_diplome GROUP BY s.libelle_specialite;'''

    cursor = connect()
    cursor.execute(command)


    rows = cursor.fetchall()

    x_data = [row['libelle_specialite'] for row in rows]  # get values of 'libelle_specialite'
    y_data = [row['nombre_etudiants'] for row in rows]  # get values of 'nombre_etudiants'

    # create the plot with Plotly
    fig = go.Figure(data=go.Scatter(x=x_data, y=y_data, mode='markers'))

    # get the HTML of the plot
    graph_html = fig.to_html(full_html=False)



    # obtenir le HTML du graphique
    graph_html = fig.to_html(full_html=False)#

    return render_template("index.html", graph_html=graph_html)
