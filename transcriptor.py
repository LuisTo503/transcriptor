import os

# 1. Grabar reunión (simulado: usar un archivo de audio existente)
AUDIO_FILE = r"C:\Users\Luis\Desktop\ChatBots Complejos\curso-chatbots\src\transcriptor\audio\reunion.mp3"

# 2. Transcripción de audio a texto usando Whisper
def transcribe_audio(audio_path):
    import openai
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    with open(audio_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcript.text

# 3. Resumir el texto con ChatGPT

#Usa client = openai.OpenAI(api_key=...) para crear el cliente.
#Usa client.chat.completions.create(...) para llamar al modelo.
#El modelo recomendado es "gpt-4o" o "gpt-3.5-turbo" (no "gpt-4o-mini").

def summarize_text(text):
    import openai
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    prompt = f"Resume la siguiente transcripción en un resumen claro y breve:\n\n{text}"
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# 4. Generar mensaje de voz (Text to Speech)
def text_to_speech(text, output_path="mensaje_resumen.mp3"):
    from gtts import gTTS
    tts = gTTS(text, lang="es")
    tts.save(output_path)
    return output_path

# 5. Crear diagrama (simulado: exportar texto a archivo)
def create_excalidraw_diagram(summary, output_path="diagrama_excalidraw.txt"):
    # Aquí podrías usar la API de Excalidraw o exportar un archivo .excalidraw
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"Resumen para diagrama:\n{summary}")
    return output_path

# 6. Compartir archivos (simulado: mostrar rutas)
def share_files(*files):
    print("Archivos generados:")
    for f in files:
        print(f" - {f}")
    # Aquí podrías integrar con WhatsApp API, email, etc.

if __name__ == "__main__":
    # Paso 2: Transcribir audio
    texto_transcrito = transcribe_audio(AUDIO_FILE)
    print("Transcripción:", texto_transcrito[:100], "...")

    # Paso 3: Resumir con ChatGPT
    resumen = summarize_text(texto_transcrito)
    print("Resumen:", resumen)

    # Paso 4: Generar mensaje de voz
    audio_resumen = text_to_speech(resumen)

    # Paso 5: Crear diagrama (simulado)
    diagrama = create_excalidraw_diagram(resumen)

    # Paso 6: Compartir archivos
    share_files(audio_resumen, diagrama)