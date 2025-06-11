import random
import string
import requests

def generate_otp(length=6):
    return ''.join(random.choices(string.digits, k=length))

def send_sms_otp(phone_number, otp):
    message = f"Your decryption OTP is: {otp}"
    response = requests.post('https://textbelt.com/text', {
        'phone': phone_number,
        'message': message,
        'key': 'f7b6ca8e2bb28a784ce076b480fd7d5ee52b104cpTdSoJysbC1ll5oF1Wb6iFBZD', 
    })

    result = response.json()
    if not result.get("success"):
        print("SMS failed to send:", result.get("error"))
    else:
        print("OTP sent successfully.")
