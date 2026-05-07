from customtkinter import *
import requests
from PIL import Image



carac = [
    "Température",
    "Description Météo",
    "Humidité"
]
champs = []
ecran = CTk()
ecran.minsize(600,500)
ecran.title("Météo")
ecran.configure(fg_color="#87CEFA")
ecran.resizable(0,0)
ecran.iconbitmap("meteo.ico")

def get_meteo():
    l = Entry.get()
    reponse = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={l}&appid=174b7a07135690b4d62578cd7741b409&units=metric&lang=fr")
    data = reponse.json()
    print(data)
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    champs[0].insert("end",temperature)
    champs[1].insert("end",description)
    champs[2].insert("end",humidity)

image = Image.open("meteo.png")
image = image.resize((150, 150))
photo = CTkImage(light_image=image, dark_image=image, size=(150, 150))
label_image = CTkLabel(ecran, image=photo,text="",fg_color= "transparent")
label_image.grid(row = 0,column = 1,padx = 55,pady = 30)

label = CTkLabel(ecran,text="ville",text_color="black")
label.grid(column=0,row=2,padx=30,pady=10)
Entry = CTkEntry(ecran,border_width=0)
Entry.grid(column=1,row=2,padx=30,pady=10)

bouton = CTkButton(ecran,text= "Rechercher",command=get_meteo)
bouton.grid(column=2,row=2,padx=30,pady=10)

for i in range(0,len(carac)):
    texte = CTkLabel(ecran,text=carac[i],width=50,height=50,text_color="black")
    texte.grid(column=0,row=i+3,padx=30,pady=10)
    champ = CTkEntry(ecran,border_width=0)
    champ.grid(column=1,row=i + 3,padx=30,pady=10)
    champs.append(champ)




ecran.mainloop()
