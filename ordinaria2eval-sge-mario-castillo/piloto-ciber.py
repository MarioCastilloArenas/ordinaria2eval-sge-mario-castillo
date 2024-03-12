import json
import pandas as pd
def loadJson():
    with open("reservas.json", "r") as file:
        return json.load((file))

print(loadJson())

def loadJson2():
    with open("secure.json", "r") as file:
        return json.load((file))

print(loadJson2())

reservas = loadJson()
personas =  loadJson2()
userId = []
personaarray = []
fecha = []
horas = []
#dentro de un array sala
idSala = []
plaza = []
suite = []


for persona in personas:
    for reserva in reservas:
        if persona['id'] == reserva['userId']:
            personaarray.append(persona['name'])
            userId.append(reserva['userId'])
            fecha.append(reserva['date'])
            horas.append(reserva['hours'])
            idSala.append(reserva['sala']['salaId'])
            plaza.append(reserva['sala']['suite'])
            suite.append(reserva['sala']['plazas'])


#en el excel guardamos los datos del array
df = pd.DataFrame({
    'persona': personaarray,
    'userId': userId,
    'fecha': fecha,
    'horas': horas,
    'idSala':idSala,
    'plaza': plaza,
    'suite': suite,

})

#pasamos los datos guardados en df al excel
df.to_excel("reservas.xlsx")
#pintamos df pues por la cara
print(df)

