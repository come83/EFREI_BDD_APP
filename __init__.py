import pymysql
from sql_commands import create_tables, insert_values
from requestsAndPlot import r1, connect
import plotly.graph_objects as go
import json

def connectToDB(): 
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='alternance',
    cursorclass=pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()  
    return connection, cursor  


def insert_values(cursor): 
    with open('all.json') as f:
        data = json.load(f)

    k = 0
    # Insertion des données dans la table Organisme
    for i in data:
        print(k)

        id_og = i['fields']['id_og']
        libelle_og = i['fields']['libelle_og']
        cursor.execute("INSERT INTO Organisme (id_og, libelle_organisme) VALUES (%s, %s);", 
                    (id_og, libelle_og))


        cursor.execute('''SET @id_organisme := LAST_INSERT_ID();''')

    # Insertion des données dans la table CFA
        id_etab = i['fields']['id_etab']
        nom_complet_cfa = i['fields']['nom_complet_cfa']
        cursor.execute('''
        INSERT INTO CFA 
        (id_etab, nom_complet_cfa, id_organisme) 
        VALUES (%s, %s, @id_organisme);''',
                    (id_etab, nom_complet_cfa))

        cursor.execute('''SET @id_cfa := LAST_INSERT_ID();''')


    # Insertion des données dans la table Ecole
        duree_formation_mois = i['fields']['duree_formation_mois']
        annee_formation = i['fields']['annee_formation']
        id_siteformation = i['fields']['id_siteformation']
        libelle_lien_cfa = i['fields']['libelle_lien_cfa']
        nom_site_formation = i['fields']['nom_site_formation']
        adresse1_site = i['fields']['adresse1_site']
        code_postal_site = i['fields']['code_postal_site']
        libelle_ville_site = i['fields']['libelle_ville_site']
        

        cursor.execute("INSERT INTO Ecole (duree_formation_mois, annee_formation, id_siteformation, libelle_lien_cfa, nom_site_formation, adresse1_site, code_postal_site, libelle_ville_site) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",(duree_formation_mois, annee_formation, id_siteformation, libelle_lien_cfa, nom_site_formation,adresse1_site, code_postal_site, libelle_ville_site))
        
        cursor.execute('''SET @id_ecole := LAST_INSERT_ID();''')

        # Insertion des données dans la table Entreprise
        code_naf_entreprise = i['fields'].get('code_naf_entreprise')
        depart_entreprise = i['fields'].get('depart_entreprise','')
        code_insee_entreprise = i['fields'].get('code_insee_entreprise','')
        cursor.execute('''
        INSERT INTO Entreprise 
            (code_naf_entreprise, depart_entreprise, code_insee_entreprise) 
            VALUES (%s, %s, %s);''',
                        (code_naf_entreprise, depart_entreprise, code_insee_entreprise))
    
        cursor.execute('''SET @id_entreprise := LAST_INSERT_ID();''')

        # Insertion des données dans la table Specialite
        code_groupe_specialite = i['fields']['code_groupe_specialite']
        libelle_specialite_com = i['fields']['libelle_specialite_com']
        libelle_specialite = i['fields']['libelle_specialite']
        cursor.execute('''
        INSERT INTO Specialite 
            (code_groupe_specialite, libelle_specialite_com, libelle_specialite) 
            VALUES (%s, %s, %s);''',
                        (code_groupe_specialite, libelle_specialite_com, libelle_specialite)
        )
        
        cursor.execute('''SET @id_specialite := LAST_INSERT_ID();''')


        # Insertion des données dans la table Diplome
        diplome = i['fields'].get('diplome','')
        libelle_diplome = i['fields']['libelle_diplome']
        type_diplome = i['fields']['type_diplome']
        cursor.execute('''
        INSERT INTO Diplome 
            (diplome, libelle_diplome, type_diplome, id_specialite, id_ecole)
            VALUES (%s, %s, %s, @id_specialite, @id_ecole);''',
                        (diplome, libelle_diplome, type_diplome)
        )
        cursor.execute('''SET @id_diplome := LAST_INSERT_ID();''')

        # Insertion des données dans la table Apprenti

        sexe  = i['fields']['sexe']
        age_jeune_decembre  = i['fields']['age_jeune_decembre']
        handicap_oui_non_vide = i['fields'].get('handicap_oui_non_vide','')
        libelle_qualite = i['fields']['libelle_qualite']
        libelle_ville_jeune = i['fields'].get('libelle_ville_jeune','')
        libelle_pcs_parent = i['fields']['libelle_pcs_parent']
        code_postal_jeune  = i['fields'].get('code_postal_jeune')
        libelle_nationalite = i['fields']['libelle_nationalite']
        libelle_origine_prec_cfa = i['fields']['libelle_origine_prec_cfa']
        libelle_origine_annee_prec = i['fields']['libelle_origine_annee_prec']
        cursor.execute('''
        INSERT INTO Apprenti
            (sexe, age_jeune_decembre, handicap_oui_non_vide, libelle_qualite,
            libelle_ville_jeune, libelle_pcs_parent, code_postal_jeune, libelle_nationalite,
            libelle_origine_prec_cfa, libelle_origine_annee_prec,
              id_diplome, id_entreprise)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, @id_diplome, @id_entreprise);''',(sexe, age_jeune_decembre, handicap_oui_non_vide, libelle_qualite, 
               libelle_ville_jeune, libelle_pcs_parent, code_postal_jeune, libelle_nationalite,
               libelle_origine_prec_cfa, libelle_origine_annee_prec)
        )

        cursor.execute('''SET @id_apprenti := LAST_INSERT_ID();''')


        # Insertion des données dans la table Ecole_CFA_Apprenti

        cursor.execute('''
        INSERT INTO Ecole_CFA_Apprenti (id_ecole, id_cfa, id_apprenti)
        VALUES (@id_ecole, @id_cfa, @id_apprenti);''')

  
        k += 1

