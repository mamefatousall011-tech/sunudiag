"""SunuDiag - API REST servant le modèle paludisme (Lab 2)."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import joblib
import pandas as pd


app = FastAPI(
    title="SunuDiag API",
    description=(
        "Pré-diagnostic du paludisme (modèle DataSANTE-221). "
        "Un pré-diagnostic n'est pas un diagnostic médical."
    ),
    version="2.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Le modèle est chargé UNE SEULE FOIS au démarrage du serveur
modele = joblib.load("models/model.pkl")


FEATURES = [
    "age",
    "glycemie",
    "hemoglobine",
    "fievre",
    "saison",
]


class Patient(BaseModel):
    """Le contrat d'interface : ce que l'API accepte en entrée."""

    age: int = Field(
        ge=0,
        le=120,
        description="Âge en années",
    )

    glycemie: float = Field(
        ge=2.0,
        le=25.0,
        description="Glycémie (mmol/L)",
    )

    hemoglobine: float = Field(
        ge=4.0,
        le=20.0,
        description="Hémoglobine (g/dL)",
    )

    fievre: float = Field(
        ge=34.0,
        le=43.0,
        description="Température (°C)",
    )

    saison: int = Field(
        ge=0,
        le=1,
        description="1 = saison des pluies",
    )


@app.get("/health")
def health():
    """Vérifier que l'API est en vie et que le modèle est chargé."""

    return {
        "statut": "ok",
        "modele": "RandomForest DataSANTE-221",
    }


@app.post("/predict")
def predict(patient: Patient):
    """Prédire le risque de paludisme pour un patient."""

    donnees = pd.DataFrame(
        [patient.model_dump()]
    )[FEATURES]

    proba = float(
        modele.predict_proba(donnees)[0, 1]
    )

    return {
        "probabilite_paludisme": round(proba, 3),
        "pre_diagnostic": (
            "A ORIENTER"
            if proba >= 0.5
            else "risque faible"
        ),
        "avertissement": "Ne remplace pas un avis médical.",
    }