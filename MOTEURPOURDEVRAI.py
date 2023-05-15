class Bateau:
    def __init__(self, nom, taille, orientation, x, y):
        #Initiation de l'objet : bateau mgl 
        self.nom = nom
        self.taille = taille
        self.orientation = orientation
        self.x = x
        self.y = y
        self.cases = []
        self.touchees = []
        self.etat = 'pastouché'
        self.init_cases()
#Initiation de l'objet : bateau mgl 

    def init_cases_en_lien_avec_le_bateau(self):
        #methode pour que le bateau ben il prennent ses coordonnées quoi 
        if self.orientation == 'Horizontale':
            for i in range(self.taille):# si le bateau est placé a l'horizontale il prend des places que sur une ligne et plusieurs colones
                self.cases.append((self.x, self.y + i))
        elif self.orientation == 'Verticale':# si le bateau est placé a la verticale il prend des places que sur une colone et sur plusieurs lignes 
            for i in range(self.taille):
                self.cases.append((self.x + i, self.y))

    def est_touche(self, x, y):
        if (x, y) in self.cases:
            self.touchees.append((x, y))# si la case visée fait partie des cases occupées par le bateau bah le bateau est TOCUH AHAHA
            if len(self.touchees) == len(self.cases):# si toutes les cases occupées par le bateau sont touchées, le bateau est coulé et t'as perdu
                self.etat = 'T AS ETE COULES AHAHA'
            else:
                self.etat = 'YOU GET TOUCH AHAHA'
            return True
        else:
            return False


