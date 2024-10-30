import pymongo
import random
from datetime import datetime


def colecciones_final():
  # Colección de usuarios
  usuarios = db["users"]

  # Colección de publicaciones
  publicaciones = db["posts"]

  # Paso 1: Extraer los "_id" de usuarios
  usuarios_ids = [doc["_id"] for doc in usuarios.find({}, {"_id": 1})]

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

def colecciones_inicial():
  # Obtener la lista de usuarios existentes
  usuarios = db.users.find({})

  # Estructura de una publicación
  publicacion_template = {
      "author": None,  # Aquí se llenará con el ObjectId del autor
      "content": "Contenido de la publicación",
      "image": "ruta/a/imagen.jpg",
      "likes": [],
      "created_at": datetime.utcnow(),
      "comments": []
  }

  # Iterar sobre la lista de usuarios y crear publicaciones
  for usuario in usuarios:
      for x in range(2):  # Crear 2 publicaciones por usuario
          nueva_publicacion = publicacion_template.copy()
          nueva_publicacion["author"] = usuario["_id"]
          db.posts.insert_one(nueva_publicacion)  # Reemplaza "publicaciones" con el nombre de tu colección de publicaciones

if __name__=='__main__':
  # Conecta a la base de datos MongoDB
  client = pymongo.MongoClient("mongodb+srv://admin:1234@cluster0.nktfur3.mongodb.net/?retryWrites=true&w=majority")
  db = client["lime"]
  
  colecciones_inicial()
  colecciones_final()

  # Cierra la conexion
  client.close()
