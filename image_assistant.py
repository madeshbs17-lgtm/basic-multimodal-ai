import os
import base64
import mimetypes

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# Replace this with the vision model you selected on OpenRouter.
MODEL = "nvidia/nemotron-3.5-super-vl:free"


def encode_image(image_path):
    mime_type, _ = mimetypes.guess_type(image_path)

    if not mime_type or not mime_type.startswith("image/"):
        raise ValueError("Please provide a supported image file.")

    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(
            image_file.read()
        ).decode("utf-8")

    return f"data:{mime_type};base64,{image_data}"


def generate_caption(image_path):
    image_url = encode_image(image_path)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Describe this image clearly in 3-5 sentences. "
                            "Mention the main objects, setting, and visible "
                            "activities. Do not invent details that cannot "
                            "be determined from the image."
                        ),
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url,
                        },
                    },
                ],
            }
        ],
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    image_path = input("Enter your image path: ")

    try:
        caption = generate_caption(image_path)

        print("\n--- Image Caption ---")
        print(caption)

    except Exception as error:
        print(f"Something went wrong: {error}")