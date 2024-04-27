import socket
import time

# Fungsi untuk mengirim jawaban ke server
def send_response(server_address, color_translation):
    client_socket.sendto(color_translation.encode(), server_address)

# Membuat soket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_host = 'localhost'
server_port = 12345

# Mengirim pesan inisialisasi ke server untuk memulai komunikasi
init_message = "Hello, server!"
client_socket.sendto(init_message.encode(), (server_host, server_port))

print(f"Client is connected with server: {server_host} {server_port}")

# Loop untuk menerima warna dan mengirim jawaban
while True:
    print("Waiting color from server...")
    data, server = client_socket.recvfrom(1024)
    color_received = data.decode()
    print(f"Server say: {color_received}")
    
    # Mendapatkan jawaban dari user
    print("Please enter the color translation in Indonesian (5 Second answer) :")
    user_answer = input()
    send_response(server, user_answer)
    
    # Menerima feedback dari server
    feedback, server = client_socket.recvfrom(1024)
    print(f"Server say: {feedback.decode()}")
