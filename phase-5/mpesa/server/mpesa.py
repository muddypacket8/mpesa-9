# import base64
# import datetime
# import requests
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # Replace these with your actual values from .env file or other configuration
# MPESA_CONSUMER_KEY = "czDU1qJDtkhfYapAosFZAezzt2wVrL1m"
# MPESA_CONSUMER_SECRET = "ZJiMW22UALvlbEtu"

# MPESA_PAYBILL = "174379"
# MPESA_PASSKEY = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
# CALLBACK_URL = "YOUR_CALLBACK_URL"
# CALLBACK_ROUTE = "YOUR_CALLBACK_ROUTE"

# token = None


# @app.route("/stk", methods=["POST"])
# def stk_push():
#     global token

#     if token is None:
#         token = get_access_token()

#     data = request.get_json()
#     phone = data["phone"][1:]  # formatted to 72190........
#     amount = data["amount"]

#     timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#     short_code = MPESA_PAYBILL
#     passkey = MPESA_PASSKEY

#     password = base64.b64encode(f"{short_code}{passkey}{timestamp}".encode()).decode()
#     # headers = {
#     #     'Content-Type': 'application/json',
#     #     'Authorization': 'Bearer x7ObHt5HYDuFZ7wOQLjmsseD0BX0'
#     #     }

#     payload = {
#         "BusinessShortCode": 174379,
#         "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjMwODAzMTYxODU0",
#         "Timestamp": "20230803161854",
#         "TransactionType": "CustomerPayBillOnline",
#         "Amount": 1,
#         "PartyA": 254708374149,
#         "PartyB": 174379,
#         "PhoneNumber": 254794199883,
#         "CallBackURL": "https://mydomain.com/",
#         "AccountReference": "CompanyXLTD",
#         "TransactionDesc": "Payment of X" 
#     }

#     response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, data = payload)
#     print(response.text.encode('utf8'))

#     return jsonify(response.json())


# @app.route(f"/{CALLBACK_ROUTE}", methods=["POST"])
# def callback():
#     data = request.get_json()

#     if "stkCallback" not in data["Body"]:
#         print(data["Body"]["stkCallback"]["ResultDesc"])
#         return jsonify("ok"), 200

#     amount = data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][0]["Value"]
#     code = data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][1]["Value"]
#     phone1 = str(data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][4]["Value"])[3:]
#     phone = f"0{phone1}"

#     # saving the transaction to db
#     print({"phone": phone, "code": code, "amount": amount})

#     # Assuming you have a MongoDB connection and model similar to the JavaScript code

#     return jsonify("ok"), 200


# @app.route("/stkpushquery", methods=["POST"])
# def stk_push_query():
#     if token is None:
#         token = get_access_token()

#     data = request.get_json()
#     checkout_request_id = data["CheckoutRequestID"]

#     timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#     short_code = MPESA_PAYBILL
#     passkey = MPESA_PASSKEY

#     password = base64.b64encode(f"{short_code}{passkey}{timestamp}".encode()).decode()

#     payload = {
#         "BusinessShortCode": short_code,
#         "Password": password,
#         "Timestamp": timestamp,
#         "CheckoutRequestID": checkout_request_id,
#     }

#     # =headers = {
#     #     'Content-Type': 'application/json',
#     #     'Authorization': 'Bearer x7ObHt5HYDuFZ7wOQLjmsseD0BX0'
#     #     }

#     response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, data = payload)
#     print(response.text.encode('utf8'))

#     return jsonify(response.json())


# def get_access_token():
#     key = MPESA_CONSUMER_KEY
#     secret = MPESA_CONSUMER_SECRET
#     auth = base64.b64encode(f"{key}:{secret}".encode()).decode()

#     response = requests.request("GET",
#          'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials',
#          headers = { 'Authorization': 'Bearer cFJZcjZ6anEwaThMMXp6d1FETUxwWkIzeVBDa2hNc2M6UmYyMkJmWm9nMHFRR2xWOQ==' })
#     print(response.text.encode('utf8'))

#     token = response.json().get("access_token")
#     return token


# if __name__ == "__main__":
#     app.run(host = "0.0.0.0", port = 3500, debug = True)
    
