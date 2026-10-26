import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

MODEL = "whisper-large-v3-turbo"


def transcribe_audio(audio_path):
    """Convert speech in an audio file into text."""

    audio_file = Path(audio_path)

    if not audio_file.is_file():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    with audio_file.open("rb") as file:
        transcription = client.audio.transcriptions.create(
            file=(audio_file.name, file.read()),
            model=MODEL,
            response_format="json",
        )

    return transcription.text


if __name__ == "__main__":
    audio_path = input("Enter the audio file path: ").strip().strip('"')

    try:
        result = transcribe_audio(audio_path)

        print("\n--- Transcription ---")
        print(result)

    except FileNotFoundError as error:
        print(f"Error: {error}")

    except Exception as error:
        print(f"Something went wrong: {error}")