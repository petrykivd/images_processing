import re
from PIL import Image
import os

from config import settings


def parse_gpt_response(response):
    pattern = r'(\d+)\.\s*(.*?):\s*\[([0-9.]+),\s*([0-9.]+),\s*([0-9.]+),\s*([0-9.]+)\]'

    objects = []
    for match in re.finditer(pattern, response):
        name = match.group(2)
        coords = [float(match.group(i)) for i in range(3, 7)]
        objects.append((name, coords))

    return objects


def crop_objects(image_path, objects, output_folder):
    with Image.open(os.path.join(settings.DOWNLOAD_FOLDER, image_path)) as img:
        width, height = img.size

        os.makedirs(output_folder, exist_ok=True)
        outputs = []
        for i, (name, coords) in enumerate(objects):
            x1, y1, x2, y2 = [
                int(coords[0] * width),
                int(coords[1] * height),
                int(coords[2] * width),
                int(coords[3] * height)
            ]

            cropped = img.crop((x1, y1, x2, y2))
            output_path = os.path.join(output_folder, f"{i + 1}_{name.replace(' ', '_')}.png")
            cropped.save(output_path)
            outputs.append(output_path)

        return outputs
