from openai import OpenAI

from config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_search_query(description):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that generates search queries for images. "
                           "Give only one simple search query."
            },
            {
                "role": "user",
                "content": f"Generate a search query for images of: {description}"}
        ]
    )

    return completion.choices[0].message.content


def analyze_images(images_64, description):
    images = [
        {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{image64}"
            }
        } for image64 in images_64
    ]
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"How well does this images match the description: '{description}'?"
                            f"In your answer must be only one number of the image that best matches the description."
                },
            ]
        }
    ]
    messages[0]["content"].extend(images)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
    )
    return response.choices[0].message.content


def extract_objects(image_64):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Identify and list all distinct objects in this image."
                                "Your response must be ONLY a list of objects."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_64}"
                        }
                    }

                ]
            },

        ]
    )

    return completion.choices[0].message.content
