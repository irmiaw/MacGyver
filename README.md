# projet 3: Aidez MacGyver à s'échapper !

## Courte description du projet
C'est un jeu de labyrinthe codé en python.  
Mac Gyver doit collecter des objets puis endormir le garde qui surveille la sortie du labyrinthe.  
[**Détails du projet**](https://openclassrooms.com/projects/aidez-macgyver-a-sechapper)  

## Contraintes
- Versionner le code avec git et le publier sur Github  
- Suivre les recommandations de la PEP 8 et développerer dans un environnement virtuel utilisant Python 3  
- Code écrit en anglais (nom des variables, commentaires, fonctions, etc)

## Anticipation des diverses difficultés que je pourrais rencontrer  
- je ne connais pas encore Pygame (affichage + gestion des évenements clavier)  
- je dois apprendre a charger et lire les fichiers écrits dans mon propre format  
- anglais !!  
- quelques problèmes mineurs:  
  - placer aléatoirement les objets sur la carte (uniquement sur des cases vides)  
  - inventaire des objets (liste des objets avec 'true' si on les possède ou simple compteur d'objets ?)  
  - game design: choix des graphismes, boutons/options dans le jeu ?

### Problèmes imprévus
- installer pygame en python3 (https://askubuntu.com/questions/401342/how-to-download-pygame-in-python3-3)  
- trouver des images/sprites libres de droit (les images proposés par le cours sont pas très jolis)  

## Choix techniques:
Il est important de bien choisir les bibliothéques a utiliser et faire des prévisions du projet à long terme pour éviter la [*technical debt*](https://en.wikipedia.org/wiki/Technical_debt).  

### Bibliothéque graphique
Le programme se base sur le module Pygame. Même si Tkinter est plus simple, Pygame est plus adapté aux jeux 2D.  
Source principale du choix: https://openclassrooms.com/forum/sujet/choisir-entre-pygame-et-tkinter

### Format des fichiers
Le fichier du labyrinthe est une version simplifié du [format .xsb](https://fr.wikipedia.org/wiki/Sokoban)  

### Modules
Le programme est découpé en plusieurs modules avec un objectif bien défini. Afin de respecter l'indépendance des modules, les diverses méthodes qu'ils contiennent ne s'appellent pas directement entre eux. L'appel entre les modules est effectué dans la fonction main.  
- **main:** le fichier qui contient la fonction main
- **load:** chargement de la map (a partir du fichier .xsb) et des images du jeu
- **display:** gestion de l'affichage (module Pygame)  
- **game:** gestion du jeu (calcul des collisions (murs), objet personnage, méthodes de récupération des objets, calcul de victoire)  
- **constants:** constantes du programme

## Versionnage du projet
### Notation des versions
**x.y.z**  
x: version majeure (nouvelle branche)  
y: version mineure (nouvelle fonctionnalité)  
z: correction des bugs  

### Versions
0.0: Void  
C'est le néant. Il n'y a rien à part quelques idées.  

0.1: Création du dépot sur github  

0.2: Rédaction du fichier README.md  

0.5: Expérimentations avec Pygame  

**1.0:** Synthèse des méthodes utiles de Pygame  

1.1: Première brique  
Affichage d'une image de briques.  

1.2: Mur de briques  
Affichage des briques ou espaces en parcourant une liste à 2 dimensions 15*15, appelé map.  

1.3: Personnages  
Affichage de Mac Gyver et du garde à une certaine position.  
La position de Mac Gyver est définie dans son objet et la position du garde est définie dans la map.  

1.4: Mac Gyver se déplace  
Gére les évenements clavier, met à jour la position de Mac Gyver et rafraîchit l'affichage.  
Pas de gestion des collisions avec les murs et si Mac Gyver sort de la map le programme plante.  

1.5: Mac Gyver se cogne  
Gestion des collisions avec les murs et les bords de la map.  

1.6: Mac Gyver gagne  
Lorsque Mac Gyver arrive à la position du gardien le programme affiche un message de victoire et se termine.  

1.7: Refonte du programme  
Le programme est [découpé en modules](https://openclassrooms.com/courses/manipulez-des-donnees-avec-python-1/organisez-un-projet-en-modules) et est [mieux organisé](https://openclassrooms.com/courses/manipulez-des-donnees-avec-python-1/organisez-un-script)  

1.8: Environnement virtuel  
Mise en place d'un [environnement virtuel](https://openclassrooms.com/courses/manipulez-des-donnees-avec-python-1/travaillez-dans-un-environnement-virtuel)  

1.9: Bêta de la 2.0  
Test du programme, relecture du code et correction des bugs.  

**2.0:** Animer le personnage (branche stable)  
Version majeure du programme. Célébration avec une pizza !  

2.1: Chargement de la map a partir d'un fichier  

2.2: Détection de la position de Mac Gyver  

2.3: Gestion de la position des objets et leur affichage  

2.4: Gestion de la collecte des objets  

2.5: Répartition aléatoire des objets  
Algorithme basique, il y a un risque de "collision" avec la position d'un objet existant.  

2.6: Mac Gyver perd  
Lorsque Mac Gyver arrive à la position du gardien et n'a pas les 3 objets il perd et le programme se termine.  

2.7: Docstrings  
Documentation du code  

2.8: DRY  
*Don't Repeat Yourself*. Regroupement du code en methodes et autres structures.  

2.9: Bêta de la 3.0  
Test du programme, relecture du code et correction des bugs.  

**3.0:** Récupérer les objets (branche stable)  

3.1: Fichier config.json  
Le fichier contient la configuration des variables suivants:  
- Message lors de la collecte d'un objet, message de début et fin de partie  
- Les noms des images a charger (+ images dans un dossier à part)  
- Le nom des objets  

3.2: Programme plus fléxible  
Nombre d'objets variable: pour ajouter un objet il suffit de modifier le fichier config.json et rien d'autre.  
Taille de la map variable: pour modifier la taille de la map il suffit de modifier une constante et adapter le fichier map.xsb.  

3.3: Affichage des messages/dialogues dans la console  

3.4: Amélioration de l'algorithme de répartition des objets (éviter leur apparition sur une même case)  

3.5: N'afficher que Mac Gyver ou le gardien lorsqu'ils se trouvent sur la même case (en fonction de la victoire ou perte)  

3.6: Replay  
Proposer de rejouer à la fin d'une partie.  
La position des objets est réinitialisée, Mac Gyver replacé sur sa position initiale et son inventaire est vidé.  

3.7: PEP8  
Vérification du code avec Pylint  

3.8: [Gestion des erreurs](https://openclassrooms.com/courses/manipulez-des-donnees-avec-python-1/gerez-les-erreurs-et-les-bogues)  
Ajout de messages d'erreur clairs pour les utilisateurs du programme:  
- Changement de noms des fichiers du programme (par ex. si l'utilisateur essaye de remplacer une image par une autre).  
- Modification du config.json et oubli de spécifier un message, ou lien vers l'image de l'objet incorrect.  
- Oubli de définir la position initiale du personnage dans le fichier map.xsb (les autres erreurs ne sont pas gérées !).  

3.9: Bêta de la 4.0  
Test du programme, relecture du code et correction des bugs.  

**4.0:** Gagner ! (branche stable)    <---- je suis ici !  

4.9: Bêta de la 5.0  
Test du programme, relecture du code et correction des bugs.  

**5.0:** Intelligence artificielle (branche stable)  

## Contribuer
Ce projet a pour but de valider mes compétences en python. Par conséquent toute pull request avec du code sera refusé.  
Ouvrez plutôt une *issue* pour signaler un bug, une faute d'orthographe ou pour simplement donner un conseil.  
Le programme est dévéloppé sous linux (Ubuntu 16.04 64bit). Des tests pour les autres OS sont bienvenus !
