import requests

from config import settings


def search_images(query):
    params = {
        'key': settings.GOOGLE_SEARCH_ENGINE_API_KEY,
        'cx': settings.GOOGLE_SEARCH_ENGINE_CX,
        'q': query,
        'searchType': 'image',
        'num': settings.MAX_RESULTS * 2,
        'fileType': 'png|jpg|jpeg|webp',
    }

    response = requests.get(settings.SEARCH_ENGINE_URI, params=params)
    results = response.json()

    filtered_images = []
    for item in results.get('items', []):
        image_url = item['link']

        try:
            head = requests.head(image_url, allow_redirects=True)
            size = int(head.headers.get('Content-Length', 0))
            if size < 20 * 1024 * 1024:
                filtered_images.append(image_url)
            if len(filtered_images) == 5:
                break
        except:
            continue

    return filtered_images
