import requests
import platform


data = {
    "app_name": "Calculator",
    "version": platform.system(),
    "description": "A simple calculator app"
}

# Flask server URL
url = "http://127.0.0.1:5000/add-app"

# Sending POST request
response = requests.post(url, json=data)

# Log the response from server
if response.status_code == 201:
    print(data)
    print("Data sent successfully:", response.json())
else:
    print("Error sending data:", response.json())
