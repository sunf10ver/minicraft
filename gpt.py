import requests
import base64

# Read and encode image as base64
try:
    with open("1433735650_472905306.jpg", "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")
    image_data_uri = f"data:image/png;base64,{base64_image}" # Ensure correct MIME type
except FileNotFoundError:
    print("Error: Image file not found.")
    exit()

# API request payload
url = "https://api.perplexity.ai/chat/completions"
headers = {
    "Authorization": "Bearer ",
    "accept": "application/json",
    "content-type": "application/json"
}
payload = {
    "model": "sonar-pro",
    "messages": [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Что изображено на картинке?"},
                {"type": "image_url", "image_url": {"url": image_data_uri}}
            ]
        }
    ],
    "stream": False
}

try:
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status() # Raise an exception for bad status codes
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"API Request failed: {e}")