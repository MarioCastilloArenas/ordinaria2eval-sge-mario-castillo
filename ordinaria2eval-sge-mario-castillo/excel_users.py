import json
import pandas as pd

def loadJson():
    with open("secure.json", "r") as file:
        return json.load((file))

print(loadJson())

usuarios = loadJson()

#creamos unos arrays que sera donde guardaremos los datoa que vamos a mandar al excel
ids = []
names = []
passwords = []

for usuario in usuarios:
    #guardamos en los arrays los datos que queremos rescatar del secure.json
    ids.append(usuario['id'])
    names.append(usuario['name'])
    passwords.append(usuario['password'])

#en el excel guardamos los datos del array
df = pd.DataFrame({
    'id':  ids,
    'names': names,
    'passwrd': passwords
})

#pasamos los datos guardados en df al excel
df.to_excel("usuarios.xlsx")
#pintamos df pues por la cara
print(df)
