# Ce programme permet à l'utilisateur de rechercher et d'afficher des recettes de cuisine
from tkinter import *

class Application(Tk):
    "Application"
    def __init__(self):
        super().__init__() # Hériter des attributs de la classe Tk

        self.label_recheche = Label(self, text="Renseignez le nom de la recette que vous souhaitez rechercher :") # Label pour indiquer à l'utilisateur ce qu'on attend de lui
        self.label_recheche.pack()

        self.champ_recherche = Entry(self) # Champ pour la recherche d'une recette de cuisine
        self.champ_recherche.pack(fill="x")

        self.bouton_recherche = Button(self, text="Rechercher la recette de cuisine", command=None) # Bouton pour rechercher la recette de cuisine
        self.bouton_recherche.pack(fill="x")



app = Application()
app.mainloop()        