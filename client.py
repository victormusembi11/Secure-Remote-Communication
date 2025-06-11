import socket
from tkinter import *
from aes_utils import decrypt_message
import threading

received_encrypted = ""

def receive_data():
    global received_encrypted
    while True:
        data = client.recv(4096).decode()
        if data:
            received_encrypted = data
            message_label.config(text="Encrypted Message Received!")

def decrypt():
    otp = otp_entry.get()
    decrypted = decrypt_message(received_encrypted, otp)
    if decrypted:
        result_label.config(text="Decrypted: " + decrypted)
    else:
        result_label.config(text="Decryption failed. Incorrect OTP?")

# GUI
root = Tk()
root.title("Receiver")

Label(root, text="Enter OTP:").pack()
otp_entry = Entry(root)
otp_entry.pack()

Button(root, text="Decrypt Message", command=decrypt).pack()
message_label = Label(root, text="Waiting for message...")
message_label.pack()

result_label = Label(root, text="")
result_label.pack()

# Socket client
client = socket.socket()
client.connect(("localhost", 8080))

threading.Thread(target=receive_data, daemon=True).start()
root.mainloop()
