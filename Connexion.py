import tkinter as tk
from tkinter import messagebox
from database import Database
import importlib


class ConnexionApp:
    def __init__(self):
        # Création de la fenêtre principale
        self.connexion = tk.Tk()
        self.connexion.title("Interaction Software")
        self.connexion.geometry("600x400")
        self.connexion.configure(bg='#f0f0f0')

        # Création des frames
        self.frame_left = tk.Frame(self.connexion, bg='#ffcccc', width=300, height=400)
        self.frame_right = tk.Frame(self.connexion, bg='#ccffcc', width=300, height=400)

        # Placement des frames
        self.frame_left.pack(side='left', fill='both', expand=True)
        self.frame_right.pack(side='right', fill='both', expand=True)

        # Ajout de contenu aux frames (exemple)
        self.label_left = tk.Label(self.frame_left, text="INTERACTION SOFTWARE", bg='#ffcccc')
        self.label_left2 = tk.Label(self.frame_left, text="M1 Images et Interactios", bg='#ffcccc')
        self.label_left3 = tk.Label(self.frame_left, text="Vous n'avez-pas de compte!", bg='#ffcccc')
        self.btnInscript = tk.Button(self.frame_left, text="Inscription", bg='#ffcccc', command=self.ouvrirInscription)

        self.label_left.pack(pady=40)
        self.label_left2.pack(pady=20)
        self.label_left3.pack(pady=40)
        self.btnInscript.pack(pady=10)

        # Première ligne de labels
        """self.label_title1 = tk.Label(self.frame_right, text="Bienvenu", font=("Berlin sans FB", 20), bg='#f0f0f0',
                                     fg='#333')
        self.label_title2 = tk.Label(self.frame_right, text="Tongasoa", font=("Berlin sans FB", 20), bg='#f0f0f0',
                                     fg='#333')

        self.label_title1.pack(padx=10, pady=10)
        self.label_title2.pack(padx=10, pady=10)

        # Label "Connexion"
        self.label_title = tk.Label(self.frame_right, text="Connexion", font=("Helvetica", 16), bg='#f0f0f0', fg='#333')
        self.label_title.pack(pady=20)

        # Formulaire
        self.label_name = tk.Label(self.frame_right, text="Nom:", bg='#f0f0f0')
        self.entry_name = tk.Entry(self.frame_right, width=30)
        self.label_password = tk.Label(self.frame_right, text="Mot de passe:", bg='#f0f0f0')
        self.entry_password = tk.Entry(self.frame_right, width=30, show='*')
        self.button_submit = tk.Button(self.frame_right, text="Se connecter", width=25, command=self.connexion_action,
                                       bg='#4CAF50', fg='white')

        self.label_name.pack(padx=5, pady=5)
        self.entry_name.pack(padx=5, pady=5)
        self.label_password.pack(padx=5, pady=5)
        self.entry_password.pack(padx=5, pady=5)
        self.button_submit.pack(padx=10, pady=20)"""

        # Création des widgets
        self.label_title1 = tk.Label(self.frame_right, text="Bienvenu", font=("Berlin sans FB", 20), bg='#f0f0f0',
                                     fg='#333')
        self.label_title2 = tk.Label(self.frame_right, text="Tongasoa", font=("Berlin sans FB", 20), bg='#f0f0f0',
                                     fg='#333')
        self.label_title = tk.Label(self.frame_right, text="Connexion", font=("Helvetica", 16), bg='#f0f0f0', fg='#333')
        self.label_name = tk.Label(self.frame_right, text="Nom:", bg='#f0f0f0')
        self.label_password = tk.Label(self.frame_right, text="Mot de passe:", bg='#f0f0f0')

        self.entry_name = tk.Entry(self.frame_right, width=30)
        self.entry_password = tk.Entry(self.frame_right, width=30, show='*')

        self.button_submit = tk.Button(self.frame_right, text="Se connecter", width=25, command=self.connexion_action,
                                       bg='#4CAF50', fg='white')

        self.label_title1.pack(side=tk.TOP, padx=10, pady=10)
        self.label_title2.pack(side=tk.TOP, padx=10, pady=10)
        self.label_title.pack(side=tk.TOP, padx=10, pady=20)
        self.label_name.pack(side=tk.BOTTOM, padx=5, pady=5)
        self.entry_name.pack(side=tk.BOTTOM, padx=5, pady=5)
        self.label_password.pack(side=tk.BOTTOM, padx=5, pady=5)
        self.entry_password.pack(side=tk.BOTTOM, padx=5, pady=5)
        self.button_submit.pack(side=tk.BOTTOM, padx=10, pady=20)

        # Lancement de la boucle principale
        self.connexion.mainloop()

    # Exemple d'utilisation
    db = Database(host="localhost", user="root", password="", database="proojetinteractionbdd")
    db.connect()

    def connexion_action(self):
        name = self.entry_name.get()
        password = self.entry_password.get()
        if not name or not password:
            messagebox.showwarning("Avertissement", "Veuillez remplir tout les formulaires !")
        else:
            result = self.db.execute_query(
                "SELECT * FROM utilisateur WHERE nomU = %s and motdepasseU = %s", (name, password))
            if result:
                messagebox.showinfo("Information", "Connexion réussie!")
                # self.connexion.destroy()  # Fermer la fenêtre actuelle
                # main = importlib.import_module('main')
                # main.open_main_window()  # Ouvrir la nouvelle fenêtre
            else:
                messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect")

    def ouvrirInscription(self):
        self.connexion.destroy()  # Fermer la fenêtre actuelle
        inscription = importlib.import_module('Inscription')
        inscription.InscriptionApp()  # Ouvrir la nouvelle fenêtre


