import json
import os
import requests

path = os.path.dirname(os.path.abspath(__file__))


def get_token():
    try:
        secret_file = path + "\secrets.json"
        with open(secret_file) as f:
            secrets = json.loads(f.read())
        myToken = secrets["Token"]
        return myToken
    except:
        return False
    

# 채널명, 내용을 입력받고, 토큰을 파일로부터 획득하여 해당 채널에 내용을 post
def to_slack(text, channel="#일반"):
    myToken = get_token()
    if not myToken:
        return "No secret key! Message Failed."
    response = requests.post(
        "https://slack.com/api/chat.postMessage",
        data={"token": myToken, "channel": channel, "text": text},
    )
    if response.status_code == 200:
        return "Sucessfully Sent!"
    else:
        return "Message Failed while Posting.."