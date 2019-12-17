class MrRobot(object):
    """cette classe permet de crée des robots dont le nôtre (B-VZXR) qui va vivre dans notre monde [espace],elle permet de crée plusieurs
   robots si besoin elle prend en paramètre, name le nom du robot for fun :), world l'espace dans le robot va ce
   déplacer currentDirection spécifie ou le robot regarde actuellement par default  à up, x indique la position du
   robot actuelle sur les lignes par par default  à 0, y indique la position du robot actuelle sur les colonnes
   par default  à 0,"""

    def __init__(self, name, world, currentDirection="up", x=0, y=0):
        self.name = name
        self.directionActuel = currentDirection #direction up, down, left, right
        self.world = world
        self.x = x #self.x  la position de l'objet  actuelle sur les lignes
        self.y = y #self.Y  la position de l'objet  actuelle sur les colonnes
        self.placeInTheStartBox()#placer le robot dans la case départ du world {espace} pas nécessaire aussi !!

    def getName(self):
        """Retourne le nom du robot"""
        return self.name

    def getCurrentDirection(self):
        """Retourne la direction actuelle du robot """
        return self.directionActuel

    def checkX(self):
        """Vérifier si x dépasse les bornes et le recadré si c'est le cas"""
        if self.x >= self.world.length:# pour pas dépasser le mur du haut
            self.x = self.world.length - 1
        elif self.x < 0:# pour pas dépasser le mur du bas
            self.x = 0

    def checkY(self):
        """Vérifier si y dépasse les bornes et le recadré ssi c'est le cas """
        if self.y >= self.world.width:# pour pas dépasser le mur du gauche
            self.y = self.world.width - 1
        elif self.y < 0:# pour pas dépasser le mur de droite
            self.y = 0

    def placeInTheStartBox(self, ):
        """Cette fonction va placer le robot -B-VZXR- pour la première fois dans son monde  (espace); cette fonction
        et les appels à cette fonctions ne sont pas nécessaires pour le bon fonctionnement du code"""
        self.checkX()#au cas où les paramètres(x, y) ont été initialiser a une valeur autre que zéro on vérifie qu'ils ne dépassent pas les bornes
        self.checkX()
        self.world.updateWorld(self.x, self.y, self)# mettre é jours le world (pas nécessaire)

    def moveRight(self, nbrBoxesRobotMustMove):
        """Cette fonction permet de faire bouger notre robot à droite selon le nombre nbrBoxesRobotMustMove qui signifie
        le nombre de cases que le robot doit bouger"""
        self.directionActuel = "right" # dés qu'on bouge à droite on met à jour la direction du robot
        self.y = self.y + nbrBoxesRobotMustMove#on vas à droite on ajoute le nombre de cases que le robot dois bouger à la position actuelle on touche pas au x
        self.checkY() #on vérifie que y n'a pas dépasser les bornes
        self.world.updateWorld(self.x, self.y, self)# mettre é jours le world (pas nécessaire)

    def moveLeft(self, nbrBoxesRobotMustMove):
        """Cette fonction permet de faire bouger notre robot à gauche selon le nombre nbrBoxesRobotMustMove qui signifie
        le nombre de cases que le robot doit bouger"""
        self.directionActuel = "left" # dés qu'on bouge à gauche on met à jour la direction du robot
        self.y = self.y - nbrBoxesRobotMustMove #on vas à gauche on enléve e nombre de cases que le robot dois bouger à la position actuelle et on touche pas au x
        self.checkY()#on vérifie que y n'a pas dépasser les bornes
        self.world.updateWorld(self.x, self.y, self)# mettre é jours le world (pas nécessaire)

    def moveDown(self, nbrBoxesRobotMustMove):
        """Cette fonction permet de faire bouger notre robot vers le bas selon le nombre nbrBoxesRobotMustMove qui signifie
        le nombre de cases que le robot doit bouger"""
        self.directionActuel = "down"
        self.x = self.x - nbrBoxesRobotMustMove
        self.checkX()
        self.world.updateWorld(self.x, self.y, self)# mettre é jours le world (pas nécessaire)

    def moveUp(self, nbrBoxesRobotMustMove):
        """Cette fonction permet de faire bouger notre robot vers le haut selon le nombre nbrBoxesRobotMustMove qui signifie
        le nombre de cases que le robot doit bouger"""
        self.directionActuel = "up"
        self.x = self.x + nbrBoxesRobotMustMove
        self.checkX()
        self.world.updateWorld(self.x, self.y, self)# mettre à jours le world (pas nécessaire)

    def move(self, instruction):
        """Cette fonction va déterminer dans quelle direction le robot va bouger elle dépend de deux principaux
        paramètres qui sont la position du robot actuelle et l’instruction qui va le faire bouger vers la prochaine
        case, l'instruction contient sens de rotation et le nombre de cases que le robot dois bouger"""
        senseOfRotation, nbrBoxesRobotMustMove = instruction.split(", ") #récupérer le sens de rotation et le nbr de cases que le robot dois bouger
        nbrBoxesRobotMustMove = int(nbrBoxesRobotMustMove)
        if senseOfRotation == "right": #si le sens de rotation et right
            if self.directionActuel == "up": #et que le robot regarde en haut donc
                self.moveRight(nbrBoxesRobotMustMove) #il dois bouger vers la droite ............
            elif self.directionActuel == "right":
                self.moveDown(nbrBoxesRobotMustMove)
            elif self.directionActuel == "down":
                self.moveLeft(nbrBoxesRobotMustMove)
            elif self.directionActuel == "left":
                self.moveUp(nbrBoxesRobotMustMove)
        elif senseOfRotation == "left":#si le sens de rotation et left
            if self.directionActuel == "up":#et que le robot regarde en haut donc
                self.moveLeft(nbrBoxesRobotMustMove)#il dois bouger vers la gauche ............
            elif self.directionActuel == "right":
                self.moveUp(nbrBoxesRobotMustMove)
            elif self.directionActuel == "down":
                self.moveRight(nbrBoxesRobotMustMove)
            elif self.directionActuel == "left":
                self.moveDown(nbrBoxesRobotMustMove)

    def getCurrentPosition(self):
        """Permet de retourner un tuple qui contient numéro de la colonne et le numéro de la ligne (numColonne, numLigne)
        actuelle du robot, cette fonction est utilisé pour avoir la position final du robot dans le monde"""
        return (self.y, self.x)#(numColonne, numLigne)