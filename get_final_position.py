from c_ways_robot.universe import Espace
from c_ways_robot.robots import MrRobot


def main(universeDimensionsFile, instructionsFile):
    """Cette fonction prend en paramètre deux fichiers, universeDimensionsFile qui contient les dimensions du monde
    (espace) dont le robot va se déplacer. instructionsFile cotient l'ensemble d'instructions qui vont faire bouger
    le robot et affiche à l’écran la position final du robot (numColonne, numLigne)"""
    try: #si le nom du fichier spécifié dans le paramètre universeDimensionsFile n'existe pas

        with open(universeDimensionsFile, "r")as file:#ouvrir le fichier qui contient les tailles width et length
            _, width = file.readline().split(": ")#récupérer le width
            _, length = file.readline().split(": ")#récupérer le length
            width = int(width)
            length = int(length)

        world = Espace(width,length) # création d'un objet monde avec le wifth et le length qu'on a récupéré
        robot = MrRobot(name="B-VZXR", world=world)# création d'un objet robot dans le monde qu'on vient de créer

        try: #si le nom du fichier spécifié dans le paramètre instructionsFile n'existe pas

            with open(instructionsFile, "r") as file:# ouvrir le fichier qui contient les instructions
                instruction = file.readline()# lire la première instruction
                while instruction: # tant qu'on lit les lignes
                    robot.move(instruction) # on bouge le robot selon l'instruction  qu'on a récupéré
                    instruction = file.readline()# on avance vers l'instruction à venir

            print(robot.getCurrentPosition()) # on affiche la position finale du robot (numColonne, numLigne)

        except FileNotFoundError:
            print("File "+instructionsFile+" was not found")

    except FileNotFoundError:
        print("File "+universeDimensionsFile+" was not found")

if __name__ == '__main__':
    main(universeDimensionsFile="universe.txt", instructionsFile="instrucion_list.txt")
