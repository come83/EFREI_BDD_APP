from __init__ import connectToDB, insert_values
from plot import r1, r2, r3, r4, r5

if __name__ == "__main__":

    connection, cursor = connectToDB()

    # Assurez vous que la base de donnée est créée (script.sql)
    # Modifier la fonction __init__.py/connectToDB() en fonction de vos crédentials
    # Assurez vous de télécharger le dataset au format json à la racine du projet et de le renommer all.json
    # Commentez la prochaine ligne si la base est déjà remplie
    insert_values(cursor)

    # r1-5 permettent de tracer le résultat des requêtes avec plotly
    connection.commit()

    r1(cursor)
    r2(cursor)
    r3(cursor)
    r4(cursor)
    r5(cursor)

    cursor.close()
    connection.close()
