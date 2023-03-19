# Projet SQL EFREI L3 RS1

* Ce repo permet de créer la BDD, insérer les valeurs depuis le dataset dans la BDD et d'afficher certaines requêtes avec plotly. 

```
git clone https://github.com/come83/EFREI_BDD_APP.git
cd EFREI_BDD_APP
pip install -r requirements.txt
```

* Assurez vous que la base de donnée est créée (script.sql)
* Modifier la fonction __init__.py/connectToDB() en fonction de vos crédentials 
* Assurez vous de télécharger le <a href="https://www.data.gouv.fr/en/datasets/apprentissage-effectifs-detailles-2008-2009/"> dataset </a> au format json à la racine du projet et de le renommer all.json

* Si la BDD est déjà remplie, commentez " insert_values(cursor)" de main.py (ligne 12)

* Executer main.py 

