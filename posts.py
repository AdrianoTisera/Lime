import pymongo
from datetime import datetime
import random


def colecciones_final(db):
    # Colección de publicaciones
    publicaciones = db["posts"]

    # Paso 1: Extraer los "_id" de usuarios
    usuarios_ids = [doc["_id"] for doc in db["users"].find({}, {"_id": 1})]

    # Paso 2: Actualizar documentos en la colección "publicaciones"
    for publicacion in publicaciones.find({}):
        # Genera valores aleatorios
        random_author = random.choice(usuarios_ids)
        random_likes = random.sample(usuarios_ids, random.randint(0, 20))

        # Actualiza el documento de la publicación con datos aleatorios
        publicaciones.update_one(
            {"_id": publicacion["_id"]},
            {
                "$set": {
                    "author": random_author,
                    "likes": random_likes,
                }
            }
        )


def colecciones_inicial(db, batch_size=100):
    # Obtener la lista de usuarios existentes
    usuarios = list(db.users.find({}))

    # Estructura de una publicación
    publicacion_template = {
        "author": None,  # Aquí se llenará con el ObjectId del autor
        "content": "Contenido de la publicación",
        "image": "ruta/a/imagen.jpg",
        "likes": [],
        "created_at": datetime.utcnow(),
        "comments": []
    }

    publicaciones_a_insertar = []  # Lista para acumular publicaciones

    # Iterar sobre la lista de usuarios y crear publicaciones
    for usuario in usuarios:
        num_publicaciones = random.randint(0, 5)  # Número aleatorio de publicaciones entre 1 y 20
        for _ in range(num_publicaciones):
            nueva_publicacion = {**publicacion_template, "author": usuario["_id"]}
            publicaciones_a_insertar.append(nueva_publicacion)

            # Inserta en lotes
            if len(publicaciones_a_insertar) >= batch_size:
                db.posts.insert_many(publicaciones_a_insertar)
                publicaciones_a_insertar.clear()  # Limpia la lista para el próximo lote

    # Inserta cualquier publicación restante que no se haya insertado
    if publicaciones_a_insertar:
        db.posts.insert_many(publicaciones_a_insertar)


if __name__ == '__main__':
    # Conecta a la base de datos MongoDB
    client = pymongo.MongoClient("mongodb+srv://admin:1234@cluster0.nktfur3.mongodb.net/?retryWrites=true&w=majority")
    db = client["lime"]

    colecciones_inicial(db)
    colecciones_final(db)

    # Cierra la conexión
    client.close()
