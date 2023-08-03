import tkinter as tk

# Créer une fenêtre
fenetre = tk.Tk()
fenetre.title("Exemple Tkinter")

# Créer une étiquette avec du texte
etiquette = tk.Label(fenetre, text="Bonjour, ceci est un exemple Tkinter!")
etiquette.pack(padx=20, pady=20)  # Afficher l'étiquette dans la fenêtre avec des marges

# Lancer la boucle principale de Tkinter pour afficher la fenêtre
fenetre.mainloop()
