# Lime
Proyecto de MongoDB para Diseño de Bases de Datos II

# Diseño de Bases de Datos II

**Profesor:** Ing. Fernando Zapata  
**Universidad de Mendoza**  
**Facultad de Ingeniería**  

---

## MongoDB - Gestión de Datos

### Documento en MongoDB
Un documento en MongoDB consiste en un conjunto de pares **CLAVE - VALOR**:
```json
{
  "nombre": "Juan",
  "apellido": "Perez",
  "edad": 20
}
```

---

## Operaciones Básicas en MongoDB

### Visualización
1. Listar bases de datos:
   ```shell
   show databases
   ```

2. Seleccionar base de datos activa:
   ```shell
   use miBase
   db
   ```

3. Eliminar base de datos:
   ```shell
   db.dropDatabase()
   ```

### Creación de Colecciones
Crear una colección:
```shell
db.createCollection("miColeccion")
```

Listar colecciones:
```shell
show collections
```

### Creación de Documentos
Insertar un documento:
```shell
use agenda
db.contactos.insertOne({ "nombre": "Juan", "apellido": "Perez" })
```

### Consultas Básicas
Consultar documentos:
```shell
use agenda
db.contacto.find().pretty()
```

Modificar documentos:
```shell
db.contacto.updateOne({ "nombre": "Juan" }, { $set: { "edad": 40 } })
```

Eliminar documentos:
```shell
db.contacto.remove({ "nombre": "Juan" })
```

Eliminar una colección completa:
```shell
db.contacto.drop()
```

---

## Tipos de Datos en MongoDB

Tipos heredados de JSON y extendidos en MongoDB:

- **null:** `{ "x": null }`
- **boolean:** `{ "x": true }`
- **number:** `{ "x": 3.14 }`
- **string:** `{ "x": "foobar" }` (UTF-8)
- **date:** `{ "x": new Date() }`
- **regex:** `{ "x": /foobar/i }`
- **array:** `{ "x": ["a", "b", "c"] }`
- **embedded docs:** `{ "x": { "foo": "bar" } }`
- **object id:** `{ "x": ObjectId() }`
- **binary data:** solo tipo no UTF-8
- **code:** `{ "x": function() { /* ... */ } }`

---

## Gestión de Documentos

### Insertar Varios Documentos
```shell
db.coleccion.insertMany([{ "_id": 0 }, { "_id": 1 }, { "_id": 2 }, { "_id": 3 }])
```

### Iterar sobre Documentos
Insertar documentos en un bucle:
```javascript
for (var i = 0; i < 1000; i++) {
  db.colec_prueba.insert({ "clave": "dato" + i, "num": i, "otro": i * 2 })
}
```

### Modificar Documentos
```shell
db.contacto.update({ "_id": ObjectId("5f419ff9a6d4d938d116923b") }, { "$set": { "nombre": "Flor" } })
```

---

## Operaciones con Arrays

Agregar elementos al final de un array:
```shell
db.contacto.update({ _id: 1 }, { $push: { tags: "música" } })
```

Eliminar el último elemento del array:
```shell
db.contacto.update({ _id: 1 }, { $pop: { tags: 1 } })
```

Eliminar elementos específicos:
```shell
db.contacto.update({ _id: 1 }, { $pull: { tags: "música" } })
```

Agregar múltiples elementos:
```shell
db.contacto.update({ _id: 1 }, { $push: { tags: { $each: ["piano", "violín", "guitarra", "saxo"] } } })
```

---

## Consultas y Filtrado de Datos

### Consultas Básicas
Consultar todos los documentos:
```shell
db.micoleccion.find()
db.micoleccion.findOne()
db.micoleccion.find({ "edad": 40, "nombre": "Juan" })
```

Consultar con rango de valores:
```shell
db.contacto.find({ "edad": { "$gte": 18, "$lte": 30 } })
```

---

## Consultas Avanzadas

### Relaciones en MongoDB

- **Uno a Uno**
- **Uno a Muchos**
- **Muchos a Muchos**

#### Ejemplo: Relaciones Uno a Muchos
```json
// Colección Carrera
{
  "_id": 3,
  "nombre": "Abogacía",
  "facultad_Id": 2
}

// Colección Facultad
{
  "_id": 2,
  "nombre": "Derecho"
}
```

### Ejemplo: Relaciones Muchos a Muchos
```json
// Colección Usuario
{
  "_id": 1,
  "apellido": "Perez",
  "nombre": "Juan",
  "grupos": [1, 3, 7]
}

// Colección Grupo
{
  "_id": 3,
  "nombre": "Andinismo",
  "usuario": [1, 3, 9, 15]
}
```

---

## Agregaciones en MongoDB

### Método `aggregate`

Filtrar y agrupar documentos:
```shell
db.miColeccion.aggregate([
  { $match: { condicion: "alguna_condicion" } },
  { $group: { _id: null, suma: { $sum: "$valor" } } }
])
```

Proyectar campos específicos:
```shell
db.empleados.aggregate([
  { $project: { apellido: 1, nombre: 0, salario: 1 } }
])
```

Renombrar claves y calcular nuevos valores:
```shell
db.empleados.aggregate([
  { $project: { nueva_clave: "$clave_original", nuevo_calculado: { $add: ["$clave1", "$clave2"] } } }
])
```

Aplicar expresiones condicionales:
```shell
db.empleados.aggregate([
  { $project: { campoResultado: { $cond: { if: { $gte: ["$edad", 18] }, then: "Adulto", else: "Menor" } } } }
])
```

---

### Consultas Relacionadas con `$lookup`
Unir documentos con otra colección:
```shell
db.clientes.aggregate([
  { $match: { _id: ObjectId("XXXX") } },
  { $lookup: { from: "pedidos", localField: "_id", foreignField: "clienteId", as: "pedidosDelCliente" } }
])
```
