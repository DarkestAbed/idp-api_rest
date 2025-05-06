# Integracion de Plataformas
## Sesion 7: APIs REST
En esta sesión, revisamos el desarrollo de una API REST usando FastAPI en Python.

# Que es una API?
API, o _Application Programming Interface_, es una conexión entre dos programas mediante una interfaz programable y programática. De acuerdo a [AWS](https://aws.amazon.com/what-is/api/),

> (🇬🇧) APIs are mechanisms that enable two software components to communicate with each other using a set of definitions and protocols. For example, the weather bureau’s software system contains daily weather data. The weather app on your phone “talks” to this system via APIs and shows you daily weather updates on your phone.

> (🇨🇱) Las APIs son mecanismos que permiten que dos componentes de software se comuniquen entre ellas usando un conjunto de definiciones y proocolos. Por ejemplo, el sistema de software de una agencia climática contiene datos diarios del clima. La aplicación de clima de tu teléfono "habla" con este sistema vía APIs, y muestra actualizaciones diarias del clima.

# Que es una API REST?
Una API REST es un tipo particular de API. REST es un acrónimo de **Representational State Transfer** (o _Transferencia de Estado Representacional_), y es un tipo de API que se ejecuta sobre HTTP(S), y contiene un número de métodos que facilitan la comunicación entre sistemas.

# Como desarrollar una API REST en Python?
En Python 3, la versión actual y con soporte de Python, existen varios frameworks disponibles. Los más comunes son:

* Django REST Framework: Construido sobre Django, ofrece una gran cantidad de herramientas para crear APIs sofisticadas rápidamente. Incluye serializadores, autenticación, permisos y documentación automática. Es ideal para proyectos grandes y complejos que ya utilizan Django o buscan una solución integral.
    * [Página oficial de Django REST Framework](https://www.django-rest-framework.org/)
* Flask: Un microframework minimalista y muy flexible. Permite a los desarrolladores elegir las herramientas que necesitan, lo que lo hace ideal para construir APIs pequeñas y personalizadas. Requiere la selección e integración de bibliotecas adicionales para funcionalidades como serialización y validación.
    * [Página oficial de Flask](https://flask.palletsprojects.com/)
* FastAPI: Un framework moderno de alto rendimiento, basado en Python 3.8+ con type hints. Ofrece serialización y validación de datos automática con Pydantic, inyección de dependencias y documentación automática con OpenAPI. Está diseñado para construir APIs rápidas y robustas con poco código.
    * [Página oficial de FastAPI](https://fastapi.tiangolo.com/)

## FastAPI
Como fue mencionado, FastAPI es un framework moderno, que corre en Python 3.8+. Su potencia y versatilidad se reflejan en su diseño minimalista, y la posibilidad de tener un producto disponible y desplegable en 5 minutos (no es una exageración!).

FastAPI se ha posicionado rápidamente como uno de los frameworks más populares y potentes para construir APIs (Interfaces de Programación de Aplicaciones) con Python. Su diseño se centra en la velocidad de desarrollo, el alto rendimiento (gracias a Starlette y Pydantic), la robustez y la facilidad de uso.

#### Características Clave que lo Hacen Destacar:
* Alto Rendimiento: FastAPI se basa en Starlette para la parte web y ASGI (Asynchronous Server Gateway Interface), lo que le permite manejar concurrencia de manera eficiente y alcanzar un rendimiento comparable a frameworks de Node.js y Go. Esto lo hace ideal para aplicaciones que requieren una alta capacidad de respuesta.
* Desarrollo Rápido: La sintaxis intuitiva y las características integradas permiten a los desarrolladores construir APIs de manera significativamente más rápida. La validación de datos, la serialización y la documentación automática se manejan con mínimas líneas de código.
* Validación de Datos con Pydantic: La integración con Pydantic permite la definición de modelos de datos utilizando Python type hints estándar. Pydantic se encarga de la validación de los datos entrantes y salientes, asegurando la integridad de la información y proporcionando mensajes de error claros y útiles.
* Serialización Automática de Datos: Al utilizar los modelos de Pydantic, FastAPI automáticamente serializa los datos de Python a formatos estándar como JSON para las respuestas de la API.
* Documentación Automática con OpenAPI y Swagger UI/ReDoc: Una de las características más atractivas de FastAPI es su capacidad para generar automáticamente documentación interactiva de la API utilizando el estándar OpenAPI. Esto incluye interfaces de usuario como Swagger UI y ReDoc, lo que facilita la comprensión y prueba de la API por parte de los desarrolladores.
* Soporte Nativo para Asincronía: FastAPI está diseñado desde cero para trabajar con código asíncrono (async y await). Esto simplifica la escritura de código concurrente y no bloqueante, esencial para aplicaciones de alto rendimiento que manejan múltiples solicitudes simultáneamente.
* Inyección de Dependencias: FastAPI incorpora un potente sistema de inyección de dependencias. Esto facilita la reutilización de código, la gestión de dependencias (como conexiones a bases de datos o autenticación) y la mejora de la estructura y la capacidad de prueba de la aplicación.
* Seguridad Integrada: FastAPI proporciona herramientas y facilidades para implementar mecanismos de seguridad comunes, como autenticación (OAuth2 con JWT) y manejo de cookies y encabezados.
* Basado en Estándares: Al utilizar OpenAPI para la documentación y Pydantic para la validación de datos, FastAPI se adhiere a estándares ampliamente adoptados en la industria, lo que facilita la integración con otras herramientas y sistemas.

#### Ejemplo Básico:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

En este ejemplo sencillo, se definen dos rutas de API (`/` y `/items/{item_id}`). FastAPI automáticamente maneja la validación del tipo de item_id como entero y permite un parámetro opcional q. Además, generaría la documentación OpenAPI para estas rutas.

#### ¿Cuándo Considerar FastAPI?
FastAPI es una excelente opción para:
* Construir APIs de alto rendimiento.
* Proyectos que requieren una validación de datos robusta.
* APIs que necesitan documentación automática y actualizada.
* Aplicaciones que se benefician del código asíncrono.
* Equipos que buscan un framework moderno y con una curva de aprendizaje relativamente suave.

En resumen, FastAPI combina lo mejor de la tipificación estática de Python con conceptos modernos de desarrollo de APIs, ofreciendo una experiencia de desarrollo eficiente, un rendimiento excepcional y una gran cantidad de características integradas que simplifican la creación de APIs robustas y escalables.

# Instalando FastAPI
La instalación de FastAPI es muy sencilla. Si bien no es un requisito, se recomienda instalarlo en un proyecto dentro de un _ambiente virtual_.

## Ambientes virtuales en Python
En el desarrollo de software con Python, es común trabajar en múltiples proyectos simultáneamente. Cada uno de estos proyectos puede tener dependencias específicas en diferentes versiones de las mismas bibliotecas. Aquí es donde entran en juego los entornos virtuales.

Un entorno virtual en Python es un directorio aislado que contiene una instalación de Python específica, junto con todas las bibliotecas y dependencias necesarias para un proyecto en particular. Este aislamiento garantiza que las dependencias de un proyecto no interfieran con las de otro, evitando conflictos de versiones y manteniendo cada proyecto autocontenido y reproducible.

#### Por qué son importantes los ambientes virtuales en Python?
* Aislamiento de Dependencias: El beneficio principal es el aislamiento. Sin entornos virtuales, todas las bibliotecas se instalarían globalmente en el sistema Python. Esto puede llevar a situaciones donde dos proyectos requieren versiones diferentes de la misma biblioteca, causando errores y dificultando la gestión. Un entorno virtual asegura que cada proyecto tenga su propio conjunto de dependencias, sin afectar a otros.
* Reproducibilidad: Al mantener una lista clara de las dependencias específicas de un proyecto dentro de su entorno virtual, se facilita la reproducción del entorno en otra máquina. Esto es crucial para la colaboración, el despliegue y la garantía de que el software funcione de manera consistente en diferentes entornos.
* Gestión de Versiones: Los entornos virtuales permiten especificar las versiones exactas de las bibliotecas que necesita un proyecto. Esto es vital porque las actualizaciones de las bibliotecas pueden introducir cambios que rompen el código existente. Al fijar las versiones en el entorno virtual, se asegura la estabilidad del proyecto.
* Limpieza del Sistema Global: Al confinar las dependencias a entornos virtuales, se mantiene limpio el entorno Python global del sistema operativo, evitando la acumulación de bibliotecas innecesarias.

#### Creación de ambientes virtuales en Python 3.12
Python 3.3 introdujo el módulo `venv` como la herramienta estándar para crear y gestionar entornos virtuales. Para crear un entorno virtual en Python 3.12, sigue estos pasos:

1. Abre la Terminal o Símbolo del Sistema: Navega hasta el directorio donde deseas crear el proyecto o el directorio donde quieres alojar tu entorno virtual.
2. Ejecuta el Comando `venv`: Utiliza el siguiente comando, reemplazando `<nombre_del_entorno>` con el nombre que deseas darle a tu entorno virtual (por ejemplo, `mi_entorno`, `.venv`, `env`). Es común usar .`venv` o `env` para indicar que es un directorio de entorno virtual.

```bash
python3.12 -m venv <nombre_del_entorno>
```

Por ejemplo:

```bash
python3.12 -m venv mi_entorno
```

Este comando ejecutará el módulo `venv` con la instalación de Python 3.12 y creará un directorio llamado `mi_entorno` (o el nombre que hayas elegido). Dentro de este directorio, `venv` copiará el ejecutable de Python, la biblioteca estándar pip y otros archivos necesarios para un entorno Python aislado.

#### Estructura de directorios en un venv
Una vez creado el entorno virtual, el directorio contendrá una estructura similar a la siguiente (los nombres exactos pueden variar ligeramente según el sistema operativo):

* **`bin`** (en macOS y Linux) o **`Scripts`** (en Windows): Contiene los ejecutables de Python (python, python3) y pip (pip, pip3) específicos de este entorno virtual, así como otros scripts relacionados con las bibliotecas instaladas.
* **`include`**: Puede estar vacío o contener archivos de encabezado para compilar extensiones C.
* **`lib`**: Contiene la copia de la biblioteca estándar de Python y el subdirectorio site-packages, donde se instalarán las bibliotecas y dependencias específicas del proyecto mediante pip.
* **`pyvenv.cfg`**: Un archivo de configuración que contiene información sobre la ruta del intérprete de Python base utilizado para crear el entorno.

#### Activar un entorno virtual
Antes de comenzar a trabajar en tu proyecto dentro del entorno virtual, necesitas activarlo. La activación configura tu shell para usar el intérprete de Python y los scripts que se encuentran dentro del directorio del entorno virtual.

* En macOS y Linux:

Navega al directorio del entorno virtual y ejecuta el script activate que se encuentra dentro del directorio `bin`:

```bash
source <nombre_del_entorno>/bin/activate
```

Por ejemplo:

```bash
source mi_entorno/bin/activate
```

Una vez activado, verás el nombre del entorno virtual entre paréntesis al principio de tu línea de comandos, por ejemplo:

`(mi_entorno) tu_usuario@tu_maquina:~/tu_proyecto$`.

* En Windows (con `cmd`):

Navega al directorio del entorno virtual y ejecuta el script `activate.bat` que se encuentra dentro del directorio Scripts:

```bash
.\<nombre_del_entorno>\Scripts\activate.bat
```
Por ejemplo:

```bash
.\mi_entorno\Scripts\activate.bat
```

Al igual que en macOS y Linux, el nombre del entorno virtual aparecerá entre paréntesis al principio de la línea de comandos: 

`(mi_entorno) C:\tu_proyecto>`

* En Windows (con Powershell):

Navega al directorio del entorno y ejecuta:

```powershell
.\<nombre_del_entorno>\Scripts\Activate.ps1
```

Reemplaza <nombre_del_entorno> con el nombre de tu entorno virtual. Verás el nombre del entorno entre paréntesis al inicio de tu prompt.

#### Uso de pip dentro del Entorno Virtual
Una vez que el entorno virtual está activado, cualquier paquete que instales utilizando pip se guardará dentro del directorio `site-packages` de ese entorno virtual, en lugar de la instalación global de Python.

Por ejemplo, para instalar el framework requests dentro de tu entorno virtual activado, ejecutarías:

```bash
pip install requests
```

Para ver la lista de paquetes instalados en tu entorno virtual, puedes usar el comando:

```bash
pip freeze
```

Es una buena práctica guardar la lista de dependencias de tu proyecto en un archivo `requirements.txt`. Puedes crear este archivo ejecutando `pip freeze > requirements.txt` dentro del entorno virtual activado. Luego, en otra máquina o para configurar un nuevo entorno, puedes instalar todas las dependencias de una vez utilizando:

```bash
pip install -r requirements.txt
```

#### Desactivación del Entorno Virtual
Cuando termines de trabajar en tu proyecto, puedes desactivar el entorno virtual para volver a tu entorno Python global. Simplemente ejecuta el comando deactivate en la terminal:

```bash
deactivate
```

El nombre del entorno virtual desaparecerá del principio de la línea de comandos.

## Instalación de FastAPI

FastAPI tiene varios tipos de instalación disponibles. Nos enfocaremos en dos: la instalación _vainilla_ y la instalación `standard`, que contiene la CLI `fastapi`.

Para instalar FastAPI, debemos ejecutar la siguiente instrucción:

```bash
pip install fastapi
```

con nuestro ambiente virtual activado.

Si deseamos usar la CLI `fastapi`, debemos ejecutar la siguiente instrucción:

```bash
pip install fastapi[standard]
```

Con ello tenemos disponible el framework para trabajar. Podemos verificar la instalación `standard` con la instrucción:

```bash
which fastapi

> {raíz del proyect}/{ambiente virtual}/bin/fastapi
```

# Descripción de la API `hello.py`

```python
# hello.py

## Importamos la clase FastAPI desde el modulo FastAPI, para poder crear una app de tipo API
from fastapi import FastAPI
## Importamos desde [Pydantic](https://docs.pydantic.dev/latest/) la clase BaseModel, y el validador de
## texto EmailStr, para poder crear un campo de tipo correo electronico
from pydantic import BaseModel, EmailStr


## Creamos una aplicacion de FastAPI, con algunos parametros
app: FastAPI = FastAPI(
    debug=True,
    title="API de prueba",
    version="0.0.1",
)


## Para poder pedir datos en un request de tipo POST, debemos tener una clase que herede desde BaseModel
## de Pydantic. Esto permitira habilitar las validaciones de datos necesarias
class UserLogin(BaseModel):
    user: str
    pswd: str
    email: EmailStr


## Nuestro primer endpoint sera en la raiz del sitio (`localhost/`). Para ello, decoramos la funcion a ejecutar
## con `@app.<metodo>`, donde nuestro primer metodo sera GET
@app.get("/")
## Definimos la funcion a ejecutar en la ruta `localhost:<puerto>/`
### PYTHONTIP: El guion bajo o _underscore_ tiene varios roles en Python ([text](https://www.geeksforgeeks.org/underscore-_-python/))
### En este caso, lo usamos para definir una funcion cuyo nombre no es relevante
def _():
## El cuerpo de nuestra funcion solo retorna un diccionario, con un mensaje
    return {
        "message": "Hello World from my first API",
    }


## Nuestro segundo endpoint se ubicara en la ruta `localhost/login`. Como es un metodo POST, se decora con
## `@app.post`
@app.post("/login")
## Esta funcion tiene un parametro de tipo UserLogin, la clase definida en la linea 37. Asi, al enviar un request
## a este endpoint, se requerira la data presente en la clase definida, en formato JSON
def _(payload: UserLogin):
## Es notable que, como definimos un modelo de Pydantic, podemos acceder a sus miembros con notacion de punto
## (<objeto>.<atributo>)
    return {
        "message": f"user {payload.user} was successfully created",
        "details": {
            "user_name": payload.user,
            "user_email": payload.email,
            ### PYTHONTIP: Mala practica de seguridad. NUNCA se deben mostrar ni enviar credenciales no encriptadas
            "user_password": payload.pswd,
        }
    }

```
