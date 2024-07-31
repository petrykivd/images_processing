import os
from time import sleep

from loguru import logger

from config import settings
from core.image_saver import save_image, encode_image
from core.image_searcher import search_images
from core.openai_utils import generate_search_query, analyze_images, extract_objects
from image_visualizer import display_selected_images


def main():
    logger.info("Starting the image search process")
    os.makedirs(settings.DOWNLOAD_FOLDER, exist_ok=True)
    sleep(1)

    image_description = input("Enter a description of the image: ")

    search_query = generate_search_query(image_description)
    logger.info(f"Generated search query: {search_query}")

    image_urls = search_images(search_query)
    logger.info(f"{len(image_urls)} images found")

    saved_images = []
    for i, url in enumerate(image_urls):
        image_name = f"{image_description}_{i + 1}.jpg"
        saved_image = save_image(url, image_name)
        if saved_image:
            saved_images.append(saved_image)

    downloaded_images_base64 = [encode_image(image_name) for image_name in saved_images]
    best_match_image_number = int(analyze_images(downloaded_images_base64, image_description))
    logger.info(f"The best image is by number: {best_match_image_number}")

    objects = extract_objects(downloaded_images_base64[best_match_image_number - 1])
    logger.info(f"Extracted objects: {objects}")

    display_selected_images(saved_images)


if __name__ == "__main__":
    main()
