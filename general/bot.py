import requests


def send_telegram_message(bot_token, chat_id, message_text):
    """

    :param bot_token:
    :param chat_id:
    :param message_text:
    """
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message_text
    }
    response = requests.post(url, json=payload)
    if response.ok:
        print("Message sent successfully")
    else:
        print("Failed to send message. Status code:", response.status_code)



