from twilio.rest import Client
import random
import string
from config import TWILIO_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE

def generate_otp(length=6):
    return ''.join(random.choices(string.digits, k=length))

def send_sms_otp(phone_number, otp):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = f"Your decryption OTP is: {otp}"
    client.messages.create(to=phone_number, from_=TWILIO_PHONE, body=message)
