import json
import requests

# https://telegram-bot-sdk.readme.io/reference/getme
# https://core.telegram.org/bots/api#available-methods
# https://core.telegram.org/bots/api#reactiontype

SETTINGS = json.loads(open('settings.json', 'r').read())

TOKEN = SETTINGS['vars']['telegram_token']
# TOKEN = SETTINGS['telegram']['token']
base_url = f"https://api.telegram.org/bot{TOKEN}"

# getMe
resp = requests.get(f"{base_url}/getMe")
resp.status_code
print(json.dumps(resp.json(), indent=4))


# getUpdates - all chats
resp = requests.get(f"{base_url}/getUpdates")
resp.status_code
print(json.dumps(resp.json(), indent=4))


CHAT_ID = 15753811

# getChat  - chat details
resp = requests.get(f"{base_url}/getChat?chat_id={CHAT_ID}")
resp.status_code
print(json.dumps(resp.json(), indent=4))


# sendMessage
headers = {
    'Content-Type': 'application/json'
}
data = {
    "chat_id": CHAT_ID,
    "text": "silent message test 😱",
    "disable_notification": False
}
resp = requests.post(f"{base_url}/sendMessage", json=data, headers=headers)
resp.status_code


# sendPhoto -- url
data = {
    "chat_id": CHAT_ID,
    "photo": "https://imgs.xkcd.com/comics/grownups.png",
    "caption": "this is  an example of a photo",
    "disable_notification": False
}

resp = requests.post(f"{base_url}/sendPhoto", json=data, headers=headers)
resp.status_code

# sendPhoto -- local file
file_path1 = "/home/rodri/projects/telegram_bot/img/raspberry-pi-pico-w.png"
file_path2 = "/home/rodri/Descargas/Ryu-Street-Fighters-removebg-preview.png"

files = {
    "photo": open(file_path2, 'rb')
}

data = {
    "chat_id": CHAT_ID,
    "caption": "second photo!!!",
    "disable_notification": False
}
resp = requests.post(f"{base_url}/sendPhoto?chat_id={CHAT_ID}", files=files)
resp.status_code


# setMessageReaction
#   'https://core.telegram.org/bots/api#reactiontype'
data = {
    "chat_id": CHAT_ID,
    "message_id": 646,
    "reaction": [{"type": 'emoji', "emoji": "👍"}],
    "is_big": True
}

resp = requests.post(f"{base_url}/setMessageReaction", json=data)
resp.status_code
print(json.dumps(resp.json(), indent=4))