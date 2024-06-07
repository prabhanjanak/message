import streamlit as st
from twilio.rest import Client
from datetime import datetime

# Twilio credentials
account_sid = 'AC2986ca87648975a7af67fdb1eaa7f7f3'  # Replace with your Twilio account SID
auth_token = 'c37e8d12028881e255926a3367867046'  # Replace with your Twilio Auth Token
twilio_phone_number = '+12283382526'  # Replace with your Twilio phone number
destination_phone_number = '+918951568286'  # Replace with the recipient's phone number

# Create a Streamlit app
st.title("Slot Booking App")

# Get slot number and current datetime
slot_number = st.text_input("Enter Slot Number")
current_time = datetime.now().strftime('%H:%M:%S')
current_date = datetime.now().strftime('%Y-%m-%d')

# Prepare message body
message_body = f"Your slot number {slot_number} has been booked on {current_time} and {current_date}."

# Initialize the Twilio client
client = Client(account_sid, auth_token)

# Send the message
if st.button("Book Slot"):
    message = client.messages.create(
        body=message_body,
        from_=twilio_phone_number,
        to=destination_phone_number
    )
    st.write(f"Message Successfully Sent With SID: {message.sid}")
