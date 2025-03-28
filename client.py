import requests

# Server details
url = 'http://<SERVER_IP>:5000/upload'  # Replace with your server IP

# File to upload
file_path = 'path_to_your_file'  # Replace with the file you want to upload

# Open the file and send it to the server
with open(file_path, 'rb') as f:
    files = {'file': (file_path, f)}
    response = requests.post(url, files=files)

# Print the response from the server
print(response.text)
