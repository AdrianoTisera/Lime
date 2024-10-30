from faker import Faker
from datetime import datetime
from pymongo import MongoClient

fake = Faker()

# Generar 2000 registros de datos de usuarios con ID incremental
user_data_list = [
    {
        "_id": user_id,
        "name": f"{fake.first_name()} {fake.last_name()}",
        "user_name": f"{fake.first_name().lower()}{fake.last_name().lower()}{fake.random_int(min=1, max=999)}",
        "email": fake.email(),
        "password": fake.password(length=12),  # Contraseña aleatoria de 12 caracteres
        "profile_picture": fake.file_path(extension="jpg"),  # Ruta aleatoria de imagen
        "created_at": datetime.utcnow().isoformat()  # Fecha y hora actual en formato ISO
    }
    for user_id in range(1, 2001)  # Cambiamos para que el rango sea de 1 a 2000 (inclusive)
]

# Imprime los primeros 5 registros para verificar
for user in user_data_list[:5]:
    print(user)

# Conexión a la base de datos MongoDB
uri = "mongodb+srv://admin:1234@cluster0.nktfur3.mongodb.net/?retryWrites=true&w=majority"
db_name = "lime"
collection_name = "users"

client = MongoClient(uri)
db = client[db_name]
collection = db[collection_name]

# Insertar datos de usuarios en la colección
try:
    insert_results = collection.insert_many(user_data_list)
    print(f"Documentos insertados: {len(insert_results.inserted_ids)}")
except Exception as e:
    print(f"Error al insertar documentos: {e}")
