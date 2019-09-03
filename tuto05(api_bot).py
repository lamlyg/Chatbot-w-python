# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import random
import json
import os
from flask import Flask, request
from pymessenger.bot import Bot
from tuto04 import movie_showtime
from tuto06 import recent_alert

app = Flask(__name__)
ACCESS_TOKEN = 'EAAPrTVdOBBIBAKt3ZCWyr1HEHMghC5zCR62qzuonzZC06r7bb6J6wmWWk7KDEZCSSZBfxwU99GM2YpjDHNIeFe3lSF0r3tJFH5sPitVIZA2unfDT2DTq8BNqasz2MvO1wgxCZConfPmLRMasAtnikOLeId8ccuHmbbubQa0rNq3zyVosjB6bvT'
VERIFY_TOKEN = 'ynzchatbot'
bot = Bot(ACCESS_TOKEN)


@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
        output = request.get_json()
        with open('request.json', 'w', encoding='UTF-8') as f:
            json.dump(output, f, indent=4, ensure_ascii=False)
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    recipient_id = message['sender']['id']
                    if message['message']['text'][:3] == '허걱맨':
                        movie_nm, movie_tm = movie_showtime(message['message']['text'][3:])
                        msg = movie_nm + "의 상영시간은 " + movie_tm + "분 입니다."
                        send_message(recipient_id, msg)
                    elif message['message']['text'] == '미세먼지':
                        msg = "최근 미세먼지 경보 지역은 " + recent_alert() + "입니다"
                        send_message(recipient_id, msg)

                    elif message['message'].get('text'):
                        response_sent_text = message['message']['text']
                        send_message(recipient_id, response_sent_text)

    return "Message Processed"


def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
