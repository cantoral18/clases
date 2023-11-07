from rich import print
from rich,Markdown import Markdown
#titulo
edad=20
respuesta="es mayor" if edad<17 else " es menor de edad"
texto="""
#parrafo
```bash
git commit -m"titulo"  -m "cuerpo del commit"
#comentario
```
*lista
*lista
>informacion valiosa
()



""",format(respuesta)


print(respuesta)