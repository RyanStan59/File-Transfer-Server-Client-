import socket
import os
import threading
from serverui import serverui  # Assuming serverui is a separate file

# Server configuration
HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 65432       # Port to listen on
BUFFER_SIZE = 1024

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print(f'Error: Creating directory. {directory}')

def handle_client(conn, addr):
    print('Connected by', addr)
    filename = conn.recv(BUFFER_SIZE).decode()
    print(f"Receiving file: {filename}")

    # Send confirmation to the client
    conn.send(b"Filename received")

    # Receive file size
    filesize = int(conn.recv(BUFFER_SIZE).decode())
    print(f"File size: {filesize} bytes")

    # Send confirmation to the client
    conn.send(b"Filesize received")
    
    # Receive file data
    with open(filename, 'wb') as f:
        bytes_received = 0
        while bytes_received < filesize:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            f.write(data)
            bytes_received += len(data)
    
    print(f"File {filename} successfully received")
    conn.close()

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        
        print(f"Server running on {HOST}:{PORT}")
        
        # Accept client connections in a loop
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

def start_server_thread():
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

if __name__ == "__main__":
    start_server_thread()
    
    # Run the UI
    serverui(HOST, PORT)
