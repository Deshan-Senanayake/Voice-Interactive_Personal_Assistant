# 🎙️ AI Voice-Interactive Personal Assistant

A fully local, offline-capable voice assistant that lets you **speak** a question and get a **spoken response** — powered by **Whisper**, **LLaMA2 via Ollama**, and **pyttsx3**. Built with a modern and professional **Gradio interface**.

---

## 🚀 Features

- 🎤 Voice Input (Record your question via mic)
- 🧠 Whisper (STT) + LLaMA2 (via Ollama) for question answering
- 🔊 Text-to-Speech using pyttsx3
- 💬 Beautiful chat-style UI with transcript and assistant response
- 🖥️ Runs 100% locally – No API keys needed

---

## 📦 Tech Stack

| Layer              | Technology        |
|-------------------|-------------------|
| Speech-to-Text     | `faster-whisper`  |
| LLM Engine         | `llama2` via `Ollama` |
| Text-to-Speech     | `pyttsx3`         |
| GUI Frontend       | `Gradio` (Blocks) |

---

## 🧑‍💻 Requirements

- Python 3.8+
- Windows/macOS/Linux
- 8GB+ RAM (recommended)
- For GPU support (optional): NVIDIA GPU with CUDA

---

## 📂 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-voice-assistant.git
cd ai-voice-assistant
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> 💡 If you get CUDA or cuDNN errors, change Whisper’s `compute_type="int8_float32"` and `device="cpu"` in `whisper_module.py`.

---

## 🤖 Setup Ollama

1. Download and install **Ollama**:
   👉 https://ollama.com/download

2. Pull a local LLaMA2 model:
   ```bash
   ollama pull llama2
   ```

3. Keep Ollama running in the background:
   ```bash
   ollama run llama2
   ```

---

## 🧠 Run the Assistant

```bash
python app.py
```

- Click "🎧 Start Talking"
- Speak your question (e.g., "What is the capital of Japan?")
- Watch the transcript + assistant response appear
- Listen to the assistant speak back

---

## 📸 Screenshot


---

## 📝 License

MIT License. Use freely for personal, academic, or demo purposes.

---

## 👨‍🎓 Author

**Deshan Senanayake**  
