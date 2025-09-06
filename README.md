# Ubuntu-Inspired Image Fetcher 🖼️

> _"I am because we are."_ — Ubuntu Philosophy

This project is a simple but meaningful Python script inspired by the spirit of Ubuntu — a philosophy of community, respect, and sharing. The script connects to the web to fetch shared images and organizes them locally for later appreciation.

---

## 🌍 Project Purpose

In the spirit of Ubuntu, this tool:

- **Connects** to the broader internet community
- **Respects** the uncertainties of online connections by handling errors gracefully
- **Shares** downloaded images by organizing them for reuse
- **Serves** a real need — downloading and saving images efficiently

---

## 🧠 Features

- Prompts the user for an image URL
- Creates a `Fetched_Images` directory if it doesn't already exist
- Downloads the image from the provided URL using the `requests` library
- Extracts or generates a filename for the image
- Saves the image in binary mode
- Handles HTTP and other errors respectfully

---

## 🧪 Challenge Features Implemented

- ✅ **Handles Multiple URLs**: User can input as many URLs as needed
- ✅ **Safe Downloading**: Only downloads via `http/https`; validates content type
- ✅ **Duplicate Detection**: Uses image hashing to skip duplicates
- ✅ **Header Checking**: Verifies `Content-Type` before saving the file
- ✅ **Robust Error Handling**: Gracefully handles timeouts, invalid URLs, unsupported formats



---

## 🚀 How to Use

### 1. Clone this repository

```bash
git clone https://github.com/Berbaz/Ubuntu_Requests.git
cd Ubuntu_Requests
