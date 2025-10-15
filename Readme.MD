# 🛡️ API con Doble Middleware: CORS y Control de Dispositivo

## 📝 Descripción del Proyecto
Este proyecto de **FastAPI** implementa un doble sistema de Middleware:
1.  **CORSMiddleware**: Permite la comunicación segura de origen cruzado.
2.  **Middleware Personalizado (`DeviceControlMiddleware`)**: Impone una regla de seguridad que **bloquea** el acceso a la API si el encabezado `User-Agent` del cliente contiene la palabra `"Mobile"`.

## ⚙️ Requisitos
* Python 3.10+
* FastAPI, Uvicorn, python-multipart

# Inicia el servidor en el puerto 8001
'uvicorn main:app --reload --port 8001'
## 💻 Instrucciones de Instalación y Ejecución

Sigue estos pasos directos para ejecutar la API localmente:

### 1. Instalación de Dependencias
Asegúrate de tener un entorno virtual activo y luego instala los paquetes necesarios:
```bash
pip install fastapi "uvicorn[standard]"

