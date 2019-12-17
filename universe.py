class Espace(object):
    """Cette classe permet de crée l'espace dans lequel le robot va vivre son monde, width pour spécifier la largeur
   de matrice, le length pour spécifier la longueur de la matrice"""
    def __init__(self, width, length):
        self.length = length
        self.width = width
        self.world=[[0 for x in range(width)] for y in range(length)]# Génaration de l'espace ou le robot va pouvoir se déplacer

    def updateWorld(self, x, y, robot):
        """Cette fonction permet de mettre à jour le monde et indique ou se trouve le robot dans
       son monde elle n'écrase pas les anciens emplacements, je l'ai utilisé pour vérifier mon code. Tous les
       appels à cette fonction  peuvent être supprimer et le programme fonctionnera sans aucun problème,
       x indique la position du robot actuelle sur les lignes, y indique la position du robot actuelle sur les
       colonnes, robot notre objet robot qu'on va créer à l'aide de la Classe MrRobot"""
        self.world[x][y] = robot.getName() + "=>" + robot.getCurrentDirection()  # placer indique l'emplacment du robot