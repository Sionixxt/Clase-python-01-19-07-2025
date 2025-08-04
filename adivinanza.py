import random
import requests

def obtenerpokemon_local():
     lista_local = ["pikachu", "bulbasaur", "charmander", "squirtle", "eevee", "jigglypuff", "meowth", "psyduck"]
     return random.choice(lista_local)

def obtenerpokemon():
    try:
        
        pokemon=random.randint(1, 1302)
        url=f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
        response=requests.get(url)
        if response.status_code==200:
            data=response.json()
            nombre=data["name"]
            return nombre
        else:
            print("No se pudo conectar a la API. Usando pokemon local")
            return obtenerpokemon_local()
    except(requests.ConnectionError, requests.Timeout):
        print("No tienes conexion a internet. Usando pokemon local")
        return obtenerpokemon_local()
     

def ahorcado():
    respuesta=1
    while respuesta==1:
        Habilidad=int(input("(1)Amateur, (2)Intermedio, (3)Experto: "))
        if Habilidad==1:
            intentos=10
        elif Habilidad==2:
            intentos=5
        else:
            intentos=3
        print(f"Tienes {intentos} intentos para adivinar el nombre del pokemon")
        nombre = obtenerpokemon()
        progress=["_"]*len(nombre)
        letras_usadas=[]
        while "_" in progress and intentos>0:
            print(" ".join(progress))
            letra=input("Introduzca una letra: ").lower()
            if len(letra)!=1:
                print("Debes introducir una sola letra")
                continue
            if letra in letras_usadas:
                print("Ya has introducido esa letra")
                continue
            letras_usadas.append(letra)
            if letra in nombre:
                for i in range(len(nombre)):
                    if nombre[i]==letra:
                        progress[i]=letra
            else:
                intentos-=1
                print(f"Intentos restantes: {intentos}")
                
        if "_" not in progress:
            print("Felicidades, Adivinaste el Pokémon:", nombre)
        else:
            print("Se acabaron los intentos. El Pokémon era:", nombre)    
  
            
        respuesta=int(input("Quiere volver a jugar? (1)Si o (2)No: "))
    print("Gracias por jugar, Hasta luego")
        

ahorcado()
    
    