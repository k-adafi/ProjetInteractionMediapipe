import tkinter as tk
from tkinter import messagebox
from database import Database
import importlib


class InscriptionApp:
    def __init__(self):
        # Création de la fenêtre principale
        self.inscription = tk.Tk()
        self.inscription.title("Interaction Software")
        self.inscription.geometry("600x400")
        self.inscription.configure(bg='#f0f0f0')

        # Création des frames
        self.frame_left = tk.Frame(self.inscription, bg='#ffcccc', width=300, height=400)
        self.frame_right = tk.Frame(self.inscription, bg='#ccffcc', width=300, height=400)

        # Placement des frames
        self.frame_left.pack(side='left', fill='both', expand=True)
        self.frame_right.pack(side='right', fill='both', expand=True)

        # Ajout de contenu aux frames (exemple)
        self.label_left = tk.Label(self.frame_left, text="INTERACTION SOFTWARE", bg='#ffcccc')
        self.label_left2 = tk.Label(self.frame_left, text="M1 Images et Interactios", bg='#ffcccc')
        self.label_left3 = tk.Label(self.frame_left, text="Vous avez déjà un compte!", bg='#ffcccc')
        self.btnInscript = tk.Button(self.frame_left, text="Connexion", bg='#ffcccc', command=self.ouvrirConnexion)

        self.label_left.pack(pady=40)
        self.label_left2.pack(pady=20)
        self.label_left3.pack(pady=40)
        self.btnInscript.pack(pady=10)

        # Création des widgets
        self.label_title1 = tk.Label(self.frame_right, text="Bienvenu", font=("Berlin sans FB", 20), bg='#f0f0f0',
                                     fg='#333')
        self.label_title2 = tk.Label(self.frame_right, text="Tongasoa", font=("Berlin sans FB", 20), bg='#f0f0f0',
                                     fg='#333')
        self.label_title = tk.Label(self.frame_right, text="Inscription", font=("Helvetica", 16), bg='#f0f0f0',
                                    fg='#333')
        self.label_name = tk.Label(self.frame_right, text="Nom:", bg='#f0f0f0')
        self.label_email = tk.Label(self.frame_right, text="Email:", bg='#f0f0f0')  # Nouveau champ pour l'email
        self.label_password = tk.Label(self.frame_right, text="Mot de passe:", bg='#f0f0f0')

        self.entry_name = tk.Entry(self.frame_right, width=30)
        self.entry_email = tk.Entry(self.frame_right, width=30)  # Nouveau champ pour l'email
        self.entry_password = tk.Entry(self.frame_right, width=30, show='*')

        self.button_submit = tk.Button(self.frame_right, text="S'inscrire", width=25, command=self.inscription_action,
                                       bg='#4CAF50', fg='white')

        self.label_title1.pack(pady=10)
        self.label_title2.pack(pady=10)
        self.label_title.pack(pady=10)
        self.label_name.pack(pady=5)
        self.entry_name.pack(pady=5)
        self.label_email.pack(pady=5)  # Placement du nouveau champ pour l'email
        self.entry_email.pack(pady=5)  # Placement du nouveau champ pour l'email
        self.label_password.pack(pady=5)
        self.entry_password.pack(pady=5)
        self.button_submit.pack(pady=20)

        # Lancement de la boucle principale
        self.inscription.mainloop()

    # Initialisation de la base de données
    db = Database(host="localhost", user="root", password="", database="proojetinteractionbdd")
    db.connect()

    def inscription_action(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        if not name or not email or not password:
            messagebox.showwarning("Avertissement", "Veuillez remplir tous les champs !")
        else:
            try:
                self.db.execute_query(
                    "INSERT INTO utilisateur (nomU, emailU, motdepasseU) VALUES (%s, %s, %s)",
                    (name, email, password))
                messagebox.showinfo("Information", "Inscription réussie!")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de l'inscription : {e}")

    def ouvrirConnexion(self):
        self.inscription.destroy()  # Fermer la fenêtre actuelle
        connexion = importlib.import_module('Connexion')
        connexion.ConnexionApp()  # Ouvrir la nouvelle fenêtre


# Lancement de l'application
app = InscriptionApp()

"""import tkinter as tk
from tkinter import messagebox


class Inscrire:
    def __init__(self):
        # Création de la fenêtre principale
        self.root = tk.Tk()
        self.root.title("Formulaire d'inscription")
        self.root.geometry("300x250")
        self.root.configure(bg='#f0f0f0')

        # Création des widgets
        self.label_title = tk.Label(self.root, text="Inscription", font=("Helvetica", 16), bg='#f0f0f0', fg='#333')
        self.label_name = tk.Label(self.root, text="Nom:", bg='#f0f0f0')
        self.label_email = tk.Label(self.root, text="Email:", bg='#f0f0f0')
        self.label_password = tk.Label(self.root, text="Mot de passe:", bg='#f0f0f0')

        self.entry_name = tk.Entry(self.root)
        self.entry_email = tk.Entry(self.root)
        self.entry_password = tk.Entry(self.root, show='*')

        self.button_submit = tk.Button(self.root, text="S'inscrire", command=self.inscription, bg='#4CAF50', fg='white')

        # Placement des widgets
        self.label_title.pack(pady=10)
        self.label_name.pack(pady=5)
        self.entry_name.pack(pady=5)
        self.label_email.pack(pady=5)
        self.entry_email.pack(pady=5)
        self.label_password.pack(pady=5)
        self.entry_password.pack(pady=5)
        self.button_submit.pack(pady=20)

        # Lancement de la boucle principale
        self.root.mainloop()

    def inscription(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        # Vous pouvez ajouter ici le code pour traiter les données du formulaire
        messagebox.showinfo("Inscription", f"Nom: {name}\nEmail: {email}\nMot de passe: {password}")


# Création et lancement de l'application
app = Inscrire()"""
