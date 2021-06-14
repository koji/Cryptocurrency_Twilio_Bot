from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import CryptoPrice
import requests
import re

app = Flask(__name__)


def check_numeric(s: str):
    pattern = r"^[+-]?[0-9]*[.]?[0-9]+$"
    return (re.match(pattern, s) is not None)


@app.route('/sms', methods=['GET', 'POST'])
def sms_reply():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    # print(incoming_msg)

    if 'price' in incoming_msg:
        # return cryptocurrency price
        crypto = incoming_msg.replace('price', '').strip().upper()
        cc = CryptoPrice.Crypto(crypto)
        crypto_price = str(cc.get_crypto_price())
        # print(crypto_price)

        if not check_numeric(crypto_price):
            response = crypto_price
        else:
            response = f"the current price of {crypto} is ${crypto_price} from cryptocompare"
        print(response)
        msg.body(response)
        responded = True

    if not responded:
        msg.body('what do you want to know about cryptocurrencies?')

    # print(str(resp))
    return str(resp)


if __name__ == '__main__':
    app.run(debug=True)
