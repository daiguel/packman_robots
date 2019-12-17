# packman_robots 
Pour comprendre ce que fait ce programme, essayez de penser comment un agent dans le jeu "packman" se déplace.

Le programme principal ‘get_final_position.py’ prend deux fichiers en paramètre, le premier fichier est le fichier de ‘universe.txt’ qui contient la longueur et la largeur du monde dont lequel le robot va jouer, le deuxième fichier en paramètre est le ‘instrucion_list.txt’ qui  contient l’ensemble d’instructions qui vont faire déplacer le robot.

Dans un premier temps le programme va lire le fichier ‘universe.txt’, ensuite il va créer l’objet  monde en fonction du width et length qu’il va trouver dans ce fichier, donc le monde est de taille width*height et il est de 2 dimensions.

Ensuite le programme va créer le robot portant le nom ‘B-VZXR’ qu’on va placer dans le monde qu’on vient de créer sur la case de départ qui porte les coordonnées  (0,0), avec sa direction actuelle vers le ‘up’, je tiens à préciser qu’on peut changer les coordonnées de la case de départ et la direction actuelle si on le souhaite, en les spécifiant comme paramètre pour le constructeur de la classe MrRobot. 
Exp: robot = MrRobot(name="B-VZXR", world=world , currentDirection="left", x=1, y=2) 
Cette ligne va placer le robot dans monde=world sur la case de départ qui porte les coordonnées  (1,2) et avec sa direction actuelle vers le ‘left’.

Ensuite le programme va lire le second fichier qui est ‘‘instrucion_list.txt’’ ligne par ligne et déplacera le robot tel que l’instruction l’indique en respectant les règles spécifiées dans le fichier ‘test-python.pdf’, cette étape est répétée jusqu’à la fin de toutes les instructions présentes dans le fichier ‘‘instrucion_list.txt’’.

A la fin le programme va afficher les coordonnées du robot ‘B-VZXR’ dans un tuple ainsi (numColonne, numLigne), et pour l’exemple actuelle on obtient (45, 83). 
