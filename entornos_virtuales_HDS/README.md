# ENTORNOS VIRTUALES 
## para crear un entorno virtual
1. nos ubicamos en la carpeta que deamos crear el entorno virtual
```bash
cd<ruta del archivo>
# ejemplo
cd nombre_carpeta/entorno_uno
```
2. creamos el entorno virtual con el siguiente comando
```bash
python -m venv<nombre de nuestro archivo>
# ejemplo
python -m venv venv_uno
```
3. para activar entorno virtual con el gitbash como terminal predeterminado corremos solo los windows
```bash
source venv_uno/scripts/activate
```
## observacion:
para poder ejecutarlo en powershell como terminal ejecuta los siguientes comandos
```
venv/scripts/activate.ps1
```  
## para instalar paquetes en nuestros entorno virtuale
1. primero verificamos que no tengamos el paquete instalado y lo listamos con el siguiente comando 
## debemos tener acvtivado nuestro entorno virtual primero
```
pip list
```
2. luego instalaremos con el siguiente comando
```
pip install<nombre del paquete>
#ejemplo
pip install pandas
```