import requests
from config import *


def sendEmail(email, subject, body):
    url = email_url

    payload = "{\n \"emailaddress\":\"" + email + "\"," \
                "\n \"emailSubject\": \"" + subject + "\"," \
                "\n \"emailBody\": \"" + body + "\"\n}"

    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        }

    requests.request("POST", url, data=payload, headers=headers)
