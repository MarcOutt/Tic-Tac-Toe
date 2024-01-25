# Tic-Tac-Toe

## Introduction

Bienvenue dans le jeu du Morpion ! Il s'agit d'une implémentation console du classique jeu du Morpion en Python. Le jeu prend en charge deux joueurs qui se relaient pour marquer leur symbole ('X' ou 'O') sur une grille de jeu 3x3. Le premier joueur à aligner trois de ses symboles en ligne (horizontalement, verticalement ou en diagonale) remporte la partie.

## Comment Jouer

1. **Exécutez le script Python** pour démarrer le jeu.
2. Le jeu affiche un plateau de jeu vide avec des coordonnées pour chaque cellule.
3. Les joueurs effectuent leurs mouvements en spécifiant les numéros de ligne et de colonne.
4. Le jeu valide les mouvements et vérifie s'il y a un gagnant après chaque coup.
5. La partie se termine lorsqu'un joueur a trois symboles alignés ou lorsque le plateau est plein (égalité).

## Plateau de Jeu

Le plateau de jeu est une grille 3x3 où les joueurs effectuent leurs mouvements. Des coordonnées sont utilisées pour spécifier une cellule. L'état initial du plateau ressemble à ceci :

 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9


## Comment Exécuter

Assurez-vous d'avoir Python installé sur votre système. Ouvrez un terminal et naviguez jusqu'au répertoire contenant le script. Exécutez la commande suivante :

``python tic_tac_toe.py``

Exemple de Déroulement
Voici un exemple de déroulement d'une partie :

C'est au tour du joueur 1 de jouer
Veuillez choisir votre ligne : 2
Veuillez choisir votre colonne : 2

 X | _ | _ 
-----------
 _ | O | _
-----------
 _ |   | _

C'est au tour du joueur 2 de jouer
Veuillez choisir votre ligne : 1
Veuillez choisir votre colonne : 1

 X | _ | _
-----------
 _ | O | _ 
-----------
 O | _ | _ 

...

Le joueur 1 a gagné !
