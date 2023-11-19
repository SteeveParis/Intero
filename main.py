import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk

class GestionLivresUtilisateurs:
    def __init__(self):
        # Initialisation de la liste des livres et des utilisateurs
        self.livres = []
        self.utilisateurs = []
        
    def emprunter_livre(self, isbn):
        """Effectue l'emprunt d'un livre en utilisant son ISBN."""
        for livre in self.livres:
            if livre['isbn'] == isbn:
            # Ajoutez ici la logique pour gérer l'emprunt (par exemple, en mettant à jour le statut du livre)
            # Pour l'exemple, nous supposerons que le livre peut être emprunté
                livre['statut'] = 'Emprunté'
            return True
        return False

    def ajouter_livre(self, titre, auteur, genre, isbn):
        """Ajoute un livre à la liste."""
        if not titre or not auteur or not genre or not isbn:
            return None

        livre = {'titre': titre, 'auteur': auteur, 'genre': genre, 'isbn': isbn}
        self.livres.append(livre)
        return livre

    def supprimer_livre(self, isbn):
        """Supprime un livre de la liste en utilisant son ISBN."""
        for livre in self.livres:
            if livre['isbn'] == isbn:
                self.livres.remove(livre)
                return livre
        return None

    def modifier_livre(self, isbn, titre=None, auteur=None, genre=None):
        """Modifie les informations d'un livre en utilisant son ISBN."""
        for livre in self.livres:
            if livre['isbn'] == isbn:
                if titre:
                    livre['titre'] = titre
                if auteur:
                    livre['auteur'] = auteur
                if genre:
                    livre['genre'] = genre
                return livre
        return None

    def rechercher_livres(self, critere, valeur):
        """Recherche des livres en fonction d'un critère et d'une valeur."""
        resultats = [livre for livre in self.livres if str(livre[critere]).lower() == str(valeur).lower()]
        return resultats

    def ajouter_utilisateur(self, nom_utilisateur, mot_de_passe):
        """Ajoute un utilisateur à la liste."""
        if not nom_utilisateur or not mot_de_passe:
            return None

        utilisateur = {'nom_utilisateur': nom_utilisateur, 'mot_de_passe': mot_de_passe}
        self.utilisateurs.append(utilisateur)
        return utilisateur

class GestionLivresUtilisateursGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestion des Livres et Utilisateurs")

        self.gestionnaire = GestionLivresUtilisateurs()
        # Variable de classe pour stocker l'ISBN actuellement sélectionné
        self.isbn_selectionne = None

        # Configuration des couleurs
        self.bg_color = "#2c3e50"  # Bleu foncé
        self.button_bg_color = "#16a085"  # Vert
        self.button_fg_color = "white"
        self.label_fg_color = "#ecf0f1"  # Blanc
        self.text_output_bg_color = "#34495e"  # Bleu-gris

        # Configuration de la fenêtre principale
        self.master.configure(bg=self.bg_color)

        # Création d'un gestionnaire d'onglets
        self.notebook = ttk.Notebook(master)

        # Onglet de gestion des livres et utilisateurs
        self.tab_livres_utilisateurs = tk.Frame(self.notebook, bg=self.bg_color)
        self.notebook.add(self.tab_livres_utilisateurs, text='Gestion des Livres et Utilisateurs')
        self.setup_gestion_livres_utilisateurs_ui()

        # Onglet d'affichage des utilisateurs
        self.tab_utilisateurs = tk.Frame(self.notebook, bg=self.bg_color)
        self.notebook.add(self.tab_utilisateurs, text='Utilisateurs Inscrits')
        self.setup_utilisateurs_ui()

        # Afficher l'onglet initial
        self.notebook.pack(fill=tk.BOTH, expand=True)

    # Configure l'interface utilisateur avec des labels, des champs de saisie et des boutons pour gérer les informations sur les livres et les utilisateurs
    def setup_gestion_livres_utilisateurs_ui(self):
        tk.Label(self.tab_livres_utilisateurs, text="Titre", fg=self.label_fg_color, bg=self.bg_color).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Label(self.tab_livres_utilisateurs, text="Auteur", fg=self.label_fg_color, bg=self.bg_color).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tk.Label(self.tab_livres_utilisateurs, text="Genre", fg=self.label_fg_color, bg=self.bg_color).grid(row=2, column=0, padx=10, pady=5, sticky="w")
        tk.Label(self.tab_livres_utilisateurs, text="ISBN", fg=self.label_fg_color, bg=self.bg_color).grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.titre_entry = tk.Entry(self.tab_livres_utilisateurs, bg=self.text_output_bg_color)
        self.titre_entry.grid(row=0, column=1, padx=10, pady=5)
        self.auteur_entry = tk.Entry(self.tab_livres_utilisateurs, bg=self.text_output_bg_color)
        self.auteur_entry.grid(row=1, column=1, padx=10, pady=5)
        self.genre_entry = tk.Entry(self.tab_livres_utilisateurs, bg=self.text_output_bg_color)
        self.genre_entry.grid(row=2, column=1, padx=10, pady=5)
        self.isbn_entry = tk.Entry(self.tab_livres_utilisateurs, bg=self.text_output_bg_color)
        self.isbn_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(self.tab_livres_utilisateurs, text="Ajouter Livre", command=self.ajouter_livre, bg=self.button_bg_color, fg=self.button_fg_color).grid(row=4, column=0, columnspan=2, pady=10, padx=10)
        tk.Button(self.tab_livres_utilisateurs, text="Rechercher Livre", command=self.rechercher_livre, bg=self.button_bg_color, fg=self.button_fg_color).grid(row=4, column=1, columnspan=2, pady=10, padx=10)
        tk.Button(self.tab_livres_utilisateurs, text="Supprimer Livre", command=self.supprimer_livre, bg=self.button_bg_color, fg=self.button_fg_color).grid(row=6, column=0, columnspan=2, pady=10, padx=10)
        tk.Button(self.tab_livres_utilisateurs, text="Modifier Livre", command=self.modifier_livre, bg=self.button_bg_color, fg=self.button_fg_color).grid(row=7, column=0, columnspan=2, pady=10, padx=10)
        tk.Button(self.tab_livres_utilisateurs, text="Emprunter Livre", command=self.emprunter_livre, bg=self.button_bg_color, fg=self.button_fg_color).grid(row=6, column=1, columnspan=2, pady=10, padx=10)
        
        tk.Label(self.tab_livres_utilisateurs, text="Nom d'utilisateur", fg=self.label_fg_color, bg=self.bg_color).grid(row=8, column=0, padx=10, pady=5, sticky="w")
        tk.Label(self.tab_livres_utilisateurs, text="Mot de passe", fg=self.label_fg_color, bg=self.bg_color).grid(row=9, column=0, padx=10, pady=5, sticky="w")

        self.nom_utilisateur_entry = tk.Entry(self.tab_livres_utilisateurs, bg=self.text_output_bg_color)
        self.nom_utilisateur_entry.grid(row=8, column=1, padx=10, pady=5)
        self.mot_de_passe_entry = tk.Entry(self.tab_livres_utilisateurs, show="*", bg=self.text_output_bg_color)
        self.mot_de_passe_entry.grid(row=9, column=1, padx=10, pady=5)

        tk.Button(self.tab_livres_utilisateurs, text="Ajouter Utilisateur", command=self.ajouter_utilisateur, bg=self.button_bg_color, fg=self.button_fg_color).grid(row=10, column=0, columnspan=2, pady=10, padx=10)

        # Zone de texte pour afficher les livres avec une scrollbar
        self.text_output = tk.Text(self.tab_livres_utilisateurs, height=20, width=60, bg=self.text_output_bg_color, fg=self.label_fg_color)
        self.text_output.grid(row=11, column=0, columnspan=2, pady=10, padx=10)
        self.scrollbar = tk.Scrollbar(self.tab_livres_utilisateurs, command=self.text_output.yview, bg=self.button_bg_color)
        self.scrollbar.grid(row=11, column=2, sticky='nsew')
        self.text_output['yscrollcommand'] = self.scrollbar.set

        # Mettre à jour la zone de texte après chaque modification
        self.update_text_output()

    def setup_utilisateurs_ui(self):
        # Zone de texte pour afficher les utilisateurs inscrits
        self.text_output_utilisateurs = tk.Text(self.tab_utilisateurs, height=20, width=60, bg=self.text_output_bg_color, fg=self.label_fg_color)
        self.text_output_utilisateurs.pack(pady=10, padx=10)

        # Mettre à jour la zone de texte des utilisateurs
        self.update_text_output_utilisateurs()

    # Fait l'ajout du livre dans la liste, en entrant les informaion demander
    def ajouter_livre(self):
        titre = self.titre_entry.get()
        auteur = self.auteur_entry.get()
        genre = self.genre_entry.get()
        isbn = self.isbn_entry.get()

        if not titre or not auteur or not genre or not isbn:
            messagebox.showinfo("Erreur", "Veuillez remplir tous les champs.")
            return

        livre = self.gestionnaire.ajouter_livre(titre, auteur, genre, isbn)
        if livre:
            self.clear_entries_livres()
            self.update_text_output()

    # Fonction de recherche de livre avec l'ISBN demander et affiche le nombre de résultats
    def rechercher_livre(self):
        critere = self.ask_for_criteria()
        if critere:
            valeur = simpledialog.askstring("Rechercher Livre", f"Entrez la valeur pour le critère '{critere}':")
            if valeur:
                resultats = self.gestionnaire.rechercher_livres(critere, valeur)
                self.text_output.delete(1.0, tk.END)  # Efface le contenu actuel
                if resultats:
                    self.text_output.insert(tk.END, f"{len(resultats)} résultat(s) trouvé(s):\n")
                    for livre in resultats:
                        self.text_output.insert(tk.END, f"{livre}\n")
                else:
                    self.text_output.insert(tk.END, "Aucun résultat trouvé.\n")
            else:
                messagebox.showinfo("Erreur", "La valeur de recherche ne peut pas être vide.")
        else:
            messagebox.showinfo("Erreur", "Aucun critère de recherche sélectionné.")

    # Demande à l'utilisateur d'entrée l'ISBN du livre pour le supprimer de la liste
    def supprimer_livre(self):
        isbn = simpledialog.askstring("Supprimer Livre", "Entrez l'ISBN du livre à supprimer:")
        if isbn:
            livre = self.gestionnaire.supprimer_livre(isbn)
            if livre:
                self.clear_entries_livres()
                self.update_text_output()
            else:
                messagebox.showinfo("Erreur", "Livre non trouvé.")
        else:
            messagebox.showinfo("Erreur", "L'ISBN ne peut pas être vide.")        

    def modifier_livre(self):
         # Demander à l'utilisateur de saisir l'ISBN du livre à modifier
        isbn = simpledialog.askstring("Modifier Livre", "Entrez l'ISBN du livre à modifier:")

        if isbn:
            # Vérifier si l'ISBN existe dans la liste des livres
            livre_exist = any(livre['isbn'] == isbn for livre in self.gestionnaire.livres)

            if livre_exist:
                # Afficher une boîte de dialogue pour la modification
                nouvelle_valeur = simpledialog.askstring("Modifier Livre", f"Entrez la nouvelle valeur pour l'ISBN {isbn}:")

                if nouvelle_valeur:
                    # Effectuer la modification
                    titre = self.titre_entry.get()
                    auteur = self.auteur_entry.get()
                    genre = self.genre_entry.get()

                    livre = self.gestionnaire.modifier_livre(isbn, titre, auteur, genre)
                    if livre:
                        self.clear_entries_livres()
                        self.update_text_output()
                    else:
                        messagebox.showinfo("Erreur", "Livre non trouvé.")
                else:
                    messagebox.showinfo("Erreur", "La nouvelle valeur ne peut pas être vide.")
            else:
                messagebox.showinfo("Erreur", f"L'ISBN {isbn} n'existe pas dans la liste des livres.")
        else:
            messagebox.showinfo("Erreur", "L'ISBN ne peut pas être vide.")
    def emprunter_livre(self):
    # Demandez à l'utilisateur d'entrer l'ISBN du livre à emprunter
        isbn = simpledialog.askstring("Emprunter Livre", "Entrez l'ISBN du livre à emprunter:")

        if isbn:
        # Appelez la fonction de votre gestionnaire pour effectuer l'emprunt
            emprunt_reussi = self.gestionnaire.emprunter_livre(isbn)

            if emprunt_reussi:
            # Mise à jour de l'affichage après l'emprunt
                self.clear_entries_livres()
                self.update_text_output()
                messagebox.showinfo("Succès", f"Livre avec ISBN {isbn} emprunté avec succès.")
            else:
                messagebox.showinfo("Erreur", f"L'emprunt du livre avec ISBN {isbn} a échoué.")
        else:
            messagebox.showinfo("Erreur", "L'ISBN ne peut pas être vide.")

    # Permet de faire l'ajout d'un uilisateur
    def ajouter_utilisateur(self):
        nom_utilisateur = self.nom_utilisateur_entry.get()
        mot_de_passe = self.mot_de_passe_entry.get()

        if not nom_utilisateur or not mot_de_passe:
            messagebox.showinfo("Erreur", "Veuillez remplir tous les champs.")
            return

        utilisateur = self.gestionnaire.ajouter_utilisateur(nom_utilisateur, mot_de_passe)
        if utilisateur:
            self.clear_entries_utilisateurs()
            self.update_text_output_utilisateurs()
            messagebox.showinfo("Succès", f"Utilisateur ajouté avec succès.\nNom d'utilisateur : {nom_utilisateur}")
        else:
            messagebox.showinfo("Erreur", "Erreur lors de l'ajout de l'utilisateur.")

    # Effacer les valeurs actuellement présentes dans plusieurs champs de saisie associés aux informations sur les livres.
    def clear_entries_livres(self):
        self.titre_entry.delete(0, tk.END)
        self.auteur_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
        self.isbn_entry.delete(0, tk.END)

    # Etre appelée lorsque vous souhaitez effacer les valeurs actuellement présentes dans les champs de saisie du nom d'utilisateur et du mot de passe associés
    def clear_entries_utilisateurs(self):
        self.nom_utilisateur_entry.delete(0, tk.END)
        self.mot_de_passe_entry.delete(0, tk.END)

    # Boîte de dialogue simple demandant à l'utilisateur de choisir un critère de recherche parmi les options prédéfinies.
    def ask_for_criteria(self):
        options = ['titre', 'auteur', 'isbn']
        return simpledialog.askstring("Critère de Recherche", "Choisissez le critère de recherche:", initialvalue=options[0], show="*")

    # Widget de texte supprimant son contenu actuel, puis en insérant les informations de chaque livre
    def update_text_output(self):
        self.text_output.delete(1.0, tk.END)
        for livre in self.gestionnaire.livres:
            self.text_output.insert(tk.END, f"{livre}\n")

    # Widget de texte supprimant son contenu actuel, puis en insérant les informations de chaque utilisateurs
    def update_text_output_utilisateurs(self):
        self.text_output_utilisateurs.delete(1.0, tk.END)
        for utilisateur in self.gestionnaire.utilisateurs:
            self.text_output_utilisateurs.insert(tk.END, f"Nom d'utilisateur : {utilisateur['nom_utilisateur']}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionLivresUtilisateursGUI(root)
    root.mainloop()