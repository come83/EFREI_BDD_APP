import plotly.graph_objs as go
import plotly.offline as pyo
import pandas as pd
import plotly.express as px




def r1(cursor):
    # Répartition des apprentis par spécialité et par sexe
    query = """
    SELECT s.libelle_specialite, COUNT(*) as total, 
        SUM(CASE WHEN a.sexe = 'Féminin' THEN 1 ELSE 0 END) as nb_femmes, 
        SUM(CASE WHEN a.sexe = 'Masculin' THEN 1 ELSE 0 END) as nb_hommes, 
        ROUND(SUM(CASE WHEN a.sexe = 'Féminin' THEN 1 ELSE 0 END) / CAST(COUNT(*) AS DECIMAL(10,2)) * 100, 2) as pct_femmes, 
        ROUND(SUM(CASE WHEN a.sexe = 'Masculin' THEN 1 ELSE 0 END) / CAST(COUNT(*) AS DECIMAL(10,2)) * 100, 2) as pct_hommes, 
        ROUND(AVG(COALESCE(a.age_jeune_decembre, 0)), 2) as age_moyen 
    FROM Specialite s 
    JOIN Diplome d ON d.id_specialite = s.id_specialite 
    JOIN Apprenti a ON a.id_diplome = d.id_diplome 
    GROUP BY s.libelle_specialite 
    ORDER BY total DESC LIMIT 10;
    """

    cursor.execute(query)
    results = cursor.fetchall()

    data = [
        go.Bar(x=[r["libelle_specialite"] for r in results],
               y=[r["total"] for r in results], name='Total'),
        go.Bar(x=[r["libelle_specialite"] for r in results], y=[
               r["nb_femmes"] for r in results], name='Femmes'),
        go.Bar(x=[r["libelle_specialite"] for r in results], y=[
               r["nb_hommes"] for r in results], name='Hommes')
    ]

    layout = go.Layout(title='Répartition des apprentis par spécialité et par sexe',
                       xaxis=dict(title='Spécialité'), yaxis=dict(title='Nombre d\'apprentis'))

    fig = go.Figure(data=data, layout=layout)

    pyo.plot(fig)


def r2(cursor):
    # Âge moyen des apprentis par spécialité
    query = "SELECT s.libelle_specialite_com, AVG(a.age_jeune_decembre) AS age_moyen FROM Specialite s JOIN Diplome d ON s.id_specialite = d.id_specialite JOIN Apprenti a ON a.id_diplome = d.id_diplome GROUP BY s.libelle_specialite_com ORDER BY age_moyen DESC;"
    cursor.execute(query)
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=['libelle_specialite_com', 'age_moyen'])
    fig = px.line(df, x="libelle_specialite_com", y="age_moyen",
                  title='Âge moyen des apprentis par spécialité')
    fig.show()


def r3(cursor):
    # Nombre d’entreprise par département
    query = "SELECT depart_entreprise, COUNT(*) AS nombre_entreprises FROM Entreprise GROUP BY depart_entreprise ORDER BY nombre_entreprises DESC LIMIT 10;"
    cursor.execute(query)
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=[
                      'depart_entreprise', 'nombre_entreprises'])
    fig = px.pie(df, values='nombre_entreprises', names='depart_entreprise')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.show()


def r4(cursor):
    # Nombre d’apprentis par ville
    query = """SELECT Ecole.libelle_ville_site, COUNT(Apprenti.id_apprenti) AS nb_apprentis
        FROM Ecole
        JOIN Diplome ON Ecole.id_ecole = Diplome.id_ecole
        JOIN Apprenti ON Diplome.id_diplome = Apprenti.id_diplome
        GROUP BY Ecole.libelle_ville_site
        ORDER BY nb_apprentis DESC;
        """
    cursor.execute(query)
    results = cursor.fetchall()

    df = pd.DataFrame(results, columns=['libelle_ville_site', 'nb_apprentis'])
    fig = px.line(df, x="libelle_ville_site", y="nb_apprentis",
                  title="Nombre d'apprentis par ville")
    fig.show()


def r5(cursor):
    # Nombre d’apprentis et répartition HF en fonction du diplôme 

    query = """SELECT d.libelle_diplome,
       COUNT(CASE WHEN a.sexe = 'Masculin' THEN 1 ELSE NULL END) as nb_hommes,
       COUNT(CASE WHEN a.sexe = 'Féminin' THEN 1 ELSE NULL END) as nb_femmes,
       COUNT(a.id_apprenti) as total_apprentis,
       CONCAT(ROUND(COUNT(CASE WHEN a.sexe = 'Masculin' THEN 1 ELSE NULL END) / COUNT(a.id_apprenti) * 100, 2), '%') as pourcentage_hommes,
       CONCAT(ROUND(COUNT(CASE WHEN a.sexe = 'Féminin' THEN 1 ELSE NULL END) / COUNT(a.id_apprenti) * 100, 2), '%') as pourcentage_femmes
        FROM Diplome d
        JOIN Apprenti a ON a.id_diplome = d.id_diplome
        GROUP BY d.libelle_diplome
        ORDER BY total_apprentis DESC;
        """

    cursor.execute(query)
    results = cursor.fetchall()

    data = [
        go.Bar(x=[r["libelle_diplome"] for r in results], y=[
               r["total_apprentis"] for r in results], name='Total'),
        go.Bar(x=[r["libelle_diplome"] for r in results], y=[
               r["nb_femmes"] for r in results], name='Femmes'),
        go.Bar(x=[r["libelle_diplome"] for r in results], y=[
               r["nb_hommes"] for r in results], name='Hommes')
    ]

    layout = go.Layout(title='Répartition des apprentis par diplôme et par sexe',
                       xaxis=dict(title='Diplôme'), yaxis=dict(title='Nombre d\'apprentis'))

    fig = go.Figure(data=data, layout=layout)

    pyo.plot(fig)





