# ⚡ Chatbot Rápido con Groq y Gradio

Un chatbot ligero, rápido y configurable construido con Python. Utiliza la interfaz de usuario de **Gradio** y se conecta al poderoso modelo `llama-3.3-70b-versatile` a través de la API ultrarrápida de **Groq**. 

Este proyecto está diseñado para ser sencillo de entender y modificar. Cuenta con **soporte de memoria** (recuerda el contexto de la conversación) y un **sistema de prompts dinámico** configurable a través de un archivo externo.

## 🚀 Características principales

*   **Velocidad extrema**: Impulsado por la inferencia ultra rápida de Groq.
*   **Memoria de contexto**: El bot recuerda los mensajes anteriores de la conversación actual.
*   **Prompting dinámico en vivo**: Puedes editar las instrucciones de comportamiento (prompt del sistema) en el archivo `config.py` y el bot adoptará la nueva personalidad en el momento, sin necesidad de reiniciar el servidor.
*   **Prompting Avanzado**: Usa la estructura CRISPE (Contexto, Rol, Instrucción, Salida, Prohibición, Ejemplo) por defecto.
*   **Interfaz elegante**: Gracias a Gradio, tendrás una UI web lista para usar en segundos.

---

## 🛠️ Requisitos previos

Para correr este proyecto necesitas:
1. Tener **Python 3.8+** instalado en tu computadora.
2. Un manejador de paquetes de Python (recomendamos `uv` por su velocidad, o el clásico `pip`).
3. Una **API Key gratuita de Groq**. Puedes obtenerla en [console.groq.com/keys](https://console.groq.com/keys).

---

## ⚙️ Instalación y Configuración

Sigue estos pasos para poner a correr tu chatbot localmente:

### 1. Clonar o descargar el proyecto
Asegúrate de tener todos los archivos en una misma carpeta (incluyendo `app.py`, `config.py`, `requirements.txt` y tu archivo de entorno).

### 2. Configurar tu API Key
Crea un archivo llamado `.env` en la raíz del proyecto (si no existe) y agrega tu clave de API de Groq de esta manera:

```env
GROQ_API_KEY=tu_api_key_aqui
```

### 3. Instalar las dependencias
Abre una terminal en la carpeta del proyecto e instala las librerías necesarias.

Si usas **uv** (recomendado):
```bash
uv add -r requirements.txt
```

Si usas **pip** normal:
```bash
pip install -r requirements.txt
```

---

## 🏃‍♂️ Cómo ejecutarlo

Una vez instaladas las dependencias, simplemente corre el archivo principal:

Usando **uv**:
```bash
uv run app.py
```

Usando **Python** estándar:
```bash
python app.py
```

En la consola verás un mensaje indicando que el servidor está corriendo en una URL local, generalmente:
👉 `http://127.0.0.1:7860`

¡Abre ese enlace en tu navegador web y comienza a chatear!

---

## ✏️ ¿Cómo personalizar la personalidad del Bot?

Abre el archivo `config.py`. Allí encontrarás la variable `SYSTEM_PROMPT`. 
Puedes modificar ese texto usando lenguaje natural para decirle a la IA cómo quieres que actúe. Al guardar el archivo, los cambios aplicarán inmediatamente en los próximos mensajes del chat.
