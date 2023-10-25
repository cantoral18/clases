#importar mi base de datos
from bd import*#la variable usuario de mi bd estara disponibleen este archivo 

#crear clase para usuario
#esta clase  tendra los siguientes metodos
#verificar si usuario esta registrado o existe en mis registro
#validar usuario y password
from bd import usuario

class usuario:
    def verificar_usuario(self,usuario):
        return usuario in self.usuario
    if verificar_usuario.usuario(usuario):
        print("si esta en el registro")
    else:
        print("no esta registrado")
    def verificar_u_p(self,usuario,password):
        if usuario in self.usuario:
            return self.usuario[usuario]==password
        return False
    if verificar_u_p("usuario",password):
        print(verificacion valida.)
    else:
        print("credenciales invalidas.")