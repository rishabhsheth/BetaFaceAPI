import requests

# File path to the image
file_path = "./image/image_9.jpg"

# API endpoint and credentials
url = "https://www.betafaceapi.com/api/v2/media/file"
api_key = "d45fd466-51e2-4701-8da8-04351c872236"

# Prepare multipart form data
files = {
    "file": ("image_9.jpg", open(file_path, "rb"), "image/jpeg")
}
data = {
    "api_key": api_key
}
headers = {
    "accept": "application/json"
}

# Send the request
response = requests.post(url, headers=headers, files=files, data=data)

# Save to output file
with open("../output9.json", "w") as out_file:
    out_file.write(response.text)

# Optional: Print status
print("✅ Upload complete. Response saved to ../output9.json")
