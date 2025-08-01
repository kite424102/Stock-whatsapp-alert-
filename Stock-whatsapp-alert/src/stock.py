PK     PํZฟ*ดํิ  ิ     main.pyfrom flask import Flask, request
from twilio.rest import Client
import os

app = Flask(__name__)

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
from_number = 'whatsapp:+14155238886'

recipients = [
    'whatsapp:+919901849885',
    'whatsapp:+918546979139'
]

client = Client(account_sid, auth_token)

@app.route('/')
def home():
    return "โ Stock Alert Bot Running"

@app.route('/whatsapp', methods=['POST'])
def whatsapp_webhook():
    incoming_msg = request.values.get('Body', '').strip().lower()
    from_number = request.values.get('From', '')
    response_msg = "๐ค Automated Stock Alert Bot. Please wait for updates."
    return response_msg, 200

@app.route('/send-dummy-alert', methods=['GET'])
def send_dummy_alert():
    msg = (
        "๐ข *Dummy Stock Alert*
"
        "๐๏ธ Sample Filing
"
        "๐ 13 Jul 2025, 11:00 AM
"
        "๐ https://dummy-link.com"
    )
    for to in recipients:
        client.messages.create(body=msg, from_='whatsapp:+14155238886', to=to)
    return "โ Dummy alert sent"

@app.route('/send-yesterday-stock-updates', methods=['GET'])
def send_yesterday_stock_updates():
    messages = [
        (
            "๐งพ *Fineotex Chemicals โ 12 Jul 2025*

"
            "๐ข *Fineotex Chemicals*
"
            "๐๏ธ Regulation 30 โ Director Reappointments
"
            "๐ Re-appointed: Bindu Darshan Shah, Sunil Waghmare, Sanjay Tibrewala & Surendra Tibrewala
"
            "๐ Filing Time: 3:26 PM
"
            "๐ https://www.bseindia.com/xml-data/corpfiling/AttachLiveLink1.pdf"
        ),
        (
            "๐งพ *GPT Healthcare โ 12 Jul 2025*

"
            "๐ข *GPT Healthcare*
"
            "๐๏ธ Annual Report & AGM Notice (36th AGM)
"
            "๐๏ธ AGM Date: 5 Aug 2025
"
            "๐ Filing Time: 5:30 PM
"
            "๐ https://nsearchives.nseindia.com/corporate/GPTHEALTHCARE_12072025173015_GHLSubmissionofLetter36_1_12072025.pdf"
        )
    ]

    for msg in messages:
        for to in recipients:
            client.messages.create(body=msg, from_='whatsapp:+14155238886', to=to)

    return "โ Yesterday's stock updates sent via WhatsApp!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)PK     PํZผcz$   $      requirements.txtflask
twilio
requests
beautifulsoup4PK     PํZ-7ฤ         Procfileweb: python main.pyPK     PํZฟ*ดํิ  ิ             ค    main.pyPK     PํZผcz$   $              ค๙  requirements.txtPK     PํZ-7ฤ                 คK	  ProcfilePK      ฉ   	    