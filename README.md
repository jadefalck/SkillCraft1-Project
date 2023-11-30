# SkillCraft1-Project

Ce projet python a été réalisé dans le cadre d'une analyse des performances de différents modèles de régression. Les modèles utilisés sont la régression linéaire, le support vector regression (SVR), et la régression Elastic Net.
La base de données transcrits différentes variables sur les joueurs du jeu StarCraft, que nous allons utiliser pour prédire leur rang.

## Contenu du Projet

1. **Analyse des Données** :
   - Un jeu de données CSV (`data.csv`) contenant les données à analyser.
   - Un notebook réalisé sur Jupyter, avec un nettoyage et une analyse des données, ainsi que la réalisation de différents modèles afin de prédire le rang d'un joueur en fonction de différentes variables.

2. **Modèles de Régression** :
   - Trois scripts pour chaque modèle.
   - Résultats et performances des modèles, y compris les métriques telles que le Mean Squared Error (MSE) et le R-squared (R²).

3. **Graphiques** :
   - Un script qui génère des graphiques comparant les performances des modèles.

4. **Site Web** :
   - Une application Flask (`app.py`) pour afficher les résultats et les graphiques.
   - Le dossier `templates` contient les fichiers HTML.

## Instructions d'Utilisation

1. **Analyse des Données** et **Modèles de Régression** :
   - Exécutez le notebook `SkillCraft1_Master_Table_Database_Jade_Gabriel.ipynb` pour effectuer l'analyse exploratoire des données.

2. **Site Web** :
   - Ouvrez le terminal, et notez `cd venv` pour vous diriger vers le bon dossier.
   - Exécutez le script `app.py` pour lancer l'application Flask, en ecrivant sur le terminal `python app.py`
   - Accédez au lien créé pour voir votre site.

## Remarques

- Assurez-vous d'avoir les bibliothèques Python nécessaires installées (`pip install -r requirements.txt`) :
  - pandas
  - plotly
  - flask 
- Les résultats des modèles et les graphiques sont disponibles sur le site web.
