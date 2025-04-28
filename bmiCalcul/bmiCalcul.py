# Importation des bibliothèques nécessaires
from fastapi import FastAPI

# Création de l'application FastAPI
app = FastAPI()

# Définition de la route racine
@app.get("/")

def read_root():
    """
    Fonction qui gère la route racine de l'application.
    Elle retourne un message de bienvenue.
    """
    return {"message": "Bienvenue sur l'API de calcul de l'IMC (Indice de Masse Corporelle) ! Utilisez /bmi pour calculer votre IMC."}

