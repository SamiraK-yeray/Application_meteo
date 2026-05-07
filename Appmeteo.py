from customtkinter import *
import requests
from PIL import Image

# ---------------- FENETRE ---------------- #

ecran = CTk()
ecran.geometry("700x500")
ecran.title("Application Météo")
ecran.configure(fg_color="#87CEFA")
ecran.resizable(False, False)

# ---------------- API ---------------- #

API_KEY = "TON_API_KEY"

# ---------------- FONCTION ---------------- #

def get_meteo():

    ville = entry_ville.get()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={ville}&appid={API_KEY}&units=metric&lang=fr"

    reponse = requests.get(url)
    data = reponse.json()

    # Vérifie si la ville existe
    if data["cod"] != 200:
        label_resultat.configure(
            text="Ville introuvable ❌",
            text_color="red"
        )
        return

    # Récupération des données
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidite = data["main"]["humidity"]

    # Affichage
    texte = f"""
🌡 Température : {temperature} °C

☁ Description : {description}

💧 Humidité : {humidite} %
"""

    label_resultat.configure(
        text=texte,
        text_color="black"
    )

# ---------------- IMAGE ---------------- #

image = Image.open("meteo.png")

photo = CTkImage(
    light_image=image,
    dark_image=image,
    size=(150, 150)
)

label_image = CTkLabel(
    ecran,
    image=photo,
    text=""
)

label_image.pack(pady=20)

# ---------------- TITRE ---------------- #

titre = CTkLabel(
    ecran,
    text="Application Météo",
    font=("Arial", 28, "bold"),
    text_color="black"
)

titre.pack(pady=10)

# ---------------- CHAMP VILLE ---------------- #

entry_ville = CTkEntry(
    ecran,
    width=250,
    height=40,
    placeholder_text="Entrez une ville"
)

entry_ville.pack(pady=10)

# ---------------- BOUTON ---------------- #

bouton = CTkButton(
    ecran,
    text="Rechercher",
    command=get_meteo,
    width=200,
    height=40
)

bouton.pack(pady=10)

# ---------------- RESULTAT ---------------- #

label_resultat = CTkLabel(
    ecran,
    text="",
    font=("Arial", 18),
    text_color="black"
)

label_resultat.pack(pady=20)

# ---------------- LANCEMENT ---------------- #

ecran.mainloop()