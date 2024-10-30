import pymongo
import random
from datetime import datetime

# Conectar a la base de datos MongoDB
client = pymongo.MongoClient("mongodb+srv://admin:1234@cluster0.nktfur3.mongodb.net/?retryWrites=true&w=majority")
db = client["lime"]

# Colección de usuarios
usuarios = db["users"]

# Colección de notificaciones
notificaciones = db["notifications"]

# Paso 1: Extraer los "_id" de usuarios
usuarios_ids = [doc["_id"] for doc in usuarios.find({}, {"_id": 1})]

# Tipo de notificaciones posibles
tipos_notificaciones = ["mensaje", "seguidor", "otro_tipo"]

# Paso 2: Insertar notificaciones con datos aleatorios
for i in range(5000):  # Inserta 100 notificaciones de ejemplo
    random_user_id = random.choice(usuarios_ids)
    random_sender_id = random.choice(usuarios_ids)
    random_tipo = random.choice(tipos_notificaciones)
    random_read = random.choice([True, False])
    random_detalle = "Motivo de la notificación"
    created_at = datetime.now()

    notificacion = {
        "user_id": random_user_id,
        "sender_id": random_sender_id,
        "type": random_tipo,
        "read": random_read,
        "detalle": random_detalle,
        "message": created_at
    }

    notificaciones.insert_one(notificacion)

# Cierra la conexión
client.close()
