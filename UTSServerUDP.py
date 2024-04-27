import socket
import time
import random
from threading import Thread

# Daftar warna dalam bahasa Inggris dan Indonesia
colors = {
    "red": "merah",
    "green": "hijau",
    "blue": "biru",
    "yellow": "kuning",
    "black": "hitam",
    "white": "putih"
}

selected_color = None  # Variabel global untuk menyimpan warna terpilih

# Fungsi untuk mengirim kata warna kepada semua klien
def send_color_to_all_clients():
    global selected_color  # Menggunakan variabel global
    while True:
        if clients:
            selected_color = random.choice(list(colors.keys()))
            for client in clients:
                server_socket.sendto(selected_color.encode(), client)
            print("Sending new color to all client...")
            print("Wait for 10 second...")
        time.sleep(10)

# Membuat soket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = 'localhost'
port = 12345
server_socket.bind((host, port))

clients = set()
print(f"Server is running on {host} {port}")
print("Ready to connect client...")

# Thread untuk mengirim warna
thread = Thread(target=send_color_to_all_clients)
thread.start()

# Loop untuk menerima jawaban dan menambahkan klien baru
while True:
    message, address = server_socket.recvfrom(1024)
    if address not in clients:
        clients.add(address)
        print(f"Added new client: {address}")
    
    message = message.decode().lower()
    expected_answer = colors.get(selected_color, "")
    if message == expected_answer:
        server_socket.sendto("Correct Answer! Score [100]".encode(), address)
    else:
        server_socket.sendto("Wrong Answer! Score [0]".encode(), address)
