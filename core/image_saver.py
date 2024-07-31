import base64
import io
import os

import requests

from PIL import Image

from loguru import logger

from config import settings


def save_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        try:
            img = Image.open(io.BytesIO(response.content))
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            img.save(os.path.join(settings.DOWNLOAD_FOLDER, filename))
        except Image.UnidentifiedImageError:
            logger.warning(f"Cannot identify image file from URL: {url}")
            return None
    else:
        logger.warning(f"Failed to download image from URL: {url}, status code: {response.status_code}")
        return None
    return filename


def encode_image(image_path):
    with open(os.path.join(settings.DOWNLOAD_FOLDER, image_path), "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
