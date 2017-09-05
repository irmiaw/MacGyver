# projet 3: Aidez MacGyver à s'échapper !

## Courte description du projet
C'est un jeu de labyrinthe codé en python. Mac Gyver qui doit collecter des objets puis endormir le garde qui surveille la sortie du labyrinthe.

### Details du projet:   
https://openclassrooms.com/projects/aidez-macgyver-a-sechapper  

## Contraintes
Vous versionnerez votre code en utilisant Git et le publierez sur Github pour que votre mentor puisse le commenter,  
Vous respecterez les bonnes pratiques de la PEP 8 et développerez dans un environnement virtuel utilisant Python 3,  
Votre code devra être écrit en anglais : nom des variables, commentaires, fonctions...  

### Contraintes suplémentaires:  
le projet étant public, je dois être clair sur le code et la doc (pas seulement pour moi et mon mentor)  

### Anticipation de divers difficultés que je pourrais rencontrer  
je ne connais pas encore Pygame (affichage + gestion des évenements clavier)  
je dois apprendre a charger et lire les fichiers écrits dans mon propre format  
anglais !!  
quelques problèmes mineurs:  
-placer aléatoirement les objets sur la carte (uniquement sur des cases vides)  
-inventaire des objets (liste des objets avec 'true' si on les possède ou simple compteur d'objets ?)  
-gamedesign: uniquement la map/labyrinthe ou des boutons suplémentaires ?, choix des graphismes  

## Choix technique:
Il est important de bien choisir les bibliothéques a utiliser et faire des prévisions du projet à long terme pour éviter la [*technical debt*](https://en.wikipedia.org/wiki/Technical_debt).  

### Bibliothéque
Le programme se base sur le module Pygame. Même si Tkinter est plus simple, Pygame est est plus adapté aux jeux 2D.  
Source principale du choix: https://openclassrooms.com/forum/sujet/choisir-entre-pygame-et-tkinter

### Format des fichiers
Le fichier du labyrinthe est une version simplifié du [format .xsb](https://fr.wikipedia.org/wiki/Sokoban)  

### Modules
Le programme est découpé en plusieurs modules avec un objectif bien défini. Afin de respecter l'indépendance des modules, les diverses méthodes qu'ils contiennent ne s'appellent pas directement entre eux. L'appel entre les modules est effectué dans la fonction main.
#### Modules crées:
chargement de la carte (a partir du fichier .xsb)  
gestion de l'affichage (module Pygame)  
gestion du jeu (calcul des collisions (murs), objet personnage, méthodes de récupération des objets, calcul de victoire)  

## Versionnage du projet
### Notation des versions
x.y.z  
x: version majeure (nouvelle branche)  
y: version mineure (sous étape)  
z: correction des bugs  

### Versions
0.0: Void
C'est le néant. Il n'y a rien à part quelques idées.  

0.1: Création du dépot sur github  

0.2: Rédaction du fichier README.md  

0.5:

1.1: Première brique  
Affichage d'une image de briques.  

1.2: Mur de briques  
Affichage des briques ou espaces en parcourant une liste à 2 dimensions 15*15, appelé map.  

1.3: Personnages  
Affichage de Mac Gyver et du garde à une certaine position.  
La position de Mac Gyver est définie dans son objet et la position du garde est définie dans la map.  

1.4: Mac Gyver se déplace  
Gére les évenements clavier, met à jour la position de Mac Gyver et rafraîchit l'affichage.  
Pas de gestion des collisions avec les murs et si Mac Gyver sort de la map la programme plante.  

1.5: Mac Gyver se cogne  
Gestion des collisions avec les murs et les bords de la map.  

1.6: Mac Gyver gagne  
Lorsque Mac Gyver arrive à la position du gardien le programme affiche un message de victoire, et propose peut-être de refaire une partie.  

1.7: [Refonte du programme](https://openclassrooms.com/courses/manipulez-des-donnees-avec-python-1/organisez-un-projet-en-modules)  
Le programme est découpé en 2 modules: la gestion de l'affichage et la gestion du jeu.  

1.8: [Gestion des erreurs](https://openclassrooms.com/courses/manipulez-des-donnees-avec-python-1/gerez-les-erreurs-et-les-bogues)  
Le programme lève une exception lorsque un bug survient. Le message d'erreur s'affiche en prenant en compte le niveau du log.  
Points pouvant créer regulièrement des bugs: images manquantes, manque d'un module, mauvais chemin/nom de fichier, utilisateur qui tape n'importe quoi au clavier.  
Les méthodes qui ne prennent pas en paramètre des données externes au programme plantent plus rarement. Néanmoins il faut tester leurs paramètres pour éviter de commettre des erreurs en chaine si une méthode en amont renvoie une valeur imprévue.  

1.9: Bêta de la 2.0  
Le programme est testé sous d'autres systèmes d'exploitation et en demandant l'avis à des utilisateurs bêta testeurs.  

2.0: Animer le personnage (branche stable)
Version majeure du programme. Célébration avec une pizza !

3.0: Récupérer les objets (branche stable)  

4.0: Gagner ! (branche stable)  

5.0: Intelligence artificielle (branche stable)  

## Contribuer:
pas de pull requests, seulement commentaires sur le code, conseils, problèmes avec le programme (issues)  
dev sous linux, tests sous win7 et arch, il faut un testeur sous macos
