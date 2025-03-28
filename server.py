from flask import Flask, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'  # Folder to save the uploaded files
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return """
        <h1>File Upload Server</h1>
        <form method="POST" enctype="multipart/form-data" action="/upload">
            <input type="file" name="file"><br>
            <input type="submit" value="Upload">
        </form>
    """

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    # Save the file in the "uploads" folder
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Simulate packet receipt in the terminal
    print(f"Starting to receive file: {file.filename}")
    total_size = len(file.read())  # Get the total size of the file
    packet_size = 1024  # Simulating packet size
    packets_received = 0

    with open(file_path, 'wb') as f:
        file.seek(0)  # Rewind the file pointer to the beginning
        while True:
            chunk = file.read(packet_size)
            if not chunk:
                break
            f.write(chunk)
            packets_received += 1
            print(f"Received packet {packets_received} out of {total_size // packet_size}")

    print(f"File successfully received and saved to {file_path}")
    return f"File uploaded successfully! File saved to {file_path}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
