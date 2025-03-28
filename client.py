import socket
import os
from clientui import clientui

# Server configuration
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
BUFFER_SIZE = 1024
clientui()

def send_file(filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # Send filename
        s.send(filename.encode())
        ack = s.recv(BUFFER_SIZE)
        if ack.decode() != "Filename received":
             raise Exception("Filename not acknowledged by the server")

        # Send file size
        filesize = os.path.getsize(filename)
        s.send(str(filesize).encode())

        ack = s.recv(BUFFER_SIZE)
        if ack.decode() != "Filesize received":
             raise Exception("Filesize not acknowledged by the server")
        
        # Send file data
        with open(filename, 'rb') as f:
            while True:
                data = f.read(BUFFER_SIZE)
                if not data:
                    break
                s.send(data)
        print(f"File {filename} successfully sent")

if __name__ == "__main__":
    filename = "example.txt"  # Replace with your file name
    # Create a dummy file for testing
    with open(filename, 'w') as f:
        f.write("This is a test file.")
    send_file(filename)