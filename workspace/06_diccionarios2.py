mi_mascota=[
    {"nombre":"Toby","animal":"perro","edad":1},
    {"nombre":"luna","animal":"yegua","edad":5}
]
#recorre y acceder a cada dato utilizado for
for mascota in mi_mascota:
    print (f"{mascota['nombre']},{mascota['animal']},{mascota['edad']}")