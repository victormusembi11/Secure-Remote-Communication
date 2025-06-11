import socket
from tkinter import *
from aes_utils import encrypt_message
from otp_sms import generate_otp, send_sms_otp

def send_message():
    message = msg_entry.get()
    otp = generate_otp()
    encrypted = encrypt_message(message, otp)
    conn.sendall(encrypted.encode())
    send_sms_otp(phone_entry.get(), otp)
    status_label.config(text="Message sent and OTP delivered!")

# GUI
root = Tk()
root.title("Sender")

Label(root, text="Receiver Phone:").pack()
phone_entry = Entry(root)
phone_entry.pack()

Label(root, text="Message:").pack()
msg_entry = Entry(root, width=40)
msg_entry.pack()

Button(root, text="Send Secure Message", command=send_message).pack()
status_label = Label(root, text="")
status_label.pack()

# Socket server
server = socket.socket()
server.bind(("0.0.0.0", 8080))
server.listen(1)
print("Waiting for receiver...")
conn, _ = server.accept()
print("Connected to receiver.")

root.mainloop()
