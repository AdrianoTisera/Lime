import pymongo
import random
from datetime import datetime

# Conectar a la base de datos MongoDB
client = pymongo.MongoClient("mongodb+srv://admin:1234@cluster0.nktfur3.mongodb.net/?retryWrites=true&w=majority")
db = client["lime"]

# Colección de usuarios
usuarios = db["users"]

# Colección de followers
followers = db["followers"]

# Paso 1: Extraer los "_id" de usuarios
usuarios_ids = [doc["_id"] for doc in usuarios.find({}, {"_id": 1})]

# Paso 2: Insertar datos aleatorios en la colección "followers"
for i in range(2500):  # Inserta 100 registros de ejemplo
    random_user_id = random.choice(usuarios_ids)
    random_followed_id = random.choice(usuarios_ids)
    date = datetime.now()

    # Asegúrate de que el usuario no se siga a sí mismo
    while random_user_id == random_followed_id:
        random_followed_id = random.choice(usuarios_ids)

    follower = {
        "user_id": random_user_id,
        "followed_id": random_followed_id,
        "date": date
    }

    followers.insert_one(follower)

# Cierra la conexión
client.close()
