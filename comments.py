from pymongo import MongoClient
from bson import ObjectId
import random


def generar_comentario(usuarios):
    random_usuario = random.choice(usuarios)
    author_id = random_usuario["_id"]
    
    limit_likes = random.randint(0, 20)
    likes = [usuario["_id"] for usuario in random.sample(usuarios, limit_likes)]
    
    return {
        "_id": ObjectId(),
        "author": author_id,
        "content": "Este es un comentario aleatorio",
        "image": "ruta/a/imagen.jpg",
        "likes": likes,
        "created_at": "ISODate('2023-10-26T21:30:00Z')",
        "updated_at": "ISODate('2023-10-26T21:30:00Z')",
        "answers": []
    }


def generar_comentarios_y_respuestas(db, publicaciones, usuarios):
    for publicacion in publicaciones:
        num_comentarios = random.randint(0, 5)
        comentarios = []

        for _ in range(num_comentarios):
            comentario = generar_comentario(usuarios)
            comentarios.append(comentario)

        # Muestra el número de comentarios generados
        print(f"Publicación ID {publicacion['_id']} - Comentarios generados: {len(comentarios)}")
        print(comentarios)  # Verifica los comentarios generados

        # Actualiza la publicación con los comentarios
        db["posts"].update_one(
            {"_id": publicacion["_id"]},
            {"$set": {"comments": comentarios}}
        )


if __name__ == '__main__':
    client = MongoClient("mongodb+srv://admin:1234@cluster0.nktfur3.mongodb.net/?retryWrites=true&w=majority")
    db = client["lime"]

    publicaciones = list(db["posts"].find())
    if not publicaciones:
        print("No hay publicaciones para agregar comentarios.")
    else:
        usuarios = list(db["users"].find())
        generar_comentarios_y_respuestas(db, publicaciones, usuarios)

    client.close()
