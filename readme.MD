# Transcriptor y Resumidor de Reuniones con IA

## 📚 Analogía: Transcriptor y Resumidor de Reuniones con IA

Crea un resumen de grabación de una reunión. Por cierto ***muy eficiente***

1. **Escucha la reunión** (transcribe el audio a texto).
2. **Lee y entiende lo que se dijo** (resume el texto con IA).
3. **Te entrega un resumen claro** (genera un audio breve y un archivo de texto).
4. **Organiza la información** (puedes compartir los resultados fácilmente).

Así, no necesitas escuchar toda la reunión: Transcriptor y Resumidor de Reuniones con IA te da solo lo más importante, listo para compartir o consultar.

---

## ⚙️ Explicación técnica breve

- **Transcripción:** Usa la API de OpenAI Whisper para convertir el audio de la reunión en texto.
- **Resumen:** Usa ChatGPT (modelo GPT-4o) para resumir la transcripción.
- **Audio resumen:** Convierte el resumen de texto a voz usando Google Text-to-Speech (`gtts`).
- **Exportación:** Guarda el resumen en texto y audio.
- En construcción...**Compartir:** Muestra las rutas de los archivos generados (puedes integrar WhatsApp o email fácilmente). 

---

## 📝 Estructura del proyecto
curso-chatbots/ │ ├── src/ │ └── transcriptor/ │ ├── transcriptor.py │ └── audio/ │ └── reunion.mp3 ├── requirements.txt ├── README.md └── ...


---

## 📦 requirements.txt

```txt
openai>=1.0.0
gtts

🚀 ¿Cómo usar?
1.Coloca tu archivo de audio en src/transcriptor/audio/reunion.mp3.
2.Configura tu clave de OpenAI en la variable de entorno OPEN<vscode_annotation details='%5B%7B%22title%22%3A%22hardcoded-credentials%22%2C%22description%22%3A%22Embedding%20credentials%20in%20source%20code%20risks%20unauthorized%20access%22%7D%5D'>AI</vscode_annotation>_API_KEY.
3. Instala dependencias:
pip install -r requirements.txt
4. Ejecuta el script:
python src/transcriptor/transcriptor.py
5. Revisa los archivos generados y compártelos según necesites.

🛠️ Personalización
Puedes integrar segmentación de hablantes y envío por WhatsApp con Twilio.
Adapta el script para otros idiomas cambiando el parámetro de gtts.

👤 Autor
Nombre: Luis Tobar
GitHub:https://github.com/LuisTo503
correo:rgbmultimedios@gmail.com 
Fecha de creación: 2025/05/17

📄 Licencia
Este proyecto es de uso educativo y demostrativo.
