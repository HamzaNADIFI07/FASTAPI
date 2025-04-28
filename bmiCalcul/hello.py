# Importation des bibliothèques nécessaires
from fastapi import FastAPI , Query

# Importation de la classe BaseModel de Pydantic
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

class BmiOutput(BaseModel):
    """
    Classe représentant un item avec un indice de masse corporelle (IMC) et un message.
    """
    bmi: float
    message: str
# Création de l'application FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permettre toutes les origines
    allow_credentials=True,
    allow_methods=["*"],  # Permettre toutes les méthodes HTTP
    allow_headers=["*"],  # Permettre tous les en-têtes
)
# Définition de la route racine
@app.get("/")

def read_root():
    """
    Fonction qui gère la route racine de l'application.
    Elle retourne un message de bienvenue.
    """
    return {"message": "Bienvenue sur l'API de calcul de l'IMC (Indice de Masse Corporelle) ! Utilisez /bmi pour calculer votre IMC."}

# Définition de la route pour le calcul de l'IMC
@app.get("/bmi")

def calculBmi(weight: float = Query(...,gt=10,lt=200 , description='entre 10 et 20') , height: float = Query(...,gt=1.0,lt=2.5 , description='entre 1m et 2.5m')):
    bmi= weight / (height ** 2)
    if bmi < 18.5:
        a="You are underweight."
    elif 18.5 <= bmi < 24.9:
        a="You have a normal weight."
    elif 25 <= bmi < 29.9:
        a="You are overweight."
    else:
        a="You are obese."
    return BmiOutput(bmi=bmi, message=a)