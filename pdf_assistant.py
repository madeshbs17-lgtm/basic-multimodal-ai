import os

import pymupdf
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

MODEL = "nvidia/nemotron-3.5-super-vl:free"


def extract_pdf_text(pdf_path):
    """Extract text from a PDF document."""

    with pymupdf.open(pdf_path) as document:
        pages = []

        for page_number, page in enumerate(document, start=1):
            text = page.get_text().strip()

            if text:
                pages.append(
                    f"Page {page_number}:\n{text}"
                )

    return "\n\n".join(pages)


def ask_pdf_question(pdf_path, question):
    """Answer a question using the extracted PDF text."""

    document_text = extract_pdf_text(pdf_path)

    if not document_text:
        return (
            "No selectable text was found in this PDF. "
            "It may be scanned or image-based."
        )

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You answer questions using the provided PDF text. "
                    "Use only information supported by the document. "
                    "If the answer is not present, say that the PDF "
                    "does not provide the answer. Do not invent facts."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"PDF CONTENT:\n{document_text}\n\n"
                    f"QUESTION:\n{question}"
                ),
            },
        ],
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    pdf_path = input("Enter the PDF file path: ")
    question = input("Ask a question about the PDF: ")

    try:
        answer = ask_pdf_question(pdf_path, question)

        print("\n--- Answer ---")
        print(answer)

    except FileNotFoundError:
        print("Error: The specified PDF file was not found.")

    except Exception as error:
        print(f"Something went wrong: {error}")