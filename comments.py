from pymongo import MongoClient
from bson import ObjectId
import random

# Conéctate a la base de datos
client = MongoClient("mongodb+srv://admin:1234@cluster0.nktfur3.mongodb.net/?retryWrites=true&w=majority")
db = client["lime"]

# Función para generar un comentario o respuesta con likes aleatorios
def generar_comentario(usuarios):
    # Recupera un ID aleatorio de usuario existente
    random_usuario = random.choice(usuarios)
    author_id = random_usuario["_id"]
    
    # Genera una lista de IDs de usuarios para los likes
    limit_likes = random.randint(0, 20)  # Establece el límite de likes como máximo en 20
    likes = [usuario["_id"] for usuario in random.sample(usuarios, limit_likes)]
    
    return {
        "_id": ObjectId(),
        "author": author_id,  # ID de un usuario que hizo el comentario
        "content": "Este es un comentario aleatorio",
        "image": "ruta/a/imagen.jpg",
        "likes": likes,
        "created_at": "ISODate('2023-10-26T21:30:00Z')",
        "updated_at": "ISODate('2023-10-26T21:30:00Z')",
        "answers": []
    }

# Recupera las publicaciones
publicaciones = db["posts"].find()

# Recupera la lista de usuarios
usuarios = list(db["users"].find())

# Itera a través de las publicaciones
for publicacion in publicaciones:
    # Genera un número aleatorio de comentarios para esta publicación
    num_comentarios = random.randint(0, 5)
    comentarios = []

    for x in range(num_comentarios):
        comentario = generar_comentario(usuarios)

        # Genera un número aleatorio de respuestas para este comentario
        num_respuestas = random.randint(0, 3)
        respuestas = []

        for x in range(num_respuestas):
            respuesta = generar_comentario(usuarios)
            respuestas.append(respuesta)

        comentario["answers"] = respuestas
        comentarios.append(comentario)

    # Actualiza la publicación con los comentarios
    db["posts"].update_one(
        {"_id": publicacion["_id"]},
        {"$set": {"comments": comentarios}}
    )
