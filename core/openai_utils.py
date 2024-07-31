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


def extract_objects(image_64, description):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"""
                        Carefully analyze the provided image and perform the following steps:
                        1. Identify all significant objects in the image, but don't identify {description}.
                        2. For each identified object, provide:
                        a) The name of the object
                        b) Precise coordinates of the bounding box in the format [x1, y1, x2, y2], where:
                          - (x1, y1) are the coordinates of the top-left corner of the box
                          - (x2, y2) are the coordinates of the bottom-right corner of the box
                        c) Coordinates should be normalized relative to the image size, where 0,0 is the top-left corner,
                        and 1,1 is the bottom-right corner of the image.
                        3. If an object is partially cropped by the edge of the image, still provide coordinates for 
                        its visible part.
                    
                        4. For irregularly shaped objects, try to encompass the entire object as accurately as possible, 
                        minimizing the inclusion of background.
                        
                        5. If objects overlap, provide coordinates for each separately, even if they partially overlap.
                        
                        6. For a group of very similar objects (e.g., a flock of birds), you can provide coordinates for 
                        the entire group, but also indicate the approximate number of objects in the group.
                        
                        Provide the answer ALWAYS ONLY in the following format:
                        1. [Object name]: [x1, y1, x2, y2]
                        2. [Object name]: [x1, y1, x2, y2]
                        ...
                        Please ensure that your coordinates are as accurate as possible, as they will be used for 
                        automatically cropping objects from the image.
                        """
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
