# Proyecto MongoDB

## Condiciones

- Importar base de datos
- Crear base de datos
- Recargar base de datos
- Crear colección
- Eliminar colección
- Eliminar base de datos
- Crear usuario
- Eliminar usuario
- Hacer consultas
- Cerrar la base de datos

## Comandos útiles mongosh

### Encontrar users que incluyan un substring en el username
```javascript
db.users.find({"user_name": /victor/i})
```

### Obtener el `_id` de los usuarios que incluyan un substring en el username
```javascript
db.users.find({"user_name": /victor/i}, {_id: 1})
```

### Obtener todos los posts que incluyan el `_id` de un usuario
```javascript
db.posts.find({"author_id": db.users.findOne({"user_name": "victor"})._id})
```
