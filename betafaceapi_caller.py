import requests
import base64
import time

# Your FREE BetaFace credentials
API_KEY = "d45fd466-51e2-4701-8da8-04351c872236"
API_SECRET = "171e8465-f548-401d-b63b-caf0dc28df5f"

# Local path to the image file
IMAGE_PATH = "images/image_6.jpg"  # Change this to your image file path

def encode_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def upload_and_get_classifiers(image_path):
    image_base64 = encode_image(image_path)

    upload_url = "https://www.betafaceapi.com/api/v2/media"
    headers = {"Content-Type": "application/json"}

    # Upload image to BetaFace
    payload = {
        "api_key": API_KEY,
        "api_secret": API_SECRET,
        "file_base64": image_base64,
        "detection_flags": "classifiers",
        "original_filename": image_path
    }

    response = requests.post(upload_url, json=payload, headers=headers)
    response_data = response.json()

    media_id = response_data.get("media", {}).get("media_id")
    if not media_id:
        print("Failed to upload image:", response_data)
        return

    print(f"Image uploaded. Media ID: {media_id}")

    # Wait for processing (5 seconds is good for free tier)
    time.sleep(5)

    # Poll result
    status_url = f"https://www.betafaceapi.com/api/v2/media/{media_id}"
    status_payload = {
        "api_key": API_KEY,
        "api_secret": API_SECRET
    }

    result = requests.post(status_url, json=status_payload, headers=headers)
    result_data = result.json()

    try:
        face = result_data["media"]["faces"][0]
        print("\nFace Classifiers:")
        for classifier in face.get("classifiers", []):
            name = classifier["name"]
            value = classifier["value"]
            confidence = classifier["confidence"]
            print(f"{name}: {value} (confidence: {confidence:.2f})")
    except Exception as e:
        print("Could not extract classifiers:", e)

# Run the function
upload_and_get_classifiers(IMAGE_PATH)
