import os
import importlib
import gradio as gr
from groq import Groq
from dotenv import load_dotenv
import config

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la API key de Groq
api_key = os.getenv("GROQ_API_KEY")

# Inicializar el cliente de Groq
client = Groq(api_key=api_key)

# Función para cargar el prompt del sistema desde config.py
def load_system_prompt():
    try:
        # Recargamos el módulo en cada mensaje para que tome los cambios en caliente
        importlib.reload(config)
        return config.SYSTEM_PROMPT
    except Exception as e:
        print(f"Error cargando config.py: {e}")
        return "Eres un asistente útil."

# Función principal del chat que interactúa con la API de Groq
def chat_with_groq(message, history):
    # Cargar el prompt cada vez permite cambiarlo en caliente editando config.py
    system_prompt = load_system_prompt()
    
    # 1. Agregar el prompt del sistema al inicio
    messages = [{"role": "system", "content": system_prompt}]
    
    # 2. Agregar el historial de la conversación previa para mantener la memoria
    for item in history:
        if isinstance(item, dict):
            messages.append({"role": item["role"], "content": item["content"]})
        else:
            user_msg, assistant_msg = item
            messages.append({"role": "user", "content": user_msg})
            if assistant_msg:
                messages.append({"role": "assistant", "content": assistant_msg})
            
    # 3. Agregar el mensaje actual del usuario
    messages.append({"role": "user", "content": message})
    
    try:
        # Llamar a la API de Groq
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile", # Puedes cambiarlo a llama3-70b o mixtral-8x7b-32768 si prefieres
            messages=messages,
            stream=True # Para mostrar la respuesta casi instantáneamente
        )
        
        # Procesar la respuesta en streaming
        partial_message = ""
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                partial_message += chunk.choices[0].delta.content
                yield partial_message
                
    except Exception as e:
        yield f"**Error al comunicarse con la API:**\n{str(e)}\n\n*Asegúrate de haber puesto tu GROQ_API_KEY en el archivo .env*"

# Crear la interfaz gráfica con Gradio
demo = gr.ChatInterface(
    fn=chat_with_groq,
    title="⚡ Chatbot ultra rápido con Groq",
    description="Un chatbot sencillo y con memoria. Edita el archivo `config.py` para cambiar las instrucciones (prompt) y `.env` para agregar tu GROQ_API_KEY.",
    examples=["Hola, ¿qué puedes hacer?", "Explícame qué es Groq de forma sencilla."],
)

if __name__ == "__main__":
    # Lanzar la aplicación en local
    demo.launch()
