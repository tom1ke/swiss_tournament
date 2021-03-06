# Centre Échecs

Programme de gestion de Tournois Suisses

Version : Python 3.10.1

## Paramétrage 

- Cloner le repository 
- Créer un environnement virtuel à la racine du projet avec la commande

```
 python3 -m venv env
```

- Activer l'environnement virtuel avec la commande

```
source env/bin/activate
```

- Installer les modules et paquets nécessaires automatiquement avec la commande

```
pip install -r requirements.txt
```

## Exécution du programme

- Ouvrir un terminal
- Se positionner à la racine du projet
- Lancer le programme avec la commande

```
python3 main.py
```

## Paramétrage du programme

Il est possible de modifier certains paramètres du programme, comme le nombre de tours ou de joueurs par défaut d'un 
tournoi.

Afin que le programme fonctionne correctement, le nombre de joueurs doit être pair et le nombre de tour doit être la 
moitié du nombre de joueurs

Pour cela, il faudra modifier certaines variables du fichier util.py à la racine du projet.

- Ouvrir le fichier util.py avec un éditeur de texte ou un IDE
- Pour le nombre de tours par défaut, changer la valeur par un autre nombre entier de

```python
NUMBER_OF_ROUNDS = 4
```

- Pour le nombre de joueurs par défaut, changer la valeur par un autre nombre entier de

```python
NUMBER_OF_PLAYERS = 8
```

## Utiisation de Flake8

Il est possible d'utiliser Flake8 afin de vérifier la conformité du projet avec la PEP8.

Pour générer un rapport HTML via Flake8, utiliser la commande

```
flake8 --format=html --htmldir=flake8_rapport --exclude=env/ --max-line-length=119
```

Le rapport généré se trouvera dans le dossier *flake8_rapport* à la racine du projet.

Pour le visualiser, ouvrir le fichier *index.html* avec un navigateur (Chrome, Mozilla, Safari...).