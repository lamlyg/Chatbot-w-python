# -*- coding: utf-8 -*-
"""
목표 : 가장 기본적인 형태를 익혀봅시다.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def receive_message():
    return 'Hello World!'

@app.route('/Home', methods=['GET','POST'])
def home():
    return 'My Sweet Home!'

if __name__ == '__main__':
    app.run()
