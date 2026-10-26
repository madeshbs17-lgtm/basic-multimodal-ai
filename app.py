import streamlit as st
import tempfile
from pathlib import Path

from image_assistant import generate_caption
from pdf_assistant import ask_pdf_question
from audio_assistant import transcribe_audio


st.set_page_config(
    page_title="Multimodal AI Assistant",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 Multimodal AI Assistant")
st.write("One application for images, PDFs, and audio.")

mode = st.sidebar.selectbox(
    "Choose a feature",
    [
        "Image Captioning",
        "PDF Question Answering",
        "Audio Transcription",
    ],
)


# IMAGE CAPTIONING
if mode == "Image Captioning":
    st.header("🖼️ Image Captioning")

    uploaded_image = st.file_uploader(
        "Upload an image",
        type=["png", "jpg", "jpeg", "webp"],
    )

    if uploaded_image is not None:
        st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)

        if st.button("Generate Caption"):
            temp_path = None

            try:
                suffix = Path(uploaded_image.name).suffix or ".jpg"

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=suffix,
                ) as temp_file:
                    temp_file.write(uploaded_image.getvalue())
                    temp_path = temp_file.name

                with st.spinner("Generating caption..."):
                    caption = generate_caption(temp_path)

                st.subheader("Generated Caption")
                st.write(caption)

            except Exception as error:
                st.error(f"Could not generate caption: {error}")

            finally:
                if temp_path and Path(temp_path).exists():
                    Path(temp_path).unlink()


# PDF QUESTION ANSWERING
elif mode == "PDF Question Answering":
    st.header("📄 PDF Question Answering")

    uploaded_pdf = st.file_uploader(
        "Upload a PDF document",
        type=["pdf"],
    )

    question = st.text_input(
        "Ask a question about the document",
        placeholder="What is this document about?",
    )

    if st.button("Ask Question"):
        if uploaded_pdf is None:
            st.warning("Please upload a PDF first.")

        elif not question.strip():
            st.warning("Please enter a question.")

        else:
            temp_path = None

            try:
                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".pdf",
                ) as temp_file:
                    temp_file.write(uploaded_pdf.getvalue())
                    temp_path = temp_file.name

                with st.spinner("Reading the PDF and generating an answer..."):
                    answer = ask_pdf_question(temp_path, question.strip())

                st.subheader("Answer")
                st.write(answer)

            except Exception as error:
                st.error(f"Could not answer your question: {error}")

            finally:
                if temp_path and Path(temp_path).exists():
                    Path(temp_path).unlink()


# AUDIO TRANSCRIPTION
elif mode == "Audio Transcription":
    st.header("🎙️ Audio Transcription")

    uploaded_audio = st.file_uploader(
        "Upload an audio file",
        type=["mp3", "wav", "m4a", "ogg", "webm", "flac"],
    )

    if uploaded_audio is not None:
        st.audio(uploaded_audio)

        if st.button("Transcribe Audio"):
            temp_path = None

            try:
                suffix = Path(uploaded_audio.name).suffix or ".mp3"

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=suffix,
                ) as temp_file:
                    temp_file.write(uploaded_audio.getvalue())
                    temp_path = temp_file.name

                with st.spinner("Transcribing audio..."):
                    transcription = transcribe_audio(temp_path)

                st.subheader("Transcription")
                st.write(transcription)

                st.download_button(
                    "Download Transcription",
                    data=transcription,
                    file_name="transcription.txt",
                    mime="text/plain",
                )

            except Exception as error:
                st.error(f"Could not transcribe audio: {error}")

            finally:
                if temp_path and Path(temp_path).exists():
                    Path(temp_path).unlink()