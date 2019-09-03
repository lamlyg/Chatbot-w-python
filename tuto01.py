# -*- coding: utf-8 -*-
"""

"""
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN = 'EAAPrTVdOBBIBAK0vHTlbr5mBAOwIpaZBbkYLCPjYlMwtWsVvZAWb1tIhXn1ZCx2dfntFuC1VXrMJJHCugnNr9OJP9FZCbHpKGTx04mBhFtpnve8EcEZAvfGc6b0ZALpNA3YwDHlOuH5tVQVof75CuWK6UeBNpeeQTZBJoqKZBgfwEwOsJH23Bqzv'  #토큰
VERIFY_TOKEN = 'ynzchatbot' #콜백 URL 확인 토큰 
bot = Bot(ACCESS_TOKEN)

# localhost:5000 접속했을때 데이터 처리
@app.route('/', methods=['GET','POST'])
def receive_message():
    if request.method == 'GET':
        """
        사전에 설정한 VERIFY_TOKEN을 확인함으로써 데이터 요청이 Facebook 을 통해서
        들어온 것인지 확인하는 과정
        """ 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    return 'Hello World!'

def verify_fb_token(token_sent):
    """
    VERIFY_TOKEN 이 우리가 설정한거랑 일치하는지 확인 
    일치하면 요청 허용, 그렇지 않으면 오류
    """
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

# Localhost:5000/Home 접속했을때 데이터 처리
@app.route('/Home', methods=['GET','POST'])
def home():
    return 'My Sweet Home!'

if __name__ == '__main__':
    app.run()
