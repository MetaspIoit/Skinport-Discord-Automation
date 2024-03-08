import requests
import time

channel_id = 591956635262386177

def send_discord_message():
    payload = {
        "content": '''
<PUT YOUR MESSAGE HERE THAT YOU WANT DISPLAYED>
'''
    }

    header = {
        'Authorization': '<DISCORD TOKEN>'
    }

    while True:
        response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=header)

        if response.status_code == 200:
            print("Message sent successfully.")
        else:
            print(f"Failed to send message. Status code: {response.status_code}")

        time.sleep(6 * 60 * 60)  # Sleep for 6 hours before sending next message

# Call the function to start sending messages
send_discord_message()
