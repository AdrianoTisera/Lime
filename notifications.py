import pymongo
import random
from datetime import datetime

def generar_notificaciones(db, cantidad=5000, batch_size=100):
    # Colección de notificaciones
    notificaciones = db["notifications"]

    # Colección de usuarios
    usuarios = db["users"]

    # Paso 1: Extraer los "_id" de usuarios
    usuarios_ids = [doc["_id"] for doc in usuarios.find({}, {"_id": 1})]

    # Tipo de notificaciones posibles
    tipos_notificaciones = ["mensaje", "seguidor", "otro_tipo"]

    # Lista para acumular notificaciones
    notificaciones_a_insertar = []

    # Paso 2: Insertar notificaciones con datos aleatorios
    for _ in range(cantidad):  # Inserta 5000 notificaciones
        random_user_id = random.choice(usuarios_ids)
        random_sender_id = random.choice(usuarios_ids)
        random_tipo = random.choice(tipos_notificaciones)
        random_read = random.choice([True, False])
        random_detalle = "Motivo de la notificación"
        created_at = datetime.utcnow()  # Usar UTC para consistencia

        notificacion = {
            "user_id": random_user_id,
            "sender_id": random_sender_id,
            "type": random_tipo,
            "read": random_read,
            "detalle": random_detalle,
            "message": created_at
        }

        notificaciones_a_insertar.append(notificacion)

        # Inserta en lotes
        if len(notificaciones_a_insertar) >= batch_size:
            notificaciones.insert_many(notificaciones_a_insertar)
            notificaciones_a_insertar.clear()  # Limpia la lista para el próximo lote

    # Inserta cualquier notificación restante
    if notificaciones_a_insertar:
        notificaciones.insert_many(notificaciones_a_insertar)

if __name__ == '__main__':
    # Conectar a la base de datos MongoDB
    client = pymongo.MongoClient("mongodb+srv://admin:1234@cluster0.nktfur3.mongodb.net/?retryWrites=true&w=majority")
    db = client["lime"]

    generar_notificaciones(db)

    # Cierra la conexión
    client.close()