# Lancement de l'application
app = ConnexionApp()

"""import tkinter as tk
from tkinter import messagebox
import mysql.connector

import database


class ConnexionApp:
    def __init__(self):
        # Création de la fenêtre principale
        self.connexion = tk.Tk()
        self.connexion.title("Interaction Software")
        self.connexion.geometry("600x400")
        self.connexion.configure(bg='#f0f0f0')

        # Création des frames
        self.frame_left = tk.Frame(self.connexion, bg='#ffcccc', width=300, height=400)
        self.frame_right = tk.Frame(self.connexion, bg='#ccffcc', width=300, height=400)

        # Placement des frames
        self.frame_left.pack(side='left', fill='both', expand=True)
        self.frame_right.pack(side='right', fill='both', expand=True)

        # Ajout de contenu aux frames (exemple)
        self.label_left = tk.Label(self.frame_left, text="INTERACTION SOFTWARE", bg='#ffcccc')
        self.label_left2 = tk.Label(self.frame_left, text="M1 Images et Interactios", bg='#ffcccc')
        self.label_left3 = tk.Label(self.frame_left, text="Vous n'avez-pas de compte!", bg='#ffcccc')
        self.btnInscript = tk.Button(self.frame_left, text="Inscription", bg='#ffcccc')

        self.label_left.pack(pady=40)
        self.label_left2.pack(pady=20)
        self.label_left3.pack(pady=40)
        self.btnInscript.pack(pady=10)

        # Création des widgets
        self.label_title1 = tk.Label(self.frame_right, text="Bienvenu", font=("Berlin sans FB", 20), bg='#f0f0f0',
                                     fg='#333')
        self.label_title2 = tk.Label(self.frame_right, text="Tongasoa", font=("Berlin sans FB", 20), bg='#f0f0f0',
                                     fg='#333')
        self.label_title = tk.Label(self.frame_right, text="Connexion", font=("Helvetica", 16), bg='#f0f0f0', fg='#333')
        self.label_name = tk.Label(self.frame_right, text="Nom:", bg='#f0f0f0')
        self.label_password = tk.Label(self.frame_right, text="Mot de passe:", bg='#f0f0f0')

        self.entry_name = tk.Entry(self.frame_right, width=30)
        self.entry_password = tk.Entry(self.frame_right, width=30, show='*')

        self.button_submit = tk.Button(self.frame_right, text="Se connecter", width=25, command=self.connexion_action,
                                       bg='#4CAF50', fg='white')

        # Placement des widgets
        self.label_title1.pack(pady=10)
        self.label_title2.pack(pady=10)
        self.label_title.pack(pady=10)
        self.label_name.pack(pady=5)
        self.entry_name.pack(pady=5)
        self.label_password.pack(pady=5)
        self.entry_password.pack(pady=5)
        self.button_submit.pack(pady=20)

        # Lancement de la boucle principale
        self.connexion.mainloop()

    # Exemple d'utilisation
    db = database.Database(host="localhost", user="root", password="", database="proojetinteractionbdd")
    db.connect()

    def connexion_action(self):
        name = self.entry_name.get()
        password = self.entry_password.get()
        if name or password is None:
            # Vous pouvez ajouter ici le code pour traiter les données du formulaire
            messagebox.showwarning("Avertissement", f"Vous dévez d'abord complèter ces formulaires!")
        else:
            database.db.execute_query(
                "SELECT * FROM utilisateur WHERE nomU = ? and motdepasseU = ?")

            messagebox.showinfo("Information", f"Connexion réussi!")


# Création et lancement de l'application
app = ConnexionApp()"""
