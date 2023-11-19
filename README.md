Gestion des Livres et Utilisateurs
Ce programme Python utilise la bibliothèque Tkinter pour créer une interface graphique permettant de gérer une liste de livres et d'utilisateurs. Il est divisé en deux classes principales :

GestionLivresUtilisateurs (dans gestion_livres_utilisateurs.py)
Cette classe définit un gestionnaire qui permet d'effectuer diverses opérations sur les livres et les utilisateurs, y compris l'ajout, la recherche, la suppression, la modification et l'emprunt de livres, ainsi que l'ajout d'utilisateurs.

Méthodes principales :

emprunter_livre(isbn): Effectue l'emprunt d'un livre en utilisant son ISBN.

ajouter_livre(titre, auteur, genre, isbn): Ajoute un livre à la liste.

supprimer_livre(isbn): Supprime un livre de la liste en utilisant son ISBN.

modifier_livre(isbn, titre=None, auteur=None, genre=None): Modifie les informations d'un livre en utilisant son ISBN.

rechercher_livres(critere, valeur): Recherche des livres en fonction d'un critère et d'une valeur.

ajouter_utilisateur(nom_utilisateur, mot_de_passe): Ajoute un utilisateur à la liste.

GestionLivresUtilisateursGUI (dans gestion_livres_utilisateurs_gui.py)

Cette classe utilise Tkinter pour créer une interface graphique permettant à l'utilisateur d'interagir avec le gestionnaire de livres et d'utilisateurs. Elle comprend des onglets pour la gestion des livres et utilisateurs, ainsi que pour afficher les utilisateurs inscrits.

Méthodes principales :
setup_gestion_livres_utilisateurs_ui(): Configure l'interface utilisateur pour la gestion des livres et utilisateurs.

setup_utilisateurs_ui(): Configure l'interface utilisateur pour afficher les utilisateurs inscrits.

ajouter_livre(): Ajoute un livre à la liste en utilisant les informations saisies.

rechercher_livre(): Recherche des livres en fonction d'un critère et d'une valeur.

supprimer_livre(): Supprime un livre de la liste en demandant à l'utilisateur d'entrer l'ISBN du livre.

modifier_livre(): Modifie les informations d'un livre en demandant à l'utilisateur d'entrer l'ISBN du livre et la nouvelle valeur.

emprunter_livre(): Effectue l'emprunt d'un livre en demandant à l'utilisateur d'entrer l'ISBN du livre.

ajouter_utilisateur(): Ajoute un utilisateur à la liste en utilisant les informations saisies.

clear_entries_livres(): Efface les valeurs actuellement présentes dans les champs de saisie associés aux informations sur les livres.

clear_entries_utilisateurs(): Efface les valeurs actuellement présentes dans les champs de saisie associés aux informations sur les utilisateurs.

ask_for_criteria(): Affiche une boîte de dialogue pour demander à l'utilisateur de choisir un critère de recherche parmi les options prédéfinies.

update_text_output(): Met à jour la zone de texte des livres après chaque modification.

update_text_output_utilisateurs(): Met à jour la zone de texte des utilisateurs après chaque modification.

Utilisation du programme

Exécutez le fichier gestion_livres_utilisateurs.py pour démarrer l'application.

L'interface graphique s'ouvrira avec deux onglets : "Gestion des Livres et Utilisateurs" et "Utilisateurs Inscrits".

Dans l'onglet "Gestion des Livres et Utilisateurs", vous pouvez ajouter, rechercher, supprimer, modifier et emprunter des livres. Vous pouvez également ajouter des utilisateurs.

L'onglet "Utilisateurs Inscrits" affiche la liste des utilisateurs ajoutés.