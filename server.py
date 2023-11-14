# Create server that accepts connections

import sqlite3
import hashlib
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))

server.listen()

def handle_connection(c):
    c.send("Username: ".encode())
    username = c.recv(1024).decode()
    c.send("Password: ".encode())
    password = c.recv(1024)
    password = hashlib.sha256(password).hexdigest() # if the password is correct it will equal to what's in the database

    conn = sqlite3.connect("userdata.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))

    if cur.fetacall():
        c.send("Login Successful!".encode())
        # secrets
        # services
    else:
        c.send("Login failed!".encode())


while True:
    client, addr = server.accept()
    threading.Thread(target=handle_connection, args=(client,)).start()