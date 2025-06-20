# app.py

import gradio as gr
from whisper_module import record_audio, load_whisper_model, transcribe_audio_with_model
from llm_module import ask_ollama
from tts_module import speak_text

# Load Whisper once
whisper_model = load_whisper_model("small")

chat_history = []

def handle_voice():
    record_audio(duration=5)
    user_input = transcribe_audio_with_model(whisper_model, "input.wav")
    assistant_response = ask_ollama(user_input)
    speak_text(assistant_response)

    # Append to global chat history
    chat_history.append((user_input, assistant_response))
    return chat_history

with gr.Blocks(theme=gr.themes.Soft(primary_hue="blue")) as demo:
    gr.Markdown(
        """
        <h1 style="text-align: center; color: #2c3e50;">🎙️ AI Voice Assistant</h1>
        <p style="text-align: center; font-size: 16px; color: #555;">
        Click the button to talk. The assistant will listen, think, and speak back to you.
        </p>
        """,
        elem_id="banner"
    )

    with gr.Row():
        with gr.Column(scale=1, min_width=200):
            start_button = gr.Button("🎧 Start Talking", size="lg")

        with gr.Column(scale=3):
            chatbot = gr.Chatbot(label="Conversation", show_copy_button=True, height=400)

    start_button.click(fn=handle_voice, outputs=chatbot)

demo.launch()
