import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    print("Ubuntu-Inspired Image Fetcher: 'I am because we are' 🌍")
    
    # Prompt user for URL
    image_url = input("Please enter the image URL: ").strip()

    # Create directory "Fetched_Images" if it doesn't exist
    directory = "Fetched_Images"
    os.makedirs(directory, exist_ok=True)

    try:
        # Fetch the image using requests
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()  # Check for HTTP errors

        # Try to extract a filename from the URL
        parsed_url = urlparse(image_url)
        filename = os.path.basename(parsed_url.path)

        # If URL does not contain a filename, generate a unique one
        if not filename or '.' not in filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"

        filepath = os.path.join(directory, filename)

        # Save image in binary mode
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✅ Image successfully fetched and saved as: {filepath}")

    except requests.exceptions.RequestException as e:
        print("❌ An error occurred while trying to fetch the image.")
        print(f"Reason: {e}")
    except Exception as e:
        print("❌ An unexpected error occurred.")
        print(f"Details: {e}")

if __name__ == "__main__":
    fetch_image()
