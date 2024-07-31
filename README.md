# Image Gathering and Processing Script

## Introduction

This project involves developing a script to gather and process images using the OpenAI API and a search engine. The script takes a description of an image, retrieves related images from a search engine, analyzes them with a vision model, and extracts objects from the best-matching image.

## Objectives

- Generate a search prompt using the OpenAI API.
- Retrieve images from a search engine based on the generated search prompt.
- Analyze the retrieved images using OpenAI's vision model to select the image that best matches the description.
- Extract and save objects from the selected image as separate images.

## Requirements

- Python 3.x
- OpenAI API Key
- Google Search Engine API Key
- Google Custom Search Engine ID

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/petrykivd/images_processing.git
    cd images_processing
    ```
2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your .env:**
   - Create .env file in the root directory.
   - Add the environment variables like a `.env.example` file.


## Usage

1. **Run the script:**

    ```bash
    python main.py
    ```

    The script will:
    - Generate a search query from your description input.
    - Retrieve images related to the query.
    - Analyze these images to select the best match.
    - Extract objects from the selected image and save them as separate files.

2. **Output:**
    - `downloaded_images/` directory with the retrieved images.
    - `objects/` directory with separate images for each object found in the selected image.

## Contact

For any questions, please contact [petrykiv.dmytro19@gmail.com](mailto:petrykiv.dmytro19@gmail.com) or @accbuyer19 on Telegram.

<p align="center">
<img style="width: 100%;" src="https://i.postimg.cc/nzykWKNd/result.gif">
</p>