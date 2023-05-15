import sqlite3
connexion = sqlite3.connect("basededonnees.db")
connexion.close()
curseur_sql = connexion.cursor()  # Récupération d'un curseur
curseur_sql.execute('''CREATE TABLE IF NOT EXISTS score(
    id INTEGRER PRIMARY KEY AUPINCREMENT UNIQUE,
    Nom TEXT,
    score INT
)''')

curseur
