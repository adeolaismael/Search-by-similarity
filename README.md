## Installation des Dépendances

Pour installer les dépendances nécessaires, suivez ces étapes :

1. Ouvrez votre terminal.

2. Déplacez-vous dans le dossier `FASEP` en utilisant la commande :

   ```
   cd chemin/vers/FASEP
   ```

3. Exécutez la commande suivante pour installer les dépendances à partir du fichier `requirements.txt` :

   ```
   pip install -r requirements.txt
   ```

## Exécution des Tests

Une fois l'installation terminée, procédez comme suit pour exécuter les tests :

1. Déplacez-vous dans le dossier `tests` :

   ```
   cd tests
   ```

2. Dans le fichier `test.py`, remplacez le chemin d'accès contenu dans la variable `test_file_path` par 

le chemin d'accès vers le fichier `Exemple FASEP.pptx` sur votre ordinateur. (Vous aurez peut-être à changer le "/" en "\")

Enregistrez les modifications.

3. Exécutez les tests en utilisant `pytest` :

   ```
   pytest test.py
   ```

