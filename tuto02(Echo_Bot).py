# -*- coding: utf-8 -*-
import random
from flask import Flask, request
from pymessenger.bot import Bot

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
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
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
    app.run()