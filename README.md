# MacGyver
projet 3: Aidez MacGyver à s'échapper !

Details du projet: 
https://openclassrooms.com/projects/aidez-macgyver-a-sechapper

Contraintes
Vous versionnerez votre code en utilisant Git et le publierez sur Github pour que votre mentor puisse le commenter,
Vous respecterez les bonnes pratiques de la PEP 8 et développerez dans un environnement virtuel utilisant Python 3,
Votre code devra être écrit en anglais : nom des variables, commentaires, fonctions...

Contraintes suplémentaires:
le projet étant public, je dois etre clair sur le code et la doc (pas seuelement pour moi et mon mentor)

Anticipation de divers difficultés que je pourrais rencotrer
je ne connais pas encore PyGame
je dois apprendre a charger et lire les fichiers écrits dans mon propre format
anglais !!
quelques problèmes mineurs:
-placer aléatoirement les objets sur la carte (uniquement sur des cases vides)
-inventaire des objets (liste des objets avec 'true' si on les possède ou simple compteur d'objets ?)
-gamedesign: uniquement la map/labyrinthe ou des boutons suplémentaires ?, choix des graphismes


Modules
découpage en modules:
chargement de la carte (a partir du fichier .xsb)
gestion de l'affichage (module PyGame)
gestion du jeu (calcul des collisions (murs), objet personnage, methodes de recuperation des objets, calcul de victoire)

Versionnage
1 version majeure (nouvelle branche)
0.1 version mineure (sous étape)
0.0.1 correction des bugs


Versions
1 - Créer le cadre de départ

Initialisez un repo Git et envoyez-le sur Github.

Commencez par créer le labyrinthe sans l’interface graphique. Quand la logique de votre labyrinthe est faite, utilisez le module PyGame pour dessiner l’interface graphique.

Puis intéressez-vous aux trois éléments principaux du jeu : le gardien, MacGyver et les objets. Comment les représenter dans votre programme ? Où sont-ils placés au commencement du jeu ?  
2 - Animer le personnage

Le seul élément mouvant est MacGyver. Créez les méthodes de classe qui permettent de l'animer et de trouver la sortie. Pour l'instant, faites une version simplifiée du jeu dans laquelle MacGyver gagne en arrivant face au gardien.
 
3 - Récupérer les objets

Ajoutez la gestion des objets. Comment MacGyver les ramasse-t-il ?  Ajoutez également un compteur qui les listera.
 
4 - Gagner !

Enfin, changez la fin du jeu : MacGyver gagne s'il a bien ramassé tous les objets et endormi le garde. Sinon, il perd.

5 - Intelligence artificielle


Soutenir:
pas de pull requests, seulement commentaires sur le code, conseils, problèmes avec le programme (issues)
dev sous linux, tests sous win7 et arch, il faut un testeur sous macos





