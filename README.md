# 🤖 Multimodal AI Assistant

A Python-based AI application that combines image captioning, PDF question answering, and audio transcription in a single web interface.

Built using Python, Streamlit, OpenRouter, Groq, and PyMuPDF, this project demonstrates how existing AI models and APIs can be integrated into a practical multimodal application.

## ✨ Features

### 🖼️ Image Captioning
- Upload images in supported formats.
- Generate natural-language descriptions of image content.
- Uses a vision-language model through OpenRouter.

### 📄 PDF Question Answering
- Upload PDF documents.
- Extract text using PyMuPDF.
- Ask questions about the document.
- Generate answers based on the extracted document content.

### 🎙️ Audio Transcription
- Upload audio files in supported formats.
- Convert speech into text.
- Uses Whisper Large V3 Turbo through Groq's API.
- Download the transcription as a text file.

## 🛠️ Tech Stack

- **Language:** Python
- **Web Framework:** Streamlit
- **LLM API Integration:** OpenRouter
- **Speech-to-Text:** Groq API and Whisper Large V3 Turbo
- **PDF Processing:** PyMuPDF
- **Environment Variables:** python-dotenv
- **API Client Libraries:** OpenAI Python SDK and Groq Python SDK

## 📁 Project Structure

```text
basic-multimodal-ai/
├── app.py
├── image_assistant.py
├── pdf_assistant.py
├── audio_assistant.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

The `.env` file stores API keys locally and should not be committed to version control.

## ⚙️ Setup and Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd basic-multimodal-ai
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
GROQ_API_KEY=your_groq_api_key
```

Replace the placeholder values with your own API keys.

**Never publish your real API keys or commit your `.env` file to GitHub.**

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to use the application.

## 🚀 How to Use

1. Launch the Streamlit application.
2. Select Image Captioning, PDF Question Answering, or Audio Transcription from the sidebar.
3. Upload a supported file.
4. Run the selected operation.
5. View the result in the application.

## 🔐 API Requirements

This application uses external AI services.

- Image captioning and PDF question answering require an appropriately configured OpenRouter API key.
- Audio transcription requires a Groq API key.
- API access, rate limits, and charges depend on each provider's current policies and account limits.

## 🎯 Learning Outcomes

Through this project, I practised:

- Integrating existing AI models through APIs.
- Working with vision-language models.
- Extracting and processing PDF text.
- Implementing document question answering.
- Integrating speech-to-text functionality.
- Managing API keys using environment variables.
- Building an interactive AI application with Streamlit.
- Combining multiple AI capabilities into one application.

## 🔮 Future Improvements

- Add OCR support for scanned PDFs.
- Improve document question answering using retrieval-augmented generation (RAG).
- Add multilingual audio transcription options.
- Improve error handling and API retry logic.
- Add conversation history and a more polished user interface.
- Deploy the application to a hosting platform.

## 👨‍💻 Author

Developed as a hands-on project to explore practical AI engineering and multimodal application development.