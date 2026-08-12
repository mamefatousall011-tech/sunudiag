# SunuDiag

## Description

SunuDiag est une application web pédagogique de pré-diagnostic du paludisme.

Elle permet de saisir les informations d'un patient et d'obtenir une estimation de la probabilité de paludisme à partir d'un modèle de Machine Learning.

> ⚠️ **Avertissement :** SunuDiag est un outil pédagogique de pré-diagnostic. Il ne remplace jamais l'avis, l'examen ou le diagnostic d'un professionnel de santé.

voici l'URL : https://sunudiag-11r5.onrender.com

## Fonctionnalités

- Saisie de l'âge du patient
- Saisie de la glycémie
- Saisie de l'hémoglobine
- Saisie de la température
- Sélection de la saison
- Prédiction de la probabilité de paludisme
- Affichage d'un pré-diagnostic
- Validation des données saisies
- Interface adaptée aux téléphones

## Technologies utilisées

- Python
- FastAPI
- Uvicorn
- Scikit-learn
- Pandas
- Joblib
- HTML
- Tailwind CSS
- Docker
- Git / GitHub
- Render

## Architecture

L'application est composée de plusieurs éléments :

- `api/` : API FastAPI
- `frontend/` : interface utilisateur
- `models/` : modèle de Machine Learning
- `Dockerfile` : recette de conteneurisation
- `requirements.txt` : dépendances Python

FastAPI sert directement le frontend afin que l'application fonctionne avec une seule origine et un seul serveur.

## Utilisation

L'utilisateur renseigne les informations du patient puis clique sur **Analyser**.

L'API reçoit les données, les transmet au modèle de Machine Learning et retourne :

- une probabilité de paludisme ;
- un pré-diagnostic ;
- un avertissement indiquant que le résultat ne remplace pas un avis médical.

## Tests de référence

Les tests suivants permettent de vérifier que l'application fonctionne correctement.

### Patient Moussa

- Âge : 34 ans
- Glycémie : 5,8 mmol/L
- Hémoglobine : 13,1 g/dL
- Température : 39,2 °C
- Saison : saison des pluies

Résultat attendu : **61,0 %**

### Patient Awa

- Âge : 61 ans
- Glycémie : 7,2 mmol/L
- Hémoglobine : 10,4 g/dL
- Température : 37,0 °C
- Saison : saison sèche

Résultat attendu : **19,0 %**

Une température de **99 °C** doit être refusée par l'API.

## Déploiement

L'application est conteneurisée avec Docker et peut être déployée sur Render.

Le conteneur utilise la variable d'environnement `PORT` fournie par Render.

## Auteur

**Mame Fatou Sall**

Master 1 Intelligence Artificielle et Big Data  
DMI / FST / UCAD

## Licence

Ce projet est distribué sous licence MIT.

## Limites

SunuDiag est un projet pédagogique. Le modèle et l'application ne constituent pas un dispositif médical et ne doivent pas être utilisés pour établir un diagnostic médical réel.