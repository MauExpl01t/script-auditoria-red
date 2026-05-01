use Asignaturas_Inscritas
db.createCollection("Alumnos")
db.Alumnos.insertOne({
  "ID_Alumno": "001",
  "Nombre": "Luis",
  "Apellido": "Lopez",
  "Carrera": "Informatica",
  "Asignaturas": [
    { "ID_Asignatura": "ASIG-0001", "Asignatura": "Matematica" },
    { "ID_Asignatura": "ASIG-0002", "Asignatura": "Lenguaje" }
  ]
})
db.Alumnos.insertMany([
  {
    "ID_Alumno": "002",
    "Nombre": "Ana",
    "Apellido": "Jara",
    "Carrera": "Administracion",
    "Fecha_Nacimiento": "2000-05-03",
    "Asignaturas": [
      { "ID_Asignatura": "ASIG-0010", "Asignatura": "Contabilidad" }
    ]
  },
  {
    "ID_Alumno": "004",
    "Nombre": "Jose",
    "Apellido": "Aracena",
    "Asignaturas": [
      { "ID_Asignatura": "ASIG-0011", "Asignatura": "Administracion" },
      { "ID_Asignatura": "ASIG-0012", "Asignatura": "Finanzas" }
    ]
  }
])

