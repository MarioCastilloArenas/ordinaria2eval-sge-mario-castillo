import hashlib
import json


def loadJson():
    with open("usuarios.json", "r") as file:
        return json.load((file))

print(loadJson())


def saveJason(data):
    with open("secure.json","w") as file:
        json.dump(data,file, indent = 4)

def hashPassword(plain_password):
    return hashlib.sha256(plain_password.encode()).hexdigest()

secure_users = []
i = 0
personas = loadJson()

for persona in personas:
    i = i+1
    nueva_persona = {
        'id': i,
        'name': persona['id'],
        'password': hashPassword(persona['password']),
    }

    secure_users.append(nueva_persona)

saveJason(secure_users)