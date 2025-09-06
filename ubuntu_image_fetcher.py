import os
import requests
from urllib.parse import urlparse
import uuid
import hashlib

# Constants
DIRECTORY = "Fetched_Images"
ACCEPTED_CONTENT_TYPES = ["image/jpeg", "image/png", "image/gif", "image/webp"]

# Create directory if it doesn't exist
os.makedirs(DIRECTORY, exist_ok=True)

# Set of hashes to detect duplicates
downloaded_hashes = set()

def get_file_extension(content_type):
    """Map content-type to file extension"""
    mapping = {
        "image/jpeg": ".jpg",
        "image/png": ".png",
        "image/gif": ".gif",
        "image/webp": ".webp"
    }
    return mapping.get(content_type, ".img")

def hash_image_content(content):
    """Return SHA256 hash of the image content"""
    return hashlib.sha256(content).hexdigest()

def fetch_image(url):
    try:
        # Basic safety precaution — only allow HTTP/HTTPS
        if not url.lower().startswith(('http://', 'https://')):
            print(f"⚠️ Skipping invalid URL (not HTTP/HTTPS): {url}")
            return

        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Check Content-Type header
        content_type = response.headers.get("Content-Type", "").split(";")[0].lower()
        if content_type not in ACCEPTED_CONTENT_TYPES:
            print(f"⚠️ Unsupported content type ({content_type}) at URL: {url}")
            return

        # Read content safely
        content = response.content

        # Check for duplicate using hash
        content_hash = hash_image_content(content)
        if content_hash in downloaded_hashes:
            print(f"♻️ Duplicate image detected. Skipping URL: {url}")
            return
        else:
            downloaded_hashes.add(content_hash)

        # Extract or generate filename
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename or '.' not in filename:
            extension = get_file_extension(content_type)
            filename = f"image_{uuid.uuid4().hex}{extension}"

        filepath = os.path.join(DIRECTORY, filename)

        # Save image
        with open(filepath, 'wb') as f:
            f.write(content)

        print(f"✅ Downloaded and saved: {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Network error while fetching {url}: {e}")
    except Exception as e:
        print(f"❌ Unexpected error with URL {url}: {e}")

def main():
    print("Ubuntu-Inspired Multi-Image Fetcher")
    print("Enter multiple image URLs (one per line). Type 'done' to finish:\n")

    urls = []
    while True:
        url = input("Image URL: ").strip()
        if url.lower() == 'done':
            break
        if url:
            urls.append(url)

    if not urls:
        print("🚫 No URLs provided. Exiting.")
        return

    print("\n📥 Starting download...\n")
    for url in urls:
        fetch_image(url)

    print("\n🌍 All done! Images organized in the 'Fetched_Images' directory.")

if __name__ == "__main__":
    main()

