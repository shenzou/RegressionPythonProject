# Projet Python: Année 5

## Dataset: Incident event log

- I. Modélisation
  - La partie modélisation se trouve dans le fichier Final Project.ipynb
  - Une modélisation avec des résultats différents est également présente: Option 2.ipynb

- II. API Django
  - Le modèle est sur git LFS (fichier volumineux) et doit être téléchargé manuellement (api/predictors/models/models.p)
  - Configuration de l'environnement: Ouvrir un terminal dans DjangoAPI, et lancer les commandes suivantes:
    1. python3 -m venv env
    2. source env/bin/activate
  - Si les paquets suivants ne sont pas installés, lancer la commande:
    1. pip install django djangorestframework sklearn numpy pandas
  - api/api/urls.py contient les URL endpoints
  - api/predictor/apps.py contient les variables extraites du modèle
  - api/predictors/views.py contient les réponses aux requêtes
  - api/predictor/models/models.p contient les modèles résultant de notre modélisation (I.)
  - Endpoint attendu: regressor/
  - Paramètres attendus:
    - caller_id
    - location
    - resolved_by
    - opened_by
    - opened_at (format YYYY/MM/DD HH:MM)
  - Format de la réponse: {"Random Forest Regressor:": prediction, "Decision Tree:": prediction, "Valeur probable:": prediction, "Finira le:" prediction}
  
- III. Présentation
  - La présentation PowerPoint est enregistrée sous le nom "Projet python for data analysis.pptx"
