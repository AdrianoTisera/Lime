from faker import Faker
from datetime import datetime
import random
from pymongo import MongoClient

fake = Faker()

# Generar 100 registros de datos de usuarios
user_data_list = []
for _ in range(100):
    first_name = fake.first_name()
    last_name = fake.last_name()
    username = f"{first_name.lower()}{last_name.lower()}{random.randint(1, 999)}"
    
    user_data = {
        "_id": f"ObjectId('{fake.md5(raw_output=False)}')",  # Simula un ID único similar a MongoDB
        "name": f"{first_name} {last_name}",
        "user_name": username,
        "email": fake.email(),
        "password": fake.password(length=12),  # Contraseña aleatoria de 12 caracteres
        "profile_picture": fake.file_path(extension="jpg"),  # Ruta aleatoria de imagen
        "created_at": datetime.utcnow().isoformat()  # Fecha y hora actual en formato ISO
    }
    user_data_list.append(user_data)

# Imprime los primeros 5 registros para verificar
for user in user_data_list[:5]:
    print(user)


# Conexión a la base de datos MongoDB
uri = "mongodb+srv://admin:1234@cluster0.nktfur3.mongodb.net/?retryWrites=true&w=majority"
db_name = "lime"

collection_name = "users"  # Cambia el nombre de la colección a "users"

client = MongoClient(uri)
db = client[db_name]
collection = db[collection_name]

# Insertar datos de usuarios en la colección
insert_results = collection.insert_many(user_data_list)

if insert_results.acknowledged:
    for inserted_id in insert_results.inserted_ids:
        print(f"Documento insertado con el ID: {inserted_id}")
else:
    print("Fallo al insertar documentos de usuario.")
