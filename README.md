# IA d'échec CSLabs

Suite a un défis lancé au club d'échec de l'UNamur, le [CSLabs](https://www.cslabs.be/#/) de Namur s'est lancé dans la création d'une IA capable de battre les joueurs de l'université sans s'être entraînées sur des données humaines.

## Quick start

Pour installer les dépendance il vous suffit d'exécuter les commandes suivantes :

```
pip install pipenv

pipenv install
```

## Approche choisie

Il a été décidé d'implémenter une solution similaire à [Alphago Zero](https://fr.wikipedia.org/wiki/AlphaGo_Zero) qui a été capable de surpasser les hommes au jeu de Go sans être exposé à un seul exemple humain.

# Structure du projet 

## base

Classe de bases définissants des interfaces pour les éléments clés de l'architecture

## agents

Agents pouvant intervenir dans une partie. Nous en auront deux : 

- Agent humain
- Agent artificiel

## evaluators

Code permettant d'évaluer la valeur courante d'un état du jeu ainsi que les probabilités de jouer 
un certain nombre de mouvements

## games

Implémentation d'un environnement de jeu. Nous créerons un environnement de jeu d'échec mais il peut être
intèressant de pouvoir tester notre architecture sur d'autres jeux.

## move_searcher

Contiendra les code concernant les tree search ou autres algorithme cherchant le mouvement idéal à effectuer.

# Implémentation

Afin d'implémenter l'algorithme utilisé par l'équipe de deepmind, nous nous basons très largement sur [cet article de Medium](https://medium.com/applied-data-science/how-to-build-your-own-alphazero-ai-using-python-and-keras-7f664945c188).

## Monte-Carlo Tree Search (MCTS)

Partie de l'algorithme qui va se charger de trouver le prochain coup à exécuter.

## Reseau Deep Learning

Le réseau prend en entrée l'état courant du jeu et sort en output :

- une **Valeur** qui permet de savoir si le      plateau montre des signes encourageant de victoire ou pas

- Un **Vecteur de probabilités** pour chaque coup possible qui permet de savoir quel coup est le plus probable sur base de l'observation du jeu actuel.

Ce réseau sera entraîné sur base d'un historique de chaque partie

## Historique

Garde en mémoire le déroulement d'une partie afin de pouvoir backpropager le réseau

## Environnement de jeu

Module permettant de simuler l'environnement dans lequel se déroule le jeu. Il permet de récupérer ou restaurer des **etats** d'une partie, avoir accès aux **coups valides**, ...


# Questions en suspend

- Comment sera représenté l'état du jeu d'echec ?

- Comment seront représentés les coups possibles ?

- Comment backpropager une partie dans le réseau de neurone ?

- Comment savoir quand stopper la MCTS ?

- Comment gérer les coups de l'adversaire dans la MCTS ?
