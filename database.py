import mysql.connector


class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connexion réussie à la base de données")
        except mysql.connector.Error as err:
            print(f"Erreur lors de la connexion à la base de données : {err}")
            self.connection = None

    def execute_query(self, query, params=None):
        if self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
        else:
            print("La connexion à la base de données n'est pas établie.")
            return None


"""import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connexion réussie à la base de données")
        except Error as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Déconnexion de la base de données réussie")

    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Requête exécutée avec succès")
        except Error as e:
            print(f"Erreur lors de l'exécution de la requête : {e}")

    def fetch_data(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Erreur lors de la récupération des données : {e}")
            return None


# Exemple d'utilisation
db = Database(host="localhost", user="root", password="", database="votre_base_de_donnees")
db.connect()
db.execute_query(
    "CREATE TABLE IF NOT EXISTS utilisateurs (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), email VARCHAR(255))")
db.disconnect()"""
