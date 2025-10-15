# 🚀 API de Personas - ITI-621 IIIC-2025

##  Descripción del Proyecto
Este proyecto es una API RESTful desarrollada con **FastAPI** como parte del curso ITI-621 IIIC-2025. La API proporciona un servicio básico para gestionar y consultar información de personas, e incorpora el uso del middleware CORS para habilitar la comunicación entre diferentes orígenes.

##  Características Principales
- **Endpoint `/`**: Punto de acceso raíz que devuelve un mensaje de bienvenida.
- **Endpoint `/hello/`**: Un endpoint simple para probar la conectividad de la API.
- **Endpoint `/api/personas`**: Un endpoint que devuelve los datos de una persona en formato JSON.
- **Middleware CORS**: Configurado para permitir solicitudes de orígenes cruzados, lo que facilita el desarrollo de aplicaciones frontend que consuman esta API.

## ¿Qué es el Middleware CORS?
El **middleware CORS (Cross-Origin Resource Sharing)** es un componente de seguridad esencial en el desarrollo web. Su función es permitir que un servidor **(la API)** controle qué orígenes **(dominios)** tienen permiso para acceder a sus recursos. Los navegadores web, por defecto, imponen una política de seguridad que restringe las solicitudes de un origen a otro, pero CORS flexibiliza esta regla de forma controlada.

En este proyecto, el middleware CORS está configurado para permitir que aplicaciones web que se ejecuten en un dominio diferente, como un frontend en `http://localhost`, puedan realizar solicitudes a esta API sin ser bloqueadas por el navegador.

##  Tecnologías Utilizadas
- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- **python-multipart**

##  Instalación y Configuración
Sigue estos pasos para poner en marcha el proyecto:

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/nombre-del-repo.git](https://github.com/tu-usuario/nombre-del-repo.git)
    cd nombre-del-repo
    ```

2.  **Crea un entorno virtual (opcional pero recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install fastapi "uvicorn[standard]" python-multipart
    ```

4.  **Ejecuta la API:**
    ```bash
    uvicorn main:app --reload
    ```
    La API estará disponible en `http://127.0.0.1:8000`.

##  Uso de la API
Puedes probar los endpoints directamente en tu navegador o utilizando herramientas como `curl` o Postman.

- **Acceder a la raíz:**
    `http://127.0.0.1:8000/`

- **Acceder al endpoint de saludo:**
    `http://127.0.0.1:8000/hello/`

- **Acceder a la información de la persona:**
    `http://127.0.0.1:8000/api/personas`

##  Autor
- **Nombre:** [Tu nombre aquí]
- **GitHub:** [Tu enlace a GitHub]