# #lambda un funcion que se ejecuta
# hola=lambda a,b:print(a+b)

# #funcion normald
# def suma(a,b):
#     print(a+b)
# suma(4,6)
# hola(10,20)

# #if terminario
# ternario="soy verdad ternario"if True else"soy falso ternario"
# print(ternario)

# #if normal
# if True:
#     print("soy verdad")
# else:
#     print("soy mentira")


    
lista_alumnos=[
    {
        "nombre":"edwin",
        "edad":"17"
        "hobby":"danzar"
        "flaquita":" melody"
    },
    {
        "nombre":"luis",
        "edad":"23"
        "hobby":"bailar"
        "flaquita":" melody"
    },
    {
        "nombre":"fernando",
        "edad":"51"
        "hobby":"dormir"
        "flaquita":" carmen"
    },
    {
        "nombre":"ciro",
        "edad":"20"
        "hobby":"caminar"
        "flaquita":" fer"
    },
    
]   
print(f"todo mis alumnitos{lista_alumnos}")
fans_melody=list(filter(lambda par:par["flaquita"]=="melody",lista_alumnos))
print(f"los que quieren con melody{fans_melody}")



nuevo_objeto=list(map(lambda par:{"nombre_alumno":par{"nombre"},"germita":par["flaquita]},lista_alumno))
print(nuevo_objeto)